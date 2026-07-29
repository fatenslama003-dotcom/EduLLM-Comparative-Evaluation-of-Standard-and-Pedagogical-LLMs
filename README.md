# EduLLM: Comparative Evaluation of Standard and Pedagogical LLMs for Java Learning

## Overview

EduLLM is an AI-powered educational platform designed to study the impact of pedagogically guided Large Language Models (LLMs) on beginner programming education.

The platform compares two learning assistants:

- **Reactive LLM Assistant**: provides direct answers and explanations based on students' questions.
- **Pedagogical LLM Tutor**: guides students step-by-step using instructional strategies such as hints, questioning, scaffolding, and adaptive feedback.

The goal is to evaluate how different LLM interaction styles influence students' learning outcomes, engagement, and problem-solving abilities in Java programming.

---

## Research Objective

This project investigates the following research question:

> Does a pedagogically guided LLM improve programming learning compared to a standard conversational LLM?

The study follows an experimental design with two groups:

| Group | Assistant Type |
|------|----------------|
| Group A | Reactive LLM |
| Group B | Pedagogical LLM Tutor |

Students complete:

1. Pre-test to evaluate initial knowledge
2. Java learning modules with AI assistance
3. Post-test to measure learning improvement
4. Transfer test to evaluate problem-solving ability without AI assistance

---

## Features

- 🤖 AI-based Java programming assistant
- 🧑‍🏫 Pedagogically guided tutoring approach
- 💬 Conversational learning environment
- 📚 Modular Java learning path
- 📝 Pre-test, post-test, and transfer assessment
- 📊 Automatic interaction logging for research analysis
- 🔄 Comparison between reactive and pedagogical AI assistance

---

## System Architecture

The platform is developed using:

- **Frontend:** Streamlit
- **Programming Language:** Python
- **LLM API:** OpenAI-compatible API (GitHub Models)
- **Model:** GPT-4o-mini
- **Data Storage:** CSV-based logging
- **Configuration:** Environment variables (.env)

---

## Project Structure

EduLLM/
│
├── app.py # Main Streamlit application
├── prompts.py # LLM system prompts
├── problems.py # Java programming problems
├── modules.py # Learning modules
│
├── pretest.json # Pre-test questions
├── posttest.json # Post-test questions
├── transfert.json # Transfer test questions
│
├── logs.csv # Student interactions
├── reponses_apprentissage.csv
│
├── images/
│ └── teluq.png
│
└── requirements.txt


---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/EduLLM.git
cd EduLLM

Install dependencies:

pip install -r requirements.txt

Create a .env file:

GITHUB_TOKEN=your_github_token

Run the application:

streamlit run app.py
Experimental Workflow
Registration
     |
     v
Pre-test
     |
     v
Java Learning Modules
     |
     +---- Reactive LLM
     |
     +---- Pedagogical LLM
     |
     v
Post-test
     |
     v
Transfer Test
     |
     v
Data Analysis
