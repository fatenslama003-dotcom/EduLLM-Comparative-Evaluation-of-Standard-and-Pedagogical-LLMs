import streamlit as st
import openai
import os
import csv
import datetime
import json
import time
from dotenv import load_dotenv
from prompts import REACTIVE_PROMPT, TUTOR_PROMPT, ADJUSTMENT_PROMPT
from problems import JAVA_PROBLEMS
from modules import MODULES

# Charger les variables d'environnement
load_dotenv()

st.set_page_config(page_title="Plateforme d'Apprentissage Java", layout="wide")

# --------------------------------------------------------------
# Configuration API (GitHub Models — endpoint compatible OpenAI)
# --------------------------------------------------------------
# GitHub Models n'est PAS GitHub Copilot (qui n'a pas d'API externe) : c'est
# un service à part, gratuit avec limites de débit, qui expose un endpoint
# compatible OpenAI. Il te faut un token GitHub (Settings > Developer
# settings > Personal access tokens > fine-grained) avec la permission
# "models: read". Mets-le dans ton fichier .env : GITHUB_TOKEN=ton_token
API_KEY = os.getenv("GITHUB_TOKEN")
BASE_URL = "https://models.github.ai/inference"
# Format obligatoire : "{éditeur}/{nom_du_modèle}". Quelques exemples valides :
# "openai/gpt-4.1", "openai/gpt-4o-mini", "meta/llama-3.3-70b-instruct".
MODEL = "openai/gpt-4o-mini"

if not API_KEY:
    st.error(
        "❌ Aucun token trouvé. Crée un fichier `.env` à la racine du projet "
        "contenant : GITHUB_TOKEN=ton_token_github (permission models: read)"
    )
    st.stop()

# FIX: un seul client créé une fois, réutilisé partout (au lieu d'en
# recréer un nouveau à chaque message).
client = openai.OpenAI(api_key=API_KEY, base_url=BASE_URL)

# --------------------------------------------------------------
# Initialisation des variables de session (UNE SEULE FOIS)
# --------------------------------------------------------------
if 'etape' not in st.session_state:
    st.session_state.etape = 'accueil'
if 'groupe' not in st.session_state:
    st.session_state.groupe = None
if 'nom_etudiant' not in st.session_state:
    st.session_state.nom_etudiant = ""
if 'age' not in st.session_state:
    st.session_state.age = 20
if 'niveau_etudes' not in st.session_state:
    st.session_state.niveau_etudes = "Licence"
if 'experience_prog' not in st.session_state:
    st.session_state.experience_prog = "Non, jamais"
if 'current_problem_index' not in st.session_state:
    st.session_state.current_problem_index = 0
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'pretest_answers' not in st.session_state:
    st.session_state.pretest_answers = {}
if 'posttest_answers' not in st.session_state:
    st.session_state.posttest_answers = {}
if 'transfert_answers' not in st.session_state:
    st.session_state.transfert_answers = {}
if 'pretest_start' not in st.session_state:
    st.session_state.pretest_start = None
if 'pretest_questions' not in st.session_state:
    st.session_state.pretest_questions = []
if 'posttest_start' not in st.session_state:
    st.session_state.posttest_start = None
if 'posttest_questions' not in st.session_state:
    st.session_state.posttest_questions = []
if 'transfert_start' not in st.session_state:
    st.session_state.transfert_start = None
if 'transfert_questions' not in st.session_state:
    st.session_state.transfert_questions = []

# Gestion des modules
if 'page_apprentissage' not in st.session_state:
    st.session_state.page_apprentissage = 'selection'
if 'progression_modules' not in st.session_state:
    st.session_state.progression_modules = {}
# FIX: ce bloc était auparavant DANS le `if` ci-dessus, donc si tu ajoutais
# des modules plus tard dans une session déjà démarrée, les nouveaux
# modules n'avaient jamais d'entrée de progression -> plantage.
# Maintenant on complète toujours les entrées manquantes.
for i in range(len(MODULES)):
    if i not in st.session_state.progression_modules:
        st.session_state.progression_modules[i] = {
            'termine': False,
            'dernier_item': 0
        }
if 'module_index' not in st.session_state:
    st.session_state.module_index = 0
if 'item_index' not in st.session_state:
    st.session_state.item_index = 0
if 'messages_module' not in st.session_state:
    st.session_state.messages_module = []

# --------------------------------------------------------------
# Fonctions utilitaires
# --------------------------------------------------------------
def save_log(etudiant, groupe, step, problem_id, role, content):
    log_file = "logs.csv"
    file_exists = os.path.isfile(log_file)
    with open(log_file, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["timestamp", "etudiant", "groupe", "step", "problem_id", "role", "content"])
        writer.writerow([datetime.datetime.now().isoformat(), etudiant, groupe, step, problem_id, role, content])


def save_reponse_apprentissage(etudiant, groupe, module_index, exercice_id, reponse):
    fichier = "reponses_apprentissage.csv"
    file_exists = os.path.isfile(fichier)
    with open(fichier, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["timestamp", "etudiant", "groupe", "module", "exercice_id", "reponse"])
        writer.writerow([
            datetime.datetime.now().isoformat(),
            etudiant,
            groupe,
            module_index,
            exercice_id,
            reponse
        ])


def load_questions_from_json(filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir, filename)
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data["questions"]
    except FileNotFoundError:
        st.error(f"❌ Fichier {filepath} introuvable. Utilisation de questions par défaut.")
        return [
            {"id": 1, "texte": "Quelle est la différence entre une classe et un objet ?", "type": "texte"},
            {"id": 2, "texte": "Écrire une méthode qui retourne la somme de deux entiers.", "type": "code"}
        ]
    except Exception as e:
        st.error(f"❌ Erreur de chargement du fichier JSON : {e}")
        return []


# Chargement automatique des trois jeux de questions
if not st.session_state.pretest_questions:
    st.session_state.pretest_questions = load_questions_from_json("pretest.json")
if not st.session_state.posttest_questions:
    st.session_state.posttest_questions = load_questions_from_json("posttest.json")
if not st.session_state.transfert_questions:
    st.session_state.transfert_questions = load_questions_from_json("transfert.json")

# --------------------------------------------------------------
# STYLES CSS PERSONNALISÉS
# --------------------------------------------------------------
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1E3A8A;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #4B5563;
        margin-bottom: 2rem;
    }
    .card {
        background-color: #FFFFFF;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        margin-bottom: 2rem;
    }
    .btn-primary {
        background-color: #1E3A8A;
        color: white;
        padding: 0.6rem 2rem;
        border-radius: 8px;
        border: none;
        font-weight: 600;
        width: 100%;
        transition: 0.3s;
    }
    .btn-primary:hover {
        background-color: #1E40AF;
        box-shadow: 0 4px 8px rgba(30,58,138,0.3);
    }
    .logo-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 1.5rem;
    }

    /* ===== STYLES CHAT ===== */
    .chat-container {
        background-color: #f0f2f5;
        border-radius: 12px;
        padding: 16px;
        height: 350px;
        overflow-y: auto;
        margin-bottom: 10px;
        border: 1px solid #d0d0d0;
    }
    .chat-container-tn {
        height: 280px;
    }
    .message-system {
        background-color: #e8f0fe;
        color: #1a1a1a;
        border-radius: 12px;
        padding: 12px 16px;
        margin: 10px 0;
        border-left: 4px solid #0084ff;
        width: 100%;
        clear: both;
        font-size: 0.95rem;
    }
    .message-system strong {
        color: #1a3a6a;
        font-size: 1.1rem;
    }
    .message-user {
        background-color: #0084ff;
        color: white;
        border-radius: 18px 18px 4px 18px;
        padding: 8px 14px;
        margin: 6px 0 6px auto;
        max-width: 80%;
        float: right;
        clear: both;
        box-shadow: 0 1px 2px rgba(0,0,0,0.1);
        word-wrap: break-word;
        white-space: pre-wrap;
    }
    .message-assistant {
        background-color: white;
        color: #1a1a1a;
        border-radius: 18px 18px 18px 4px;
        padding: 8px 14px;
        margin: 6px auto 6px 0;
        max-width: 80%;
        float: left;
        clear: both;
        box-shadow: 0 1px 2px rgba(0,0,0,0.1);
        word-wrap: break-word;
        white-space: pre-wrap;
    }
    .badge-tn {
        background-color: #ff6b6b;
        color: white;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: bold;
        display: inline-block;
        margin-bottom: 8px;
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-6px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .message-user, .message-assistant, .message-system {
        animation: fadeIn 0.25s ease-out;
    }
    .chat-container::after {
        content: "";
        display: table;
        clear: both;
    }
    .tn-container {
        display: flex;
        gap: 20px;
        margin-top: 10px;
    }
    .tn-chat {
        flex: 1;
        background-color: #f8f9fa;
        border-radius: 12px;
        padding: 12px;
    }
    .tn-response {
        flex: 1;
        background-color: #ffffff;
        border-radius: 12px;
        padding: 12px;
        border: 2px solid #e8e8e8;
    }
    .stTextArea textarea {
        font-family: 'Courier New', monospace;
        font-size: 14px;
    }

    /* ================================================================
       PAGE D'ACCUEIL — thème "éditeur de code Java"
       ================================================================ */
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700;800&family=Source+Sans+3:wght@400;500;600;700&display=swap');

    :root{
        --ink: #1B2321;
        --ink-2: #142019;
        --paper: #F7F5EF;
        --green: #3F8C4B;
        --green-dark: #2E6B39;
        --amber: #E3A23C;
        --slate: #5B6B66;
        --code-str: #7FB2D9;
        --code-com: #8FB08A;
        --code-fg: #DCE6DC;
        --line: #E4E0D4;
    }

    html, body, [data-testid="stAppViewContainer"], .main {
        background-color: var(--paper) !important;
        font-family: 'Source Sans 3', sans-serif;
    }
    [data-testid="stHeader"] { background: transparent; }

    .teluq-topbar{
        display: flex;
        align-items: center;
        gap: .6rem;
        font-family: 'JetBrains Mono', monospace;
        font-size: .8rem;
        letter-spacing: .06em;
        text-transform: uppercase;
        color: var(--slate);
        margin-bottom: 1.4rem;
    }
    .teluq-topbar b{ color: var(--green-dark); }
    .teluq-topbar::before{
        content: "";
        width: 8px; height: 8px; border-radius: 2px;
        background: var(--green);
        display: inline-block;
    }

    .editor-card{
        background: var(--ink);
        border-radius: 14px;
        box-shadow: 0 20px 45px rgba(27,35,33,0.28);
        overflow: hidden;
        margin-bottom: 1.8rem;
    }
    .editor-titlebar{
        display: flex;
        align-items: center;
        gap: .55rem;
        padding: .65rem 1rem;
        background: var(--ink-2);
        border-bottom: 1px solid rgba(255,255,255,0.06);
    }
    .editor-dot{ width: 10px; height: 10px; border-radius: 50%; }
    .editor-dot.r{ background: #E5605A; }
    .editor-dot.y{ background: #E8B23D; }
    .editor-dot.g{ background: #59B36B; }
    .editor-filename{
        margin-left: .5rem;
        font-family: 'JetBrains Mono', monospace;
        font-size: .78rem;
        color: #9BAFA6;
    }
    .editor-body{
        padding: 1.4rem 1.5rem 1.6rem 0;
        font-family: 'JetBrains Mono', monospace;
        font-size: .92rem;
        line-height: 1.65;
    }
    .code-line{ display: flex; }
    .code-line .ln{
        width: 2.4rem;
        flex-shrink: 0;
        text-align: right;
        margin-right: 1rem;
        color: #4B5B54;
        user-select: none;
    }
    .code-line .code{ color: var(--code-fg); white-space: pre; }
    .code-line .kw{ color: var(--amber); }
    .code-line .str{ color: var(--code-str); }
    .code-line .com{ color: var(--code-com); }
    .cursor{
        display: inline-block;
        width: 8px; height: 1.05em;
        background: var(--amber);
        margin-left: 2px;
        vertical-align: text-bottom;
        animation: blink 1.1s steps(1) infinite;
    }
    @keyframes blink{ 50% { opacity: 0; } }

    .hero-title{
        font-family: 'JetBrains Mono', monospace;
        font-weight: 800;
        font-size: 2.1rem;
        color: var(--ink);
        margin: 0 0 .3rem 0;
        letter-spacing: -0.02em;
    }
    .hero-title span{ color: var(--green-dark); }
    .hero-sub{
        font-size: 1.05rem;
        color: var(--slate);
        margin-bottom: 1.6rem;
        max-width: 34rem;
    }

    .feature-row{
        display: flex;
        gap: .9rem;
        padding: .85rem 0;
        border-bottom: 1px solid var(--line);
    }
    .feature-row:last-of-type{ border-bottom: none; }
    .feature-mark{
        flex-shrink: 0;
        width: 10px; height: 10px;
        margin-top: .35rem;
        background: var(--green);
        border-radius: 2px;
    }
    .feature-title{
        font-weight: 700;
        color: var(--ink);
        font-size: .98rem;
    }
    .feature-desc{
        color: var(--slate);
        font-size: .9rem;
    }

    .security-note{
        display: flex;
        align-items: center;
        gap: .5rem;
        font-family: 'JetBrains Mono', monospace;
        font-size: .78rem;
        color: var(--slate);
        margin-top: 1.5rem;
    }

    .eyebrow{
        font-family: 'JetBrains Mono', monospace;
        font-size: .78rem;
        letter-spacing: .05em;
        color: var(--green-dark);
        text-transform: uppercase;
        margin: 1.1rem 0 .4rem 0;
    }
    .eyebrow.first{ margin-top: 0; }

    [data-testid="stForm"] [data-testid="stTextInput"] input,
    [data-testid="stForm"] [data-testid="stNumberInput"] input{
        border-radius: 8px;
    }
    [data-testid="stFormSubmitButton"] button{
        border-radius: 8px;
        font-weight: 600;
    }
    .assistant-option .stMarkdown p{ margin-bottom: .2rem; }
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------------------
# PAGE ACCUEIL + INSCRIPTION
# --------------------------------------------------------------
if st.session_state.etape == 'accueil':
    col_left, col_right = st.columns([1, 1], gap="large")

    with col_left:
        st.markdown("""
        <div class="teluq-topbar">Université <b>TÉLUQ</b> — Recherche en apprentissage</div>
        """, unsafe_allow_html=True)

        # FIX: `except:` nu remplacé par une exception précise, plus sûr
        # et plus facile à déboguer si jamais autre chose échoue.
        try:
            st.image("images/teluq.png", width=110)
        except FileNotFoundError:
            pass

        # Signature visuelle : fenêtre d'éditeur de code, cohérente avec le
        # sujet (apprentissage de Java) plutôt qu'un visuel générique.
        st.markdown("""
        <div class="editor-card">
            <div class="editor-titlebar">
                <span class="editor-dot r"></span>
                <span class="editor-dot y"></span>
                <span class="editor-dot g"></span>
                <span class="editor-filename">Apprentissage.java</span>
            </div>
            <div class="editor-body">
                <div class="code-line"><span class="ln">1</span><span class="code"><span class="kw">public class</span> Apprentissage {</span></div>
                <div class="code-line"><span class="ln">2</span><span class="code"></span></div>
                <div class="code-line"><span class="ln">3</span><span class="code">  <span class="com">// pré-test → modules → post-test → transfert</span></span></div>
                <div class="code-line"><span class="ln">4</span><span class="code">  <span class="com">// assistant IA : réactif ou structurant</span></span></div>
                <div class="code-line"><span class="ln">5</span><span class="code"></span></div>
                <div class="code-line"><span class="ln">6</span><span class="code">  <span class="kw">public static void</span> main(String[] args) {</span></div>
                <div class="code-line"><span class="ln">7</span><span class="code">    etudiant.commencer(<span class="str">"Java"</span>);</span></div>
                <div class="code-line"><span class="ln">8</span><span class="code">  }</span></div>
                <div class="code-line"><span class="ln">9</span><span class="code">}<span class="cursor"></span></span></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="hero-title">Apprentissage <span>Java</span></div>', unsafe_allow_html=True)
        st.markdown('<div class="hero-sub">Une plateforme de recherche qui adapte l’accompagnement IA à ta façon d’apprendre le Java.</div>', unsafe_allow_html=True)

        st.markdown("""
        <div class="feature-row">
            <div class="feature-mark"></div>
            <div><div class="feature-title">Évaluation en trois temps</div>
            <div class="feature-desc">Pré-test, post-test et test de transfert pour mesurer ta progression.</div></div>
        </div>
        <div class="feature-row">
            <div class="feature-mark"></div>
            <div><div class="feature-title">Assistant adaptatif</div>
            <div class="feature-desc">Style réactif ou structurant, selon ta façon d'apprendre.</div></div>
        </div>
        <div class="feature-row">
            <div class="feature-mark"></div>
            <div><div class="feature-title">Parcours modulaire</div>
            <div class="feature-desc">Exercices interactifs et travaux notés, module après module.</div></div>
        </div>
        <div class="feature-row">
            <div class="feature-mark"></div>
            <div><div class="feature-title">Suivi continu</div>
            <div class="feature-desc">Tes échanges sont enregistrés pour un accompagnement personnalisé.</div></div>
        </div>
        <div class="security-note">🔒 Données anonymisées et sécurisées</div>
        """, unsafe_allow_html=True)

    with col_right:
        with st.container(border=True):
            st.markdown('<div class="eyebrow first">// inscription</div>', unsafe_allow_html=True)
            st.markdown("### Commence l'étude")
            st.caption("Remplis les champs ci-dessous pour démarrer ta session.")

            with st.form(key="inscription_form"):
                st.markdown('<div class="eyebrow first">01 — Identité</div>', unsafe_allow_html=True)
                nom = st.text_input("Ton nom ou identifiant", value=st.session_state.nom_etudiant)

                col_age, col_niveau = st.columns(2)
                with col_age:
                    age = st.number_input("Âge", min_value=16, max_value=100, step=1, value=st.session_state.age)
                with col_niveau:
                    niveaux_options = ["Lycée", "Licence 1", "Licence 2", "Licence 3", "Master", "Doctorat", "Autre"]
                    niveau = st.selectbox(
                        "Niveau d'études",
                        niveaux_options,
                        index=niveaux_options.index(st.session_state.niveau_etudes) if st.session_state.niveau_etudes in niveaux_options else 0
                    )

                exp_options = ["Non, jamais", "Oui, un peu", "Oui, plusieurs années"]
                exp = st.radio(
                    "Expérience en programmation",
                    exp_options,
                    index=exp_options.index(st.session_state.experience_prog)
                )

                st.markdown('<div class="eyebrow">02 — Style d\'apprentissage</div>', unsafe_allow_html=True)
                col_btn1, col_btn2 = st.columns(2)
                with col_btn1:
                    with st.container(border=True):
                        st.markdown("**🤖 Assistant Réactif**")
                        st.caption("Répond directement à tes questions, à la demande.")
                        submit_reactif = st.form_submit_button("Choisir cet assistant", use_container_width=True)
                with col_btn2:
                    with st.container(border=True):
                        st.markdown("**🧑‍🏫 Tuteur Structurant**")
                        st.caption("Te guide pas à pas vers la solution, sans te la donner.")
                        submit_structurant = st.form_submit_button("Choisir ce tuteur", use_container_width=True)

                if submit_reactif or submit_structurant:
                    # FIX: on vérifie qu'un nom a bien été saisi avant de continuer,
                    # sinon les logs plus loin seraient associés à un étudiant vide.
                    if not nom.strip():
                        st.warning("⚠️ Merci d'indiquer ton nom ou identifiant avant de continuer.")
                    else:
                        st.session_state.nom_etudiant = nom
                        st.session_state.age = age
                        st.session_state.niveau_etudes = niveau
                        st.session_state.experience_prog = exp
                        st.session_state.groupe = 'A' if submit_reactif else 'B'
                        st.session_state.etape = 'pretest'
                        st.rerun()

            st.caption("⚠️ Le choix de l'assistant détermine le style d'interaction pour toute la session.")

# --------------------------------------------------------------
# PRÉ-TEST
# --------------------------------------------------------------
elif st.session_state.etape == 'pretest':
    st.header("📋 Pré-test (15 minutes)")
    st.write("Répondez sans aide extérieure.")

    if st.session_state.pretest_start is None:
        st.session_state.pretest_start = time.time()

    elapsed = time.time() - st.session_state.pretest_start
    remaining = max(0, 15 * 60 - elapsed)
    st.sidebar.write(f"⏱️ Temps restant : {int(remaining//60)} min {int(remaining%60)} s")
    if remaining <= 0:
        st.warning("⏰ Le temps est écoulé ! Vous pouvez encore soumettre vos réponses, mais elles seront marquées comme hors délai.")

    questions = st.session_state.pretest_questions
    if not questions:
        st.error("❌ Aucune question chargée. Vérifie le fichier pretest.json à la racine.")
        if st.button("Retour à l'accueil"):
            st.session_state.etape = 'accueil'
            st.rerun()
        st.stop()

    answers = {}
    for q in questions:
        st.subheader(f"Question {q['id']}")
        st.write(q["texte"])
        if q["type"] == "qcm":
            options = q.get("options", [])
            if not options:
                st.warning("Cette question QCM n'a pas d'options.")
                rep = st.text_input("Entrez votre réponse (texte libre) :", key=f"pretest_{q['id']}")
            else:
                rep = st.radio(
                    "Choisis une réponse :",
                    options,
                    key=f"pretest_{q['id']}",
                    index=None
                )
        elif q["type"] == "code":
            rep = st.text_area("Écris ton code :", key=f"pretest_{q['id']}", height=150)
        else:
            rep = st.text_input("Votre réponse :", key=f"pretest_{q['id']}")
        answers[q['id']] = rep

    if st.button("Soumettre le pré-test"):
        if remaining <= 0:
            st.warning("⏰ Temps dépassé ! Tes réponses sont tout de même enregistrées.")
        st.session_state.pretest_answers = answers
        save_log(st.session_state.nom_etudiant, st.session_state.groupe, "pretest", "", "user", str(answers))
        st.session_state.pretest_start = None
        st.session_state.etape = 'apprentissage'
        st.rerun()

# --------------------------------------------------------------
# APPRENTISSAGE - PAGE DE SÉLECTION + MODULES
# --------------------------------------------------------------
elif st.session_state.etape == 'apprentissage':
    if not st.session_state.nom_etudiant:
        st.warning("Veuillez entrer ton nom.")
        if st.button("Retour"):
            st.session_state.etape = 'accueil'
            st.rerun()
        st.stop()

    # Si on est sur la page de sélection des modules
    if st.session_state.page_apprentissage == 'selection':
        st.header("📚 Choisis un module")
        st.markdown("Sélectionne un module pour commencer l'apprentissage. Les modules sont verrouillés : tu dois terminer le précédent pour débloquer le suivant.")
        st.markdown("---")

        cols = st.columns(2)
        for i, module in enumerate(MODULES):
            with cols[i % 2]:
                progression = st.session_state.progression_modules[i]
                if i == 0:
                    unlocked = True
                else:
                    unlocked = st.session_state.progression_modules[i - 1]['termine']

                if progression['termine']:
                    status = "✅ Terminé"
                    status_color = "#4CAF50"
                elif progression['dernier_item'] > 0:
                    status = "🔄 En cours"
                    status_color = "#FF9800"
                else:
                    status = "🔒 Non commencé"
                    status_color = "#9E9E9E"

                nb_exercices = len(module['exercices'])
                nb_questions = nb_exercices + 1

                if not unlocked:
                    st.markdown(f"""
                    <div style="
                        background-color: #f0f0f0;
                        padding: 20px;
                        border-radius: 12px;
                        border: 2px solid #d0d0d0;
                        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                        margin-bottom: 15px;
                        text-align: center;
                        opacity: 0.6;
                    ">
                        <h3 style="margin: 0; color: #1E3A8A;">{module['titre']}</h3>
                        <p style="color: #666; margin: 10px 0;">
                            {nb_questions} questions
                        </p>
                        <p style="color: {status_color}; font-weight: bold; margin: 5px 0;">
                            {status}
                        </p>
                        <p style="color: #999; font-size: 0.9em;">🔒 Complétez le module précédent</p>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div style="
                        background-color: white;
                        padding: 20px;
                        border-radius: 12px;
                        border: 2px solid {status_color};
                        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                        margin-bottom: 15px;
                        text-align: center;
                    ">
                        <h3 style="margin: 0; color: #1E3A8A;">{module['titre']}</h3>
                        <p style="color: #666; margin: 10px 0;">
                            {nb_questions} questions
                        </p>
                        <p style="color: {status_color}; font-weight: bold; margin: 5px 0;">
                            {status}
                        </p>
                    </div>
                    """, unsafe_allow_html=True)
                    if st.button(f"📖 Accéder au module {i+1}", key=f"module_btn_{i}"):
                        st.session_state.module_index = i
                        st.session_state.item_index = st.session_state.progression_modules[i]['dernier_item']
                        st.session_state.messages_module = []
                        st.session_state.page_apprentissage = 'module'
                        st.rerun()

        st.markdown("---")
        modules_termines = sum(1 for p in st.session_state.progression_modules.values() if p['termine'])
        st.info(f"📊 Progression : {modules_termines}/{len(MODULES)} modules terminés")

        if modules_termines == len(MODULES):
            st.success("🎉 Félicitations, vous avez terminé tous les modules !")
            if st.button("📝 Passer au post-test", use_container_width=True):
                st.session_state.etape = 'posttest'
                st.session_state.messages = []
                st.session_state.current_problem_index = 0
                st.rerun()

        st.markdown("---")
        col_nav1, col_nav2, col_nav3 = st.columns([1, 1, 2])
        with col_nav1:
            if st.session_state.module_index > 0:
                if st.button("⬅️ Module précédent"):
                    st.session_state.module_index -= 1
                    st.session_state.item_index = st.session_state.progression_modules[st.session_state.module_index]['dernier_item']
                    st.session_state.messages_module = []
                    st.session_state.page_apprentissage = 'module'
                    st.rerun()
            else:
                st.button("⬅️ Module précédent", disabled=True)
        with col_nav2:
            if st.session_state.module_index < len(MODULES) - 1:
                next_unlocked = st.session_state.progression_modules[st.session_state.module_index]['termine']
                if next_unlocked:
                    if st.button("Module suivant ➡️"):
                        st.session_state.module_index += 1
                        st.session_state.item_index = st.session_state.progression_modules[st.session_state.module_index]['dernier_item']
                        st.session_state.messages_module = []
                        st.session_state.page_apprentissage = 'module'
                        st.rerun()
                else:
                    st.button("Module suivant ➡️", disabled=True, help="Terminez le module actuel pour débloquer le suivant")
            else:
                st.button("Module suivant ➡️", disabled=True)
        with col_nav3:
            if st.button("🏁 Quitter l'apprentissage"):
                st.session_state.etape = 'posttest'
                st.session_state.messages = []
                st.session_state.current_problem_index = 0
                st.rerun()

    else:
        # Mode : affichage d'un module spécifique
        module = MODULES[st.session_state.module_index]
        total_exercices = len(module['exercices'])
        total_items = total_exercices + 2  # introduction + exercices + travail noté
        item = st.session_state.item_index

        st.sidebar.write(f"👤 {st.session_state.nom_etudiant} | Groupe {'A (Réactif)' if st.session_state.groupe=='A' else 'B (Structurant)'}")
        st.header(f"📘 {module['titre']}")
        st.markdown("---")

        if item == 0:
            st.subheader("📖 Introduction")
            st.markdown(module['introduction'])
            st.info("👉 Passe à l'exercice suivant pour commencer.")
            st.markdown("📚 **Référence cours** : [Lien vers le cours](https://lemire.github.io/inf1220-hugo/)")

        else:
            if item <= total_exercices:
                exercice = module['exercices'][item - 1]
                item_id = exercice['id']
                question = exercice['question']
                label = f"Exercice {item_id}"
            else:
                tn = module['travail_note']
                item_id = tn['id']
                question = tn['question']
                label = f"Travail noté : {item_id}"

            st.markdown(f"""
            <div class="message-system">
                <strong>✏️ {label}</strong><br>
                {question}
            </div>
            """, unsafe_allow_html=True)

            col_gauche, col_droite = st.columns(2)

            with col_gauche:
                st.markdown("#### 💬 Assistant (aide, explications)")

                # FIX: st.chat_input s'accroche TOUJOURS en bas de la page
                # entière, jamais à l'intérieur d'une colonne ou d'un div —
                # c'est pour ça que le champ de saisie apparaissait en
                # dehors du cadre gris. On utilise maintenant un
                # st.container(border=True, height=...) qui contient à la
                # fois l'historique des messages ET un formulaire classique
                # (text_input + bouton), le tout reste donc visuellement
                # dans le même cadre.
                with st.container(height=420, border=True):
                    for msg in st.session_state.messages_module:
                        if msg["role"] == "user":
                            st.markdown(f'<div class="message-user">👤 {msg["content"]}</div>', unsafe_allow_html=True)
                        else:
                            st.markdown(f'<div class="message-assistant">🤖 {msg["content"]}</div>', unsafe_allow_html=True)

                    with st.form(key=f"chat_form_{item_id}", clear_on_submit=True, border=False):
                        col_input, col_send = st.columns([5, 1])
                        with col_input:
                            user_input = st.text_input(
                                "Ta question",
                                key=f"chat_input_{item_id}",
                                placeholder="💬 Pose une question à l'assistant...",
                                label_visibility="collapsed"
                            )
                        with col_send:
                            envoyer = st.form_submit_button("Envoyer")

                if envoyer and user_input.strip():
                    st.session_state.messages_module.append({"role": "user", "content": user_input})
                    save_log(st.session_state.nom_etudiant, st.session_state.groupe, "apprentissage", item_id, "user", user_input)
                    system_content = (
                        REACTIVE_PROMPT.format(problem_statement=question)
                        if st.session_state.groupe == 'A'
                        else TUTOR_PROMPT.format(problem_statement=question)
                    )
                    with st.spinner("L'assistant réfléchit..."):
                        try:
                            # FIX: on réutilise le client global au lieu d'en
                            # recréer un à chaque appel, et on utilise le
                            # modèle Gemini (MODEL) au lieu de "gpt-3.5-turbo",
                            # qui n'existe pas sur ce endpoint Gemini et
                            # aurait fait échouer chaque requête.
                            response = client.chat.completions.create(
                                model=MODEL,
                                messages=[
                                    {"role": "system", "content": system_content},
                                    {"role": "user", "content": user_input}
                                ],
                                temperature=0.3,
                                max_tokens=1000
                            )
                            assistant_reply = response.choices[0].message.content
                            st.session_state.messages_module.append({"role": "assistant", "content": assistant_reply})
                            save_log(st.session_state.nom_etudiant, st.session_state.groupe, "apprentissage", item_id, "assistant", assistant_reply)
                        except Exception as e:
                            error_msg = f"Erreur technique : {str(e)}"
                            st.error(error_msg)
                            st.session_state.messages_module.append({"role": "assistant", "content": error_msg})
                    st.rerun()

            with col_droite:
                st.markdown("#### ✍️ Ta réponse")
                key_reponse = f"reponse_{item_id}"
                if key_reponse not in st.session_state:
                    st.session_state[key_reponse] = ""

                # FIX: c'était ici l'erreur de syntaxe qui faisait planter
                # toute l'application (virgule manquante avant
                # label_visibility). Corrigé ci-dessous.
                # FIX: le label ne doit pas être une chaîne vide ("") même
                # avec label_visibility="collapsed", sinon Streamlit
                # affiche un avertissement d'accessibilité dans le terminal.
                # On donne donc un vrai label, simplement masqué à l'écran.
                reponse = st.text_area(
                    "Ta réponse",
                    value=st.session_state[key_reponse],
                    height=350,
                    key=f"textarea_{item_id}",
                    placeholder="Écris ta solution ici (pseudocode, code Java, explications...)",
                    label_visibility="collapsed"
                )
                st.session_state[key_reponse] = reponse

                col_soumettre, col_statut = st.columns([1, 2])
                with col_soumettre:
                    if st.button("📤 Soumettre ma réponse", key=f"submit_{item_id}"):
                        if reponse.strip():
                            # FIX: on utilise désormais save_reponse_apprentissage,
                            # qui écrit dans un fichier dédié
                            # (reponses_apprentissage.csv) avec les bonnes
                            # colonnes (module, exercice_id, réponse), au lieu
                            # de save_log qui mélangeait tout dans logs.csv
                            # et pour lequel cette fonction avait été écrite
                            # sans jamais être appelée.
                            save_reponse_apprentissage(
                                st.session_state.nom_etudiant,
                                st.session_state.groupe,
                                st.session_state.module_index,
                                item_id,
                                reponse
                            )
                            st.success("✅ Réponse soumise avec succès !")
                        else:
                            st.warning("⚠️ Veuillez écrire une réponse avant de soumettre.")
                with col_statut:
                    if st.session_state[key_reponse].strip():
                        st.info("📌 Réponse enregistrée localement")

        # Navigation (à l'intérieur du module)
        st.markdown("---")
        col1, col2, col3 = st.columns([1, 1, 2])
        with col1:
            if item > 0:
                if st.button("⬅️ Précédent"):
                    st.session_state.item_index -= 1
                    st.session_state.messages_module = []
                    st.rerun()
            else:
                st.button("⬅️ Précédent", disabled=True)
        with col2:
            if item < total_items - 1:
                if st.button("Suivant ➡️"):
                    st.session_state.item_index += 1
                    # FIX: on garde une trace du dernier item consulté pour
                    # que le badge "🔄 En cours" et la reprise du module
                    # fonctionnent correctement.
                    st.session_state.progression_modules[st.session_state.module_index]['dernier_item'] = st.session_state.item_index
                    st.session_state.messages_module = []
                    st.rerun()
            else:
                if st.session_state.module_index < len(MODULES) - 1:
                    if st.button("Module suivant ➡️"):
                        st.session_state.progression_modules[st.session_state.module_index]['termine'] = True
                        st.session_state.module_index += 1
                        st.session_state.item_index = 0
                        st.session_state.messages_module = []
                        st.rerun()
                else:
                    if st.button("✅ Terminer l'apprentissage"):
                        st.session_state.progression_modules[st.session_state.module_index]['termine'] = True
                        st.session_state.etape = 'posttest'
                        st.session_state.messages = []
                        st.session_state.current_problem_index = 0
                        st.rerun()
        with col3:
            if st.button("🏁 Quitter l'apprentissage"):
                st.session_state.etape = 'posttest'
                st.session_state.messages = []
                st.session_state.current_problem_index = 0
                st.rerun()

# --------------------------------------------------------------
# POST-TEST
# --------------------------------------------------------------
elif st.session_state.etape == 'posttest':
    st.header("📝 Post-test (15 minutes)")
    st.write("Répondez sans aide.")

    if st.session_state.posttest_start is None:
        st.session_state.posttest_start = time.time()

    elapsed = time.time() - st.session_state.posttest_start
    remaining = max(0, 15 * 60 - elapsed)
    st.sidebar.write(f"⏱️ Temps restant : {int(remaining//60)} min {int(remaining%60)} s")
    if remaining <= 0:
        st.warning("⏰ Le temps est écoulé ! Vous pouvez encore soumettre vos réponses, mais elles seront marquées comme hors délai.")

    questions = st.session_state.posttest_questions
    if not questions:
        st.error("❌ Aucune question chargée. Vérifie le fichier posttest.json à la racine.")
        if st.button("Retour à l'accueil"):
            st.session_state.etape = 'accueil'
            st.rerun()
        st.stop()

    answers = {}
    for q in questions:
        st.subheader(f"Question {q['id']}")
        st.write(q["texte"])
        if q["type"] == "qcm":
            options = q.get("options", [])
            if not options:
                st.warning("Cette question QCM n'a pas d'options.")
                rep = st.text_input("Entrez votre réponse (texte libre) :", key=f"posttest_{q['id']}")
            else:
                rep = st.radio(
                    "Choisis une réponse :",
                    options,
                    key=f"posttest_{q['id']}",
                    index=None
                )
        elif q["type"] == "code":
            rep = st.text_area("Écris ton code :", key=f"posttest_{q['id']}", height=150)
        else:
            rep = st.text_input("Votre réponse :", key=f"posttest_{q['id']}")
        answers[q['id']] = rep

    if st.button("Soumettre le post-test"):
        if remaining <= 0:
            st.warning("⏰ Temps dépassé ! Tes réponses sont tout de même enregistrées.")
        st.session_state.posttest_answers = answers
        save_log(st.session_state.nom_etudiant, st.session_state.groupe, "posttest", "", "user", str(answers))
        st.session_state.posttest_start = None
        st.session_state.etape = 'transfert'
        st.rerun()

# --------------------------------------------------------------
# TRANSFERT (chargé depuis transfert.json)
# --------------------------------------------------------------
elif st.session_state.etape == 'transfert':
    st.header("📚 Examen de transfert (60 minutes, sans IA)")
    st.write("Résolvez ces nouveaux problèmes par vous-mêmes.")

    if st.session_state.transfert_start is None:
        st.session_state.transfert_start = time.time()

    elapsed = time.time() - st.session_state.transfert_start
    remaining = max(0, 60 * 60 - elapsed)
    st.sidebar.write(f"⏱️ Temps restant : {int(remaining//60)} min {int(remaining%60)} s")
    if remaining <= 0:
        st.warning("⏰ Le temps est écoulé ! Vous pouvez encore soumettre vos réponses, mais elles seront marquées comme hors délai.")

    questions = st.session_state.transfert_questions
    if not questions:
        st.error("❌ Aucune question chargée. Vérifie le fichier transfert.json à la racine.")
        if st.button("Retour à l'accueil"):
            st.session_state.etape = 'accueil'
            st.rerun()
        st.stop()

    answers = {}
    for q in questions:
        st.subheader(f"Problème {q['id']}")
        st.write(q["texte"])
        rep = st.text_area("Votre solution", key=f"transfert_{q['id']}", height=200)
        answers[q['id']] = rep

    if st.button("Soumettre l'examen"):
        if remaining <= 0:
            st.warning("⏰ Temps dépassé ! Tes réponses sont tout de même enregistrées.")
        st.session_state.transfert_answers = answers
        save_log(st.session_state.nom_etudiant, st.session_state.groupe, "transfert", "", "user", str(answers))
        st.session_state.transfert_start = None
        st.session_state.etape = 'finished'
        st.rerun()

# --------------------------------------------------------------
# FIN
# --------------------------------------------------------------
elif st.session_state.etape == 'finished':

    def stats_test(answers, total_q):
        """Retourne (répondues, vides) pour un test donné.
        Note : sans clé de correction dans les fichiers JSON, on ne peut
        distinguer que répondu / laissé vide — pas correct / incorrect."""
        if not total_q:
            return 0, 0
        repondues = sum(1 for v in (answers or {}).values() if str(v).strip())
        return repondues, max(0, total_q - repondues)

    nb_pretest_q = len(st.session_state.pretest_questions)
    nb_posttest_q = len(st.session_state.posttest_questions)
    nb_transfert_q = len(st.session_state.transfert_questions)

    rep_pre, vide_pre = stats_test(st.session_state.pretest_answers, nb_pretest_q)
    rep_post, vide_post = stats_test(st.session_state.posttest_answers, nb_posttest_q)
    rep_trans, vide_trans = stats_test(st.session_state.transfert_answers, nb_transfert_q)
    total_repondues = rep_pre + rep_post + rep_trans
    total_vides = vide_pre + vide_post + vide_trans

    st.markdown("""
    <style>
        .term-card{
            background: var(--ink);
            border-radius: 14px;
            box-shadow: 0 20px 45px rgba(27,35,33,0.28);
            overflow: hidden;
            max-width: 640px;
            margin: 1.5rem 0 2rem 0;
        }
        .term-titlebar{
            display:flex; align-items:center; gap:.55rem;
            padding:.65rem 1rem;
            background: var(--ink-2);
            border-bottom: 1px solid rgba(255,255,255,0.06);
        }
        .term-filename{
            margin-left:.5rem; font-family:'JetBrains Mono',monospace;
            font-size:.78rem; color:#9BAFA6;
        }
        .term-body{
            padding: 1.3rem 1.5rem 1.5rem 1.5rem;
            font-family:'JetBrains Mono',monospace;
            font-size:.88rem; line-height:1.9;
            color: var(--code-fg);
        }
        .term-row{ display:flex; justify-content:space-between; gap:1rem; }
        .term-label{ color:#9BAFA6; }
        .term-dots{ flex:1; overflow:hidden; white-space:nowrap; color:#3A4A43; margin: 0 .4rem; }
        .term-ok{ color: var(--green); font-weight:700; }
        .term-warn{ color: var(--amber); font-weight:700; }
        .term-final{
            margin-top:.9rem; padding-top:.9rem;
            border-top:1px dashed rgba(255,255,255,0.12);
            color: var(--green); font-weight:700;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="teluq-topbar">Université <b>TÉLUQ</b> — Recherche en apprentissage</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-title">Session <span>terminée</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-sub">Merci d\'avoir complété toutes les étapes de l\'étude. Voici le récapitulatif de ta session.</div>', unsafe_allow_html=True)

    def ligne(label, valeur, cls=""):
        return f'<div class="term-row"><span class="term-label">{label}</span><span class="term-dots"></span><span class="{cls}">{valeur}</span></div>'

    st.markdown(f"""
    <div class="term-card">
        <div class="term-titlebar">
            <span class="editor-dot r"></span><span class="editor-dot y"></span><span class="editor-dot g"></span>
            <span class="term-filename">résumé --session</span>
        </div>
        <div class="term-body">
            {ligne("Étudiant", st.session_state.nom_etudiant)}
            {ligne("Assistant", "Réactif" if st.session_state.groupe == 'A' else "Structurant")}
            {ligne("Pré-test", f"{rep_pre}/{nb_pretest_q} répondues" + (f" · {vide_pre} vide(s)" if vide_pre else ""), "term-ok" if vide_pre == 0 else "term-warn")}
            {ligne("Post-test", f"{rep_post}/{nb_posttest_q} répondues" + (f" · {vide_post} vide(s)" if vide_post else ""), "term-ok" if vide_post == 0 else "term-warn")}
            {ligne("Transfert", f"{rep_trans}/{nb_transfert_q} répondues" + (f" · {vide_trans} vide(s)" if vide_trans else ""), "term-ok" if vide_trans == 0 else "term-warn")}
            <div class="term-final">✔ {total_repondues} question(s) répondue(s){f" · {total_vides} laissée(s) vide(s)" if total_vides else ""}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.caption(
        "ℹ️ Ce récapitulatif indique si une réponse a été fournie ou laissée vide. "
        "L'exactitude des réponses sera évaluée séparément par l'équipe de recherche."
    )

    if st.button("🔄 Recommencer l'expérience", key="restart"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

    st.balloons()