# modules.py

MODULES = [

    {
        "id": 1,
        "titre": "Module 1 : Héritage et polymorphisme",
        "introduction": """
        Module 1 : héritage, redéfinition, polymorphisme.  
        Nous verrons comment réutiliser et étendre des classes existantes.
        """,
        "exercices":  [
            {"id": "E1.1", "question": "Écrire un algorithme (pseudocode) qui affiche 'Bonjour le monde'."},
            {"id": "E1.2", "question": "Déclarer une variable entière, l'initialiser à 10, et afficher sa valeur."},
            {"id": "E1.3", "question": "Écrire une condition if-else qui vérifie si un nombre est pair ou impair."},
            {"id": "E1.4", "question": "Calculer la somme d'un tableau d'entiers de longueur quelconque."},
            {"id": "E1.5", "question": "Rechercher un entier dans un tableau et retourner son index (ou -1 s'il est absent)."},
            {"id": "E1.6", "question": "Additionner tous les nombres naturels inférieurs à 1000 qui sont multiples de 3 ou de 5."},
            {"id": "E1.7", "question": "Trouver le plus grand nombre premier qui divise 317584931803."},
            {"id": "E1.8", "question": "Trouver le chiffre des dizaines d'un entier positif x."},
            {"id": "E1.9", "question": "Trouver l'erreur dans ce pseudocode :\n\nEntrées : Tableau R de longueur N, Valeur X\nSortie : Est-ce que X se trouve dans R ?\nVariables : i = 0\nTant que i <= N\n    Si R[i] = X Alors retourne Vrai\n    i = i + 1\nretourne Faux"},
            {"id": "E1.10", "question": "Calculer les racines réelles d'un polynôme du second degré (discriminant)."},
            {"id": "E1.11", "question": "Exécuter l'algorithme de l'exercice 10 pour P(x) = x² - 5x + 6 et présenter les résultats."},
            {"id": "E1.12", "question": "Convertir un nombre M dans une base B (2 ≤ B < 17) en utilisant la méthode des divisions successives."},
            {"id": "E1.13", "question": "Tester la parité d'un nombre M en utilisant l'algorithme de conversion en base 2."},
            {"id": "E1.14", "question": "Calculer la factorielle d'un entier positif n."},
            {"id": "E1.15", "question": "Inverser un tableau d'entiers de taille quelconque."},
            {"id": "E1.16", "question": "Compter le nombre de voyelles dans une chaîne de caractères."},
            {"id": "E1.17", "question": "Déterminer si un nombre entier est un palindrome."},
            {"id": "E1.18", "question": "Trouver le minimum et le maximum dans un tableau d'entiers."},
            {"id": "E1.19", "question": "Nombre maximal de comparaisons pour rechercher un élément dans un tableau non trié de taille n. Justifier."},
            {"id": "E1.20", "question": "Expliquer pourquoi la recherche binaire n'est applicable qu'aux tableaux triés. Quelle est sa complexité ?"},
            {"id": "E1.21", "question": "Donner un exemple d'algorithme de complexité O(n²) et expliquer."},
            {"id": "E1.22", "question": "Expliquer ce que signifie O(n log n) pour un tri fusion et pourquoi c'est plus rapide qu'un tri naïf."},
            {"id": "E1.23", "question": "Quelles étaient les motivations principales d'Alan Kay pour la POO ? Résumer brièvement."},
            {"id": "E1.24", "question": "Quelles étaient les motivations de Dahl et Nygaard pour Simula ? Influence sur la programmation moderne."},
            {"id": "E1.25", "question": "Qui est James Gosling et quel a été son rôle dans la création de Java ? Motivations derrière Java."},
            {"id": "E1.26", "question": "Citer trois domaines industriels où Java est largement utilisé et expliquer pourquoi."},
            {"id": "E1.27", "question": "Qu'est-ce que la notation de Backus-Naur (BNF) ? Donner un exemple simple."},
            {"id": "E1.28", "question": "Un ordinateur tourne à 3 GHz. Quelle distance la lumière parcourt-elle pendant un cycle ?"},
            {"id": "E1.29", "question": "Différence entre un kibioctet et un kilo-octet."},
            {"id": "E1.30", "question": "Supprimer les doublons d'un tableau trié en ordre croissant et retourner la nouvelle taille."},
            {"id": "E1.31", "question": "Calculer a^n (a entier, n positif)."},
            {"id": "E1.32", "question": "Compter le nombre d'occurrences d'un caractère spécifique dans une chaîne."},
            {"id": "E1.33", "question": "Complexité algorithmique de la recherche d'une clé dans une table de hachage."},
            {"id": "E1.34", "question": "Qu'est-ce qu'un système d'exploitation ? Décrire ses rôles principaux."},
            {"id": "E1.35", "question": "Vrai ou Faux : Le système d'exploitation gère uniquement l'interface utilisateur et ne contrôle pas les ressources matérielles."},
            {"id": "E1.36", "question": "Nommer trois systèmes d'exploitation et décrire leurs utilisations principales."},
            {"id": "E1.37", "question": "Rôle du noyau dans un système d'exploitation."},
            {"id": "E1.38", "question": "Expliquer comment le système d'exploitation permet le multitâche et le multithreading."},
            {"id": "E1.39", "question": "Que fait le processeur (CPU) dans un ordinateur ?"},
            {"id": "E1.40", "question": "Qu'est-ce qu'un processeur multi-cœurs ? Donner un exemple d'avantage."},
            {"id": "E1.41", "question": "Différence entre un processus et un thread."},
            {"id": "E1.42", "question": "Comment le système d'exploitation gère-t-il l'ordonnancement des processus ?"},
            {"id": "E1.43", "question": "Vrai ou Faux : Les threads partagent la même mémoire au sein d'un processus."},
            {"id": "E1.44", "question": "Expliquer la hiérarchie de la mémoire et pourquoi elle existe."},
            {"id": "E1.45", "question": "Différence entre RAM et mémoire cache en termes de vitesse et de volatilité."},
            {"id": "E1.46", "question": "Comparer brièvement la DRAM et la SRAM."},
            {"id": "E1.47", "question": "Que se passe-t-il lors d'une faute de page en mémoire virtuelle ?"},
            {"id": "E1.48", "question": "Qu'est-ce que la localité temporelle et spatiale, et comment le cache l'exploite-t-il ?"},
            {"id": "E1.49", "question": "Qu'est-ce que les entrées/sorties (E/S) dans un ordinateur ?"},
            {"id": "E1.50", "question": "Expliquer les deux méthodes principales de communication entre le CPU et les périphériques."}

        ],
        "travail_note": {
            "id": "TN1",
            "question": "Créer une hiérarchie de classes pour des formes géométriques (Cercle, Rectangle) avec une méthode calculerAire()."
        }
    },
    {
        "id": 2,
        "titre": "Module 2 : Interfaces et collections",
        "introduction": """
        Module 2 : nous introduisons les interfaces et les collections (List, Set, Map).  
        Vous apprendrez à manipuler des données structurées.
        """,
        "exercices": [
    {"id": "E2.1", "question": "Proposez une classe Etudiant dont le constructeur prend en paramètre un identifiant (sous la forme d'un entier) et qui comprend une méthode monIdentifiant retournant l'identifiant en question."},

    {"id": "E2.2", "question": "Combien de constructeurs est-ce qu'une classe peut avoir en Java?"},

    {"id": "E2.3", "question": "Soit la classe suivante :\n\npublic class Patate {\n  static int y;\n  public Patate(int x) {\n    y = x;\n  }\n\n  public int nombre() {\n    return y;\n  }\n}\n\nQue va afficher le code suivant ?\n\nPatate z1 = new Patate(1);\nPatate z2 = new Patate(2);\nSystem.out.println(z1.nombre());"},

    {"id": "E2.4", "question": "Écrivez une classe nommée Somme comprenant une méthode nommée additionne qui additionne deux nombres et retourne le résultat."},

    {"id": "E2.5", "question": "Expliquez pourquoi la méthode donne de cette classe va toujours retourner la valeur 2.\n\npublic class Somme {\n  public void ajoute(int a) {\n    a = a + 1;\n  }\n  public int donne() {\n    int a = 2;\n    ajoute(a);\n    return a;\n  }\n}"},

    {"id": "E2.6", "question": "Expliquez pourquoi la méthode donne de cette classe va toujours retourner la valeur 3.\n\npublic class Variable {\n  public int a = 2;\n\n  public static void ajoute(Variable x) {\n    x.a = x.a + 1;\n  }\n\n  public int donne() {\n    Variable x = new Variable();\n    ajoute(x);\n    return x.a;\n  }\n}"},

    {"id": "E2.7", "question": "Écrivez une classe Puissance qui comprend une méthode nommée deux qui prend un entier et retourne l'entier mis au carré."},

    {"id": "E2.8", "question": "Expliquez pourquoi la méthode donne de cette classe va toujours retourner la valeur 2.\n\npublic class Variable {\n  public int a = 2;\n\n  public static void ajoute(Variable x) {\n    x = new Variable();\n    x.a = x.a + 1;\n  }\n\n  public int donne() {\n    Variable x = new Variable();\n    ajoute(x);\n    return x.a;\n  }\n}"},

    {"id": "E2.9", "question": "Pourquoi le bout de code suivant va générer une erreur à la compilation ?\n\nclass T {\n  private float x;\n  private static int n;\n  public static float test(){\n    return x*n;\n  }\n}"},

    {"id": "E2.10", "question": "On admet que la classe A existe.\n\nQue peut-on en déduire quant au(x) constructeur(s) de la classe A si l’instruction suivante génère une erreur de compilation ayant trait au(x) constructeur(s) de A ?\n\nA a = new A();"},

    {"id": "E2.11", "question": "Est-ce qu'une méthode peut être à la fois static et private en Java?"},

    {"id": "E2.12", "question": "Quelle est la visibilité des attributs au sein de cette classe :\n\npublic class Joe {\n  public int x = 0;\n  protected int y = 0;\n  private int z = 0;\n  int t = 0;\n}"},

    {"id": "E2.13", "question": "Écrivez une classe représentant une valeur entière à laquelle je peux ajouter la valeur trois par l'entremise d'une méthode public nommée patate. La méthode doit retourner la valeur entière modifiée. Le constructeur doit me permettre d'initialiser la valeur entière. La classe doit n'avoir que des attributs private."},

    {"id": "E2.14", "question": "Écrivez une classe représentant une valeur entière. Cette classe doit n'avoir qu'une seule méthode appelée additionne qui prend comme paramètre une instance de la classe et qui retourne une nouvelle instance de la classe. L'instance retournée doit comprendre la somme des deux valeurs entières."},

    {"id": "E2.15", "question": "Quelle est la différence entre public, private et protected pour un attribut ou une méthode en Java ?"},

    {"id": "E2.16", "question": "Considérez le code suivant :\n\nvoid afficher(String message) {}\nint afficher(int nombre) { return nombre; }\nvoid afficher(String message, int nombre) {}\n\nDécrivez la signature de la méthode afficher(String message, int nombre) et expliquez pourquoi ces trois méthodes peuvent coexister dans la même classe."},

    {"id": "E2.17", "question": "Pourquoi la signature d’une méthode ne tient-elle pas compte du type de retour ? Donnez un exemple où deux méthodes auraient le même nom et les mêmes paramètres mais des types de retour différents, et expliquez pourquoi cela pose problème."},

    {"id": "E2.18", "question": "Considérez l’expression suivante en Java :\n\nbool = (1 + 3 == 2) || f(x) || f(x);\n\nCombien de fois la fonction f(x) est-elle appelée lors de l’évaluation de cette expression ? Expliquez pourquoi."},

    {"id": "E2.19", "question": "Vrai ou Faux : Le mot-clé static permet de créer une seule variable en mémoire pour plusieurs instances d'un objet?"},

    {"id": "E2.20", "question": "Le code suivant est truffé d'erreurs. Veuillez énumérer les erreurs et les corriger.\n\npublic clas PleinErreurs {\n\n    public int entier = \"Entier\";\n    public static String string = new String(\"string\");\n\n    public static void main(String[] args) {\n        entier += 33;\n        string = entier + string;\n        System.out.println(string)\n    }\n}"},

    {"id": "E2.21", "question": "Expliquer pourquoi e1.resultat vaut 30 et non 80 à la fin de la méthode main. Que faudrait-il corriger dans le code suivant si on souhaite obtenir 80 ?\n\npublic class Exercice {\n    protected int numeroExercice = 1;\n    protected boolean reussi = false;\n    protected static short resultat = 0;\n    public static void main(String[] args) {\n        Exercice e1 = new Exercice();\n        e1.resultat = 80;\n        Exercice e2 = new Exercice();\n        e2.resultat = 30;\n        System.out.println(\"e1.resultat: \" + e1.resultat);\n    }\n}"},

    {"id": "E2.22", "question": "Soit les deux codes suivants :\n\n1)\n\npublic class Main {\n  public static void main(String[] args) {\n    final int NOMBRE;\n    System.out.println((NOMBRE = 10) + \" Je suis un nombre final \");\n  }\n}\n\n2)\n\npublic class Main {\n  public static void main(String[] args) {\n    final int NOMBRE = 0;\n    System.out.println((NOMBRE = 10) + \" Je suis un nombre final \");\n  }\n}\n\nLequel renvoie une erreur ? Pourquoi n’y a-t-il pas d’erreur dans celui qui s’exécute correctement ?"},

    {"id": "E2.23", "question": "Vous avez à créer une classe qui selon une constante de type nombre entier présente dans la classe, le code doit afficher le bon nombre de mots de la phrase suivante : \"Veni vidi vici\". Vous ne pouvez qu'utiliser les opérateurs vus dans la leçon précédente (indice : opérateur ternaire)."}
],
        "travail_note": {
            "id": "TN2",
            "question": "Écrire une méthode qui prend une liste d'entiers et retourne la somme des éléments pairs."
        }
    },

{
    "id": 3,
    "titre": "Module 3 : Gestion des exceptions, récursivité et streams",
    "introduction": """
    Bienvenue dans le Module 3 !  
    Ce module aborde trois sujets avancés de Java :
    - **Gestion des exceptions** : comprendre les mécanismes try/catch/finally, les exceptions checked/unchecked, créer ses propres exceptions.
    - **Récursivité** : écrire des fonctions récursives et comprendre le risque de débordement de pile.
    - **Streams** : utiliser l’API Stream pour manipuler des collections de manière fonctionnelle (filter, map, collect, etc.).
    - **Unicode et chaînes** : représentation des caractères en Java, UTF-16, et manipulation correcte des caractères Unicode.

    Prenez le temps de répondre à chaque question. N’hésitez pas à poser des questions à l’assistant si besoin.
    """,
    "exercices": [
        {"id": "E3.2", "question": "Qu’est-ce qu’une exception en Java ? Donnez un exemple de code qui attrape une exception lors d’une division par zéro."},
        {"id": "E3.3", "question": "Que se passera-t-il si vous placez l’instruction return dans le bloc « try » ou « catch » ? Le bloc « finally » s’exécutera-t-il ?"},
        {"id": "E3.4", "question": "Écrivez une fonction récursive qui calcule la somme des éléments d’un tableau d’entiers."},
        {"id": "E3.5", "question": "Que se passe-t-il si une fonction récursive n’a pas de cas d’arrêt (condition d’arrêt) ?"},
        {"id": "E3.6", "question": "Quelles sont les différences entre les exceptions vérifiées (checked) et non vérifiées (unchecked) en Java ?"},
        {"id": "E3.7", "question": "Que se passe-t-il si une exception n’est pas capturée dans un bloc try/catch ?"},
        {"id": "E3.8", "question": "Comment créer sa propre exception personnalisée en Java ?"},
        {"id": "E3.9", "question": "À quoi sert le mot-clé throw en Java ? Donnez un exemple d’utilisation."},
        {"id": "E3.10", "question": "Que se passe-t-il si on place plusieurs blocs catch à la suite d’un try ? Dans quel ordre sont-ils évalués ?"},
        {"id": "E3.11", "question": "Qu’est-ce que le ramasse-miettes (garbage collector) en Java ? Quels sont ses avantages et ses inconvénients par rapport à la gestion manuelle de la mémoire ?"},
        {"id": "E3.12", "question": "Comment peut-on limiter le surcoût du ramasse-miettes (garbage collector) dans une application Java ? Donnez quelques bonnes pratiques pour réduire son impact sur les performances."},
        {"id": "E3.13", "question": "Qu’est-ce que l’encodage UTF-16 et pourquoi Java l’utilise-t-il pour représenter les chaînes de caractères (String) ?"},
        {"id": "E3.14", "question": "Expliquez pourquoi la méthode charAt(int index) sur une String Java ne retourne pas toujours un caractère complet pour l’utilisateur. Donnez un exemple."},
        {"id": "E3.15", "question": "Comment peut-on parcourir correctement tous les caractères Unicode d’une String en Java, même ceux codés sur deux char ?"},
        {"id": "E3.16", "question": "Combien de mémoire une String Java utilise-t-elle par caractère ? Cette valeur est-elle toujours la même pour tous les caractères ?"},
        {"id": "E3.17", "question": "Écrivez un programme Java qui prend une chaîne de caractères en entrée et affiche la valeur numérique (code Unicode) de chaque char de la chaîne."},
        {"id": "E3.18", "question": "Qu’est-ce qu’un stream en Java ? À quoi sert-il ?"},
        {"id": "E3.19", "question": "Expliquez le rôle de la méthode filter dans un stream Java. Donnez un exemple."},
        {"id": "E3.20", "question": "À quoi sert la méthode map dans un stream ? Donnez un exemple."},
        {"id": "E3.21", "question": "Expliquez l’utilité de la méthode limit dans un stream Java."},
        {"id": "E3.22", "question": "Que fait la méthode distinct sur un stream ? Donnez un exemple."},
        {"id": "E3.23", "question": "Quel est le rôle de la méthode sorted dans un stream Java ?"},
        {"id": "E3.24", "question": "À quoi sert la méthode collect dans un stream ? Donnez un exemple d’utilisation avec Collectors.toList()."},
        {"id": "E3.25", "question": "Expliquez la différence entre un stream et une collection en Java."},
        {"id": "E3.26", "question": "Donnez un exemple d’utilisation de stream() sur une liste de chaînes pour obtenir la liste des longueurs distinctes, triées, de ces chaînes."}
    ],
    "travail_note": {
        "id": "TN3",
        "question": "Écrire un programme Java complet qui :\n- Lit un fichier texte (dont le nom est passé en argument).\n- Compte le nombre d’occurrences de chaque mot (en ignorant la casse).\n- Affiche les 10 mots les plus fréquents.\n- Utilise les streams et la gestion des exceptions pour gérer les erreurs (fichier non trouvé, etc.).\n- Expliquez votre code en pseudocode, puis en Java."
    }

},


{
    "id": 4,
    "titre": "Module 4 : Entrées/Sorties, fichiers et flux en Java",
    "introduction": """
    Bienvenue dans le Module 4 !  
    Ce module explore les mécanismes d’entrées/sorties (E/S) en Java, essentiels pour la manipulation des fichiers, des flux binaires et textuels, et des canaux NIO.  
    Vous aborderez :
    - Les classes `File`, `Scanner`, `PrintStream`, `DataOutputStream`.
    - La gestion des fichiers texte et binaires.
    - Les tampons (buffers) et les canaux (`FileChannel`, `ByteBuffer`).
    - Les flux avec `java.nio.file` et l’API `java.net.http`.
    - La notion de boutisme (endianness) et de mappage mémoire.
    - Les bonnes pratiques pour optimiser les performances (bufferisation, StringWriter, etc.).

    Répondez aux questions en rédigeant des extraits de code ou des explications claires.  
    L’assistant est disponible à gauche pour vous aider en cas de doute.
    """,
    "exercices": [
        {"id": "E4.1", "question": "Le programme suivant permet-il de lire deux lignes entrées au clavier ?\n\n```java\nimport java.util.Scanner;\nclass TestIn {\n    public static void main(String[] args) {\n        Scanner scanner = new Scanner(System.in);\n        System.out.println(\"==> Taper deux lignes\");\n        System.out.print(\"?\");\n        String ligne1 = scanner.nextLine();\n        System.out.print(\"?\");\n        String ligne2 = scanner.nextLine();\n        System.out.println(\"==> Les deux lignes lues sont:\\n==>  \" + ligne1 + \"\\n==> \" + ligne2);\n    }\n}\n```"},
        {"id": "E4.2", "question": "Que fait ce programme ?\n\n```java\nimport java.io.*;\nimport java.util.*;\nclass TestFichOut {\n    public static void main(String[] args) {\n        File fichier = new File(\"Lasortie.txt\");\n        try (\n            FileOutputStream streamFich = new FileOutputStream(fichier);\n            DataOutputStream d = new DataOutputStream(streamFich);\n            PrintStream out = new PrintStream(d);\n            Scanner sc = new Scanner(System.in);\n        ) {\n            String ligne = \"\";\n            System.out.println(\"==> Taper des lignes terminées par ctrl-D\");\n            System.out.print(\"?\");\n            while(sc.hasNextLine()) {\n                out.println(\"\" + sc.nextLine());\n                System.out.print(\"?\");\n            }\n            System.out.println();\n        } catch (java.io.IOException e) {\n            System.out.println(\"Il y a une erreur de lecture ou écriture\");\n        } finally {}\n    }\n}\n```"},
        {"id": "E4.3", "question": "En supposant que vous avez les droits d’écriture et de lecture appropriés, créez un fichier séquentiel binaire (monFichier) dans un répertoire (monRepertoire) sur la racine. On suppose que le fichier et le répertoire n’existent pas déjà. Écrivez dans ce fichier les nombres entiers de 0 à 9."},
        {"id": "E4.4", "question": "Écrivez un programme qui affiche le contenu du fichier de l’exercice précédent, puis ajoute à ce fichier le double des entiers impairs de 0 à 9. Les noms de répertoire et de fichier devront être fournis par l’utilisateur qui les saisira au clavier."},
        {"id": "E4.5", "question": "En poursuivant avec le même exemple que les deux exercices précédents, écrivez un programme qui affiche le contenu du fichier, puis modifie ce fichier en remplaçant les nombres entiers impairs par leur double. Les noms de répertoire et de fichier devront être fournis par l’utilisateur qui les saisira au clavier.\n\nQuelle est la différence entre cet exercice et l’exercice précédent du point de vue des types d’accès et des possibilités qui y sont liées ?"},
        {"id": "E4.6", "question": "Créez un fichier texte nommé unFichier dans le répertoire courant et écrivez-y « Bonjour, je suis bien créé ». Ce nom sera fourni par l’utilisateur sous forme de chaîne « unFichier.txt »."},
        {"id": "E4.7", "question": "Écrivez un code qui prend en paramètre le nom du fichier de l’exercice précédent (unFichier.txt) et affiche son chemin d’accès (c’est-à-dire le répertoire courant) ainsi que le contenu du fichier.\n\nOn suppose dans cet exercice qu’on reste dans le même répertoire courant qu’à l’exercice précédent."},
        {"id": "E4.8", "question": "Écrivez un programme Java qui compte le nombre de voyelles dans une chaîne de caractères saisie par l’utilisateur."},
        {"id": "E4.9", "question": "Écrivez un programme Java qui lit un fichier texte ligne par ligne et affiche chaque ligne précédée de son numéro (exemple : 1: première ligne, 2: deuxième ligne, etc.)."},
        {"id": "E4.10", "question": "Écrivez un programme Java qui demande à l’utilisateur un nom de fichier, puis affiche le nombre de caractères dans ce fichier."},
        {"id": "E4.11", "question": "Le code suivant lit un fichier texte ligne par ligne et concatène toutes les lignes dans une seule chaîne :\n\n```java\nimport java.io.*;\nString resultat = \"\";\nBufferedReader reader = new BufferedReader(new FileReader(\"fichier.txt\"));\nString ligne;\nwhile ((ligne = reader.readLine()) != null) {\n    resultat = resultat + ligne;\n}\nreader.close();\n```\n\nRéécrivez ce code de façon plus performante. Expliquez pourquoi votre version est préférable."},
        {"id": "E4.12", "question": "Le code suivant lit un fichier caractère par caractère sans utiliser de buffer :\n\n```java\nimport java.io.*;\nFileReader reader = new FileReader(\"fichier.txt\");\nint c;\nwhile ((c = reader.read()) != -1) {\n    // Traitement du caractère c\n}\nreader.close();\n```\n\nExpliquez pourquoi ce code peut être lent pour de gros fichiers. Proposez une version optimisée utilisant un buffer, et expliquez pourquoi elle est préférable."},
        {"id": "E4.13", "question": "Écrivez un programme Java qui utilise StringWriter pour construire une chaîne contenant des paires clé-valeur au format clé=valeur, puis utilise StringReader pour lire et afficher chaque ligne de cette chaîne."},
        {"id": "E4.14", "question": "Écrivez un programme Java qui utilise ByteArrayOutputStream pour écrire une séquence de bytes à partir d’une chaîne, puis ByteArrayInputStream pour lire et afficher ces bytes comme caractères."},
        {"id": "E4.15", "question": "Écrivez un programme Java qui utilise ByteBuffer pour écrire une liste de 5 entiers dans un buffer, puis lire et afficher ces entiers dans l’ordre inverse."},
        {"id": "E4.16", "question": "Écrivez un programme Java qui utilise FileChannel pour écrire une chaîne dans un fichier texte, puis lire et afficher son contenu."},
        {"id": "E4.17", "question": "Écrivez un programme Java qui crée un fichier .properties avec des paires clé-valeur, puis lit et affiche une propriété spécifique demandée par l’utilisateur."},
        {"id": "E4.18", "question": "Écrivez un programme Java qui utilise l’API java.net.http pour envoyer une requête HTTP GET à une URL donnée et afficher le code de statut et le corps de la réponse."},
        {"id": "E4.19", "question": "Le code suivant utilise HttpURLConnection pour envoyer une requête HTTP GET :\n\n```java\nimport java.net.*;\nimport java.io.*;\nURL url = new URL(\"https://example.com\");\nHttpURLConnection conn = (HttpURLConnection) url.openConnection();\nconn.setRequestMethod(\"GET\");\nBufferedReader reader = new BufferedReader(new InputStreamReader(conn.getInputStream()));\nString ligne;\nStringBuilder resultat = new StringBuilder();\nwhile ((ligne = reader.readLine()) != null) {\n    resultat.append(ligne);\n}\nreader.close();\n```\n\nExpliquez pourquoi ce code peut être moins pratique que l’API java.net.http. Proposez une version optimisée utilisant HttpClient."},
        {"id": "E4.20", "question": "Écrivez un programme Java qui lit une séquence d’entiers stockée dans un fichier binaire (où chaque entier occupe 4 octets) à l’aide de FileChannel et ByteBuffer, puis vérifie si toutes les valeurs sont positives (strictement supérieures à 0). Le programme doit afficher un message indiquant si toutes les valeurs sont positives ou lister les valeurs non positives trouvées."},
        {"id": "E4.21", "question": "Écrivez un programme Java qui lit une séquence d’entiers à partir d’un fichier texte, où les entiers sont séparés par des espaces (par exemple, “10 20 -5 30 0”), en utilisant l’API java.nio.file. Le programme doit vérifier si toutes les valeurs sont positives (strictement supérieures à 0) et afficher un message indiquant si toutes les valeurs sont positives ou lister les valeurs non positives trouvées."},
        {"id": "E4.22", "question": "Écrivez un programme Java qui lit un fichier texte et compte le nombre total de lignes, de mots et de caractères (hors espaces et retours à la ligne). Le nom du fichier est saisi par l’utilisateur."},
        {"id": "E4.23", "question": "Écrivez un programme Java qui lit un fichier texte et affiche uniquement les lignes contenant un mot spécifique saisi par l’utilisateur. Le programme doit être insensible à la casse."},
        {"id": "E4.24", "question": "Écrivez un programme Java qui lit un fichier texte et remplace toutes les occurrences d’un mot donné par un autre mot, puis affiche le contenu modifié. Les mots sont saisis par l’utilisateur, et le programme doit préserver la casse."},
        {"id": "E4.25", "question": "Écrivez un programme Java qui lit un fichier texte et affiche les n premières lignes, où n est un nombre saisi par l’utilisateur. Si le fichier a moins de n lignes, toutes les lignes sont affichées."},
        {"id": "E4.26", "question": "Écrivez un programme Java qui lit un fichier texte et vérifie si son contenu est un palindrome (c’est-à-dire si le texte lu à l’envers est identique au texte original, en ignorant la casse, les espaces et la ponctuation)."},
        {"id": "E4.27", "question": "Écrivez un programme Java qui utilise le mappage en mémoire pour lire un fichier binaire contenant une séquence d’entiers (4 octets chacun) et calcule la somme de ces entiers. Le nom du fichier est saisi par l’utilisateur, et le programme doit vérifier que la taille du fichier est un multiple de 4 octets pour garantir des données valides."},
        {"id": "E4.28", "question": "Écrivez un programme Java qui écrit une séquence de 5 entiers (par exemple, 1 à 5) dans un fichier binaire en utilisant explicitement l’ordre big-endian, puis lit ce fichier en supposant un ordre little-endian pour démontrer l’impact du boutisme incorrect. Affichez les valeurs lues et expliquez pourquoi elles diffèrent des valeurs originales."},
        {"id": "E4.29", "question": "Écrivez un programme Java qui lit un fichier binaire contenant une séquence d’entiers (4 octets chacun) et permet à l’utilisateur de choisir l’ordre de boutisme (big-endian ou little-endian) pour interpréter les données. Le programme affiche les entiers lus selon l’ordre choisi et indique si la taille du fichier est valide pour des entiers."}
    ],
    "travail_note": {
        "id": "TN4",
        "question": "Écrivez un programme Java complet qui gère un fichier de notes d’étudiants (nom, note sur 100). Il doit offrir les fonctionnalités suivantes :\n- Ajouter un étudiant (nom + note) – si le fichier existe, on ajoute à la fin ; sinon on le crée.\n- Afficher tous les étudiants et leurs notes.\n- Calculer la moyenne des notes.\n- Sauvegarder les données dans un fichier CSV (ou binaire).\n- Charger les données depuis ce fichier au lancement.\n- Gérer les exceptions (fichier non trouvé, erreur de lecture/écriture).\n- Utiliser les flux (buffered) pour les entrées/sorties et une structure de données appropriée (ex. ArrayList).\n\nDonnez le pseudocode complet, puis l’implémentation Java avec les commentaires nécessaires."
    }
},

  {
    "id": 5,
    "titre": "Module 5 : Héritage, polymorphisme, interfaces et bonnes pratiques",
    "introduction": """
    Bienvenue dans le Module 5 !  
    Ce module avancé aborde les concepts fondamentaux de la programmation orientée objet en Java :
    - **Héritage** : création de classes parentes et enfants, redéfinition de méthodes.
    - **Polymorphisme** : polymorphisme paramétrique (génériques), polymorphisme par surcharge et par redéfinition.
    - **Interfaces** : définition et implémentation d'interfaces, classes abstraites.
    - **Bonnes pratiques** : Comparable vs Comparator, equals() et hashCode(), records, annotations.
    - **Principes SOLID** : substitution de Liskov, inversion de dépendances.
    - **Sérialisation** et **Cloneable**.
    - **Expressions lambda** et **classes anonymes**.

    Ce module est conçu pour consolider votre maîtrise de la POO en Java.  
    L'assistant est disponible à gauche pour vous aider en cas de doute.
    """,
    "exercices": [
        {"id": "E5.1", "question": "Pourquoi le code suivant entraîne-t-il une erreur à la compilation ?\n\n```java\npublic class Test extends JFrame, Thread {\n    String test;    \n    public Test(String test) {\n        this.test = test;\n    }\n    public void run() {\n        System.out.println(test);\n    }\n}\n```"},
        {"id": "E5.2", "question": "Voici une classe permettant de lire une image de type PNG et d'en extraire les occurrences de gradients de couleur :\n\n```java\npublic class PNGGradientExtractor {\n    int[][] gradientMatrix;\n    public PNGGradientExtractor(File file) {\n        loadImage(file);\n    }\n    public void loadImage(File file) {\n        //Charge l'image et la met en format \"raw\" dans la matrice gradientMatrix\n        return;\n    }\n    public HashMap getGradientMap() {\n        // Retourne une hashmap avec l'occurence de gradient dans l'image\n        return null;\n    }\n}\n```\n\nÀ l'aide de l'héritage et des classes abstraites, veuillez implémenter les classes qui permettront de : a. Créer une classe abstraite GradientExtractor; b. Créer une classe GIFGradientExtractor; c. modifier PNGGradientExtractor pour tenir compte des changements précédent. Pour simplifier l'exercice, ce qui diffère le GIF du PNG est le chargement de l'image dans la matrice gradientMatrix. VOUS DEVEZ FAIRE SEULEMENT LA STRUCTURE (CLASSES ET MÉTHODES) SANS IMPLÉMENTATION !"},
        {"id": "E5.3", "question": "Voici une classe permettant de calculer la régression linéaire d'une série temporelle d'entiers :\n\n```java\npublic class SerieTemporelle {\n    int[] serie;\n    public SerieTemporelle(int[] serie) {\n        this.serie = serie;\n    }\n    public void calculerRegressionLineaire() {\n        int MAXN = 1000;\n        double[] x = new double[MAXN];\n        double[] y = new double[MAXN];\n        double sumx = 0.0, sumy = 0.0, sumx2 = 0.0;\n        for (int i = 0; i < serie.length; i++) {\n            x[i] = i;\n            y[i] = serie[i];\n            sumx  += x[i];\n            sumx2 += x[i] * x[i];\n            sumy  += y[i];\n        }\n        double xbar = sumx / serie.length;\n        double ybar = sumy / serie.length;\n        double xxbar = 0.0, yybar = 0.0, xybar = 0.0;\n        for (int i = 0; i < serie.length; i++) {\n            xxbar += (x[i] - xbar) * (x[i] - xbar);\n            yybar += (y[i] - ybar) * (y[i] - ybar);\n            xybar += (x[i] - xbar) * (y[i] - ybar);\n        }\n        double beta1 = xybar / xxbar;\n        double beta0 = ybar - beta1 * xbar;\n        System.out.println(\"y   = \" + beta1 + \" * x + \" + beta0);\n        int df = serie.length - 2;\n        double rss = 0.0;\n        double ssr = 0.0;\n        for (int i = 0; i < serie.length; i++) {\n            double fit = beta1*x[i]+beta0;\n            rss += (fit - y[i]) * (fit - y[i]);\n            ssr += (fit - ybar) * (fit - ybar);\n        }\n        double R2    = ssr / yybar;\n        double svar  = rss / df;\n        double svar1 = svar / xxbar;\n        double svar0 = svar/serie.length + xbar*xbar*svar1;\n        System.out.println(\"R^2                 = \" + R2);\n        System.out.println(\"std error of beta_1 = \" + Math.sqrt(svar1));\n        System.out.println(\"std error of beta_0 = \" + Math.sqrt(svar0));\n        svar0 = svar * sumx2 / (serie.length * xxbar);\n        System.out.println(\"std error of beta_0 = \" + Math.sqrt(svar0));\n        System.out.println(\"SSTO = \" + yybar);\n        System.out.println(\"SSE  = \" + rss);\n        System.out.println(\"SSR  = \" + ssr);\n    }\n    public static void main(String[] args) {\n        int[] serie = {100, 22, 55, 10, 5, 66, 71, 8, 91};\n        SerieTemporelle serieTemporelle = new SerieTemporelle(serie);\n        serieTemporelle.calculerRegressionLineaire();\n    }\n}\n```\n\nÀ l'aide du polymorphisme paramétrique (les templates), veuillez modifier le code afin de permettre des séries temporelles de plusieurs classes (ex. Double, Integer, etc.)."},
        {"id": "E5.4", "question": "À partir du code suivant, veuillez en extraire une classe supérieure qui sera héritée et deux interfaces :\n\n```java\npublic class VoitureEssence {\n    public boolean isRunning() { return false; }\n    public void addGaz(int litres) { }\n    public double getSpeed() { return 0; }\n}\n\npublic class VoitureElectrique {\n    public boolean isRunning() { return false; }\n    public void chargeBattery(int mah) { }\n    public double getSpeed() { return 0; }\n}\n```"},
        {"id": "E5.5", "question": "Dans le code ci-dessous, quel est le type de polymorphisme utilisé ?\n\n```java\npublic class Classe1 {\n    public void uneMethode(String arg) { }\n    public void uneMethode(StringBuffer arg) { }\n}\n```"},
        {"id": "E5.6", "question": "Dans le code ci-dessous, quel est le type de polymorphisme utilisé ?\n\n```java\npublic class Classe1 {\n    public void uneMethode() { }\n}\npublic class Classe2 extends Classe1 {\n    public void uneMethode() { }\n    public static void main(String[] args) {\n        Classe2 uneClase = new Classe2();\n        ((Classe1) uneClase).uneMethode();\n    }\n}\n```"},
        {"id": "E5.7", "question": "Considérons la classe Point suivante :\n\n```java\npublic class Point {\n    public Point (int abs, int ord) { x = abs; y = ord; }\n    public void deplace (int dx, byte dy) { x += dx; y += dy; }\n    public void deplace (byte dx, int dy) { x += dx; y += dy; }\n    int x, y;\n}\n```\n\nOn voit que la classe Point a deux méthodes qui portent le même nom : Quelle technique est mise en œuvre pour y parvenir ici ?\nQuel est le résultat de la compilation de chacune des deux classes suivantes ? Expliquez chacun de ces résultats.\n\n```java\npublic class Test1 {\n    public static void main (String args[]) {\n        int n=1; byte b=1;\n        Point a = new Point(n,n);\n        a.deplace(b, b);\n    }\n}\n\npublic class Test2 {\n    public static void main (String args[]) {\n        int n=1; byte b=1;\n        Point a = new Point(n,n);\n        a.deplace (2*b, b);\n    }\n}\n```"},
        {"id": "E5.8", "question": "On suppose qu'il existe une classe A dotée d'un constructeur par défaut.\nSoient les trois instructions suivantes :\n\n```java\nA a = new A();\nObject o = new Object();\no = a;\n```\n\nÀ l'issue de ces trois instructions, on a :\n- deux variables de même type et contenant les mêmes références ;\n- deux variables de type différent contenant les mêmes références ;\n- deux variables de même type contenant des références différentes ;\n- rien de tout cela car une erreur est générée."},
        {"id": "E5.9", "question": "On dispose d'une interface I mettant en œuvre plusieurs méthodes. Soit\n\n```java\ninterface I {\n    void methode1();\n    void methode2();\n    void methode3();\n    void methode4();\n}\n```\n\nOn voudrait faire partager cette interface par deux classes ClasseA et ClasseB pouvant être regroupées dans une classe de base ClasseDeBase et partageant au moins une méthode (methodeDifferee) présente dans cette classe de base mais non encore définie. De plus, ClasseA ne doit implémenter que methode1 et methode2 de I, alors que ClasseB doit implémenter methode3 et methode4 de I.\n\nUn programmeur songe à la solution suivante. Cette solution est-elle correcte ? Si non, corrigez-la.\n\n```java\nabstract class ClasseDeBase {\n    abstract public void methodeDifferee();\n}\npublic class ClasseA extends ClasseDeBase implements I {\n    public void methodeDifferee() {\n        System.out.print(\"instructions de la méthode différée ici\");\n    }\n    void methode1() {\n        System.out.print(\"instructions de méthode1 ici\");\n    }\n    void methode2() {\n        System.out.print(\"instructions de méthode2 ici\");\n    }\n}\npublic class ClasseB extends ClasseDeBase implements I {\n    public void methodeDifferee() {\n        System.out.print(\"instructions de la méthode différée ici\");\n    }\n    void methode3() {\n        System.out.print(\"instructions de méthode3 ici\");\n    }\n    void methode4() {\n        System.out.print(\"instructions de méthode4 ici\");\n    }\n}\n```"},
        {"id": "E5.10", "question": "On dispose de différentes classes d'animaux (Poissons, Reptiles, Oiseaux, Mammifères) qui partagent en commun la méthode seDeplace. On voudrait effectuer un traitement qui consiste juste pour chaque animal d'une classe à afficher comment il se déplace. Ainsi, pour un Poisson p, p.seDeplace doit afficher « je suis un poisson, je nage » ; un Reptile « je suis un reptile, je rampe » ; un Oiseau « je suis un oiseau, je vole » ; un Mammifère « je suis un mammifère, je marche, je vole et je nage ». Proposer une solution en utilisant un seul tableau d'objets."},
        {"id": "E5.11", "question": "Expliquez la différence entre l'héritage simple et l'implémentation d'interfaces en Java."},
        {"id": "E5.12", "question": "Écrivez une interface Java nommée Volant avec une méthode void voler(), puis une classe Oiseau qui implémente cette interface."},
        {"id": "E5.13", "question": "Expliquez la différence entre la redéfinition (override) et la surcharge (overload) de méthodes en Java."},
        {"id": "E5.14", "question": "Écrivez une classe Personne avec un attribut nom et une méthode afficherNom(). Créez une sous-classe Etudiant qui ajoute un attribut matricule et redéfinit la méthode afficherNom() pour afficher le nom et le matricule."},
        {"id": "E5.15", "question": "Écrivez une classe Java Animal avec une méthode parler() qui affiche \"Je suis un animal\". Créez deux sous-classes Chien et Chat qui redéfinissent la méthode parler() pour afficher respectivement \"Wouf\" et \"Miaou\"."},
        {"id": "E5.16", "question": "Expliquez à quoi sert l'interface Serializable en Java et donnez un exemple de situation où il est nécessaire de l'utiliser."},
        {"id": "E5.17", "question": "Écrivez un exemple de classe Java qui implémente l'interface Comparable pour permettre le tri naturel d'objets selon un attribut."},
        {"id": "E5.18", "question": "Quelle est la différence entre Comparable et Comparator en Java ? Donnez un exemple d'utilisation de Comparator pour trier une liste d'objets selon un critère différent du tri naturel."},
        {"id": "E5.19", "question": "Donnez un exemple d'instanciation anonyme d'une interface Comparator en Java."},
        {"id": "E5.20", "question": "Pourquoi est-il utile d'utiliser des classes anonymes ou des expressions lambda pour implémenter des interfaces fonctionnelles en Java ? Donnez un exemple de cas où cela simplifie le code."},
        {"id": "E5.21", "question": "Expliquez le principe de substitution de Liskov (Liskov Substitution Principle, LSP) en programmation orientée objet. Donnez un exemple simple en Java illustrant une violation de ce principe."},
        {"id": "E5.22", "question": "Expliquez comment l'utilisation d'une interface peut simplifier le code en Java. Donnez un exemple concret où l'interface permet d'écrire du code plus flexible et réutilisable."},
        {"id": "E5.23", "question": "Expliquez la différence entre l'opérateur == et la méthode equals() en Java. Donnez un exemple où l'utilisation de l'un ou de l'autre change le résultat."},
        {"id": "E5.24", "question": "Qu'est-ce que la méthode hashCode() ? Pourquoi est-il important de la redéfinir lorsqu'on redéfinit equals() ?"},
        {"id": "E5.25", "question": "Peut-on utiliser les méthodes equals() et hashCode() avec des types primitifs comme int ou double ? Expliquez pourquoi."},
        {"id": "E5.26", "question": "Qu'est-ce qu'un record en Java ? Expliquez ses avantages et donnez un exemple d'utilisation."},
        {"id": "E5.27", "question": "Comment peut-on transformer un tableau d'entiers en une liste d'entiers en utilisant les streams ?"},
        {"id": "E5.28", "question": "Comment peut-on vérifier en Java qu'un objet est une instance d'une classe donnée ? Ou qu'un objet satisfait à une interface donnée ?"},
        {"id": "E5.29", "question": "Si j'ai une instance d'une classe, comment puis-je savoir si elle n'est pas en fait d'une classe dérivée (c'est-à-dire d'une sous-classe) ?"},
        {"id": "E5.30", "question": "Expliquez à quoi sert l'annotation @Override en Java et dans quels cas son utilisation est recommandée."},
        {"id": "E5.31", "question": "Quelles sont les principales caractéristiques de l'interface Iterable en Java ? Donnez un exemple simple d'utilisation."},
        {"id": "E5.32", "question": "Expliquez le rôle de l'interface Cloneable en Java et les précautions à prendre lors de son utilisation."},
        {"id": "E5.33", "question": "Comment les méthodes clone(), equals() et l'opérateur == sont-ils liés en termes de comparaison et de copie d'objets en Java ?"},
        {"id": "E5.34", "question": "Quelles précautions faut-il prendre lors de la redéfinition de equals() pour une classe implémentant Cloneable ?"}
    ],
    "travail_note": {
        "id": "TN5",
        "question": "Vous devez concevoir un système de gestion d'une bibliothèque en Java respectant les principes de la POO.\n\n**Spécifications fonctionnelles :**\n- La bibliothèque contient des documents : livres, revues, et DVD.\n- Chaque document a un titre, un auteur (ou réalisateur), un numéro d'identification unique et une année de publication.\n- Un livre a un nombre de pages et un éditeur.\n- Une revue a un numéro de volume et une périodicité (mensuelle, hebdomadaire, etc.).\n- Un DVD a une durée en minutes et un réalisateur.\n- Tous les documents peuvent être empruntés ou rendus.\n- Un emprunteur a un nom, un numéro d'adhérent, et peut emprunter jusqu'à 5 documents simultanément.\n- La bibliothèque permet d'ajouter des documents, de rechercher par titre ou par auteur, de lister tous les documents disponibles, et de gérer les emprunts/retours.\n\n**Contraintes techniques :**\n- Utilisez une hiérarchie de classes avec une classe abstraite Document.\n- Utilisez une interface Empruntable (ou une classe abstraite) pour gérer l'emprunt.\n- Utilisez le polymorphisme (tableau de Document) pour gérer tous les types de documents.\n- Utilisez Comparable pour le tri naturel (par titre).\n- Utilisez Comparator pour un tri par année de publication.\n- Implémentez equals() et hashCode() pour la classe Document.\n- Utilisez des records pour représenter les données immuables (ex. Adresse de l'emprunteur).\n\n**À fournir :**\n1. Le diagramme de classes (pseudocode des classes et interfaces).\n2. L'implémentation complète en Java des classes principales avec les commentaires nécessaires.\n3. Un programme de test (main) qui démontre toutes les fonctionnalités."
    }
}  
]