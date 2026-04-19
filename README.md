# AI Agent Teaching Materials for EEEA

## English

This repository contains introductory AI Agent teaching materials for students at EEEA. The course is designed to help students set up a Python environment, understand the basic structure of an AI Agent, and build simple agents with tools, search, prompts, and sequential multi-agent workflows.

### Learning Goals

After completing this course, students should be able to:

- Create an isolated Python environment with Anaconda.
- Add the course environment to Jupyter Lab.
- Install and use `google-adk` and `python-dotenv`.
- Configure a Google API key through a local `.env` file.
- Build a basic AI Agent with Google ADK.
- Add Google Search as a tool for factual or recent information.
- Add a custom Python function as an Agent tool.
- Understand the idea of a sequential multi-agent pipeline.

### Project Structure

```text
.
├── Instruction.ipynb
├── my_agent_project/
│   ├── __init__.py
│   └── agent.py
└── Sequential_agent/
    ├── __init__.py
    └── agent.py
```

### Main Files

#### `Instruction.ipynb`

This notebook is the main course guide. It walks students through:

1. Creating the `agent_env` conda environment.
2. Adding the environment to Jupyter Lab.
3. Installing the required packages.
4. Creating a `.env` file.
5. Checking whether `GOOGLE_API_KEY` is available.
6. Building a basic Agent.
7. Adding Google Search to an Agent.
8. Adding a custom function tool.
9. Testing more detailed prompt instructions.

#### `my_agent_project/agent.py`

This file contains a single-agent example named `search_helper`. It uses the `gemini-2.5-flash` model and the `google_search` tool.

The example demonstrates how to:

- Define a `root_agent`.
- Write clear Agent instructions.
- Use search when a question requires current information, factual verification, or restaurant evaluation.

#### `Sequential_agent/agent.py`

This file contains a sequential multi-agent example using `SequentialAgent`.

The workflow is divided into three agents:

- `research_agent`: gathers key facts and returns structured JSON.
- `outline_agent`: converts the JSON into a title and bullet-point outline.
- `final_agent`: writes a short final answer from the outline.

This example is useful for explaining how a complex task can be divided into smaller steps handled by different agents.

### Environment Setup

Create and activate the conda environment:

```bash
conda create -n agent_env python=3.11
conda activate agent_env
```

Install the Jupyter kernel:

```bash
pip install ipykernel
python -m ipykernel install --user --name agent_env --display-name "agent_env"
```

Install the required packages:

```bash
pip install google-adk python-dotenv
```

### Google API Key

Create a `.env` file in the project directory:

```bash
vi .env
```

Add the following line:

```text
GOOGLE_API_KEY=Your key
```

Do not commit your real API key to GitHub.

You can test the configuration in the notebook:

```python
import os
from dotenv import load_dotenv

load_dotenv(".env")
print(os.getenv("GOOGLE_API_KEY") is not None)
```

If the output is `True`, the API key was loaded correctly.

### Running the Agent

From the parent directory that contains the Agent project folder, run:

```bash
adk web
```

Then open the ADK Web interface in your browser and select the Agent you want to test.

### Suggested Classroom Flow

1. Prepare the Python and Jupyter environment.
2. Run a basic Agent and discuss `name`, `model`, and `instruction`.
3. Add Google Search and compare answers with and without search.
4. Add a custom function tool.
5. Modify prompts and observe how instructions change Agent behavior.
6. Introduce `SequentialAgent` and explain multi-step Agent collaboration.

### Student Exercises

- Ask the basic Agent to explain AI Agents in one sentence.
- Ask the search Agent to find a recent AI news item and summarize it.
- Give the Agent a restaurant name and ask for ranking information and detailed comments.
- Modify a custom function so the Agent can return course, school, or class information.
- Adapt the sequential pipeline to research a topic and write a short summary.

### Notes

- The `.env` file should stay local because it contains private credentials.
- If search does not work, check whether the Google API key is configured correctly.
- If Jupyter Lab does not show `agent_env`, run the kernel installation command again.
- If `adk web` cannot find the Agent, check whether `agent.py` defines `root_agent`.

## Français

Ce dépôt contient des supports d'introduction aux AI Agents pour les étudiants de l'EEEA. Le cours aide les étudiants à configurer un environnement Python, comprendre la structure de base d'un Agent, puis créer des agents simples avec des outils, la recherche, des prompts et un flux multi-agent séquentiel.

### Objectifs Pédagogiques

À la fin du cours, les étudiants devraient être capables de :

- Créer un environnement Python isolé avec Anaconda.
- Ajouter l'environnement du cours à Jupyter Lab.
- Installer et utiliser `google-adk` et `python-dotenv`.
- Configurer une clé API Google avec un fichier local `.env`.
- Créer un Agent simple avec Google ADK.
- Ajouter Google Search comme outil pour les informations factuelles ou récentes.
- Ajouter une fonction Python personnalisée comme outil d'Agent.
- Comprendre le principe d'un pipeline multi-agent séquentiel.

### Structure du Projet

```text
.
├── Instruction.ipynb
├── my_agent_project/
│   ├── __init__.py
│   └── agent.py
└── Sequential_agent/
    ├── __init__.py
    └── agent.py
```

### Fichiers Principaux

#### `Instruction.ipynb`

Ce notebook est le guide principal du cours. Il accompagne les étudiants dans les étapes suivantes :

1. Créer l'environnement conda `agent_env`.
2. Ajouter cet environnement à Jupyter Lab.
3. Installer les packages nécessaires.
4. Créer un fichier `.env`.
5. Vérifier que `GOOGLE_API_KEY` est disponible.
6. Construire un Agent de base.
7. Ajouter Google Search à un Agent.
8. Ajouter une fonction personnalisée comme outil.
9. Tester des instructions de prompt plus détaillées.

#### `my_agent_project/agent.py`

Ce fichier contient un exemple d'Agent unique nommé `search_helper`. Il utilise le modèle `gemini-2.5-flash` et l'outil `google_search`.

Cet exemple montre comment :

- Définir un `root_agent`.
- Rédiger des instructions claires pour l'Agent.
- Utiliser la recherche lorsqu'une question demande des informations récentes, une vérification factuelle ou une évaluation de restaurant.

#### `Sequential_agent/agent.py`

Ce fichier contient un exemple multi-agent séquentiel avec `SequentialAgent`.

Le flux est divisé en trois agents :

- `research_agent` : collecte les faits principaux et retourne un JSON structuré.
- `outline_agent` : transforme le JSON en titre et en plan à puces.
- `final_agent` : rédige une réponse finale courte à partir du plan.

Cet exemple permet d'expliquer comment une tâche complexe peut être divisée en étapes plus simples confiées à plusieurs agents.

### Configuration de l'Environnement

Créer et activer l'environnement conda :

```bash
conda create -n agent_env python=3.11
conda activate agent_env
```

Installer le kernel Jupyter :

```bash
pip install ipykernel
python -m ipykernel install --user --name agent_env --display-name "agent_env"
```

Installer les packages nécessaires :

```bash
pip install google-adk python-dotenv
```

### Clé API Google

Créer un fichier `.env` dans le dossier du projet :

```bash
vi .env
```

Ajouter la ligne suivante :

```text
GOOGLE_API_KEY=Your key
```

Ne publiez pas votre vraie clé API sur GitHub.

Vous pouvez tester la configuration dans le notebook :

```python
import os
from dotenv import load_dotenv

load_dotenv(".env")
print(os.getenv("GOOGLE_API_KEY") is not None)
```

Si la sortie est `True`, la clé API a été chargée correctement.

### Exécuter l'Agent

Depuis le dossier parent qui contient le projet d'Agent, lancer :

```bash
adk web
```

Ouvrir ensuite l'interface ADK Web dans le navigateur et sélectionner l'Agent à tester.

### Déroulement Suggéré du Cours

1. Préparer l'environnement Python et Jupyter.
2. Lancer un Agent simple et expliquer `name`, `model` et `instruction`.
3. Ajouter Google Search et comparer les réponses avec et sans recherche.
4. Ajouter une fonction personnalisée comme outil.
5. Modifier les prompts et observer l'effet des instructions sur le comportement de l'Agent.
6. Présenter `SequentialAgent` et expliquer la collaboration multi-agent par étapes.

### Exercices Pour les Étudiants

- Demander à l'Agent de base d'expliquer les AI Agents en une phrase.
- Demander à l'Agent avec recherche de trouver une actualité récente sur l'IA et de la résumer.
- Donner un nom de restaurant à l'Agent et demander son classement ainsi que des commentaires détaillés.
- Modifier une fonction personnalisée afin que l'Agent retourne des informations sur le cours, l'école ou la classe.
- Adapter le pipeline séquentiel pour rechercher un sujet et produire un court résumé.

### Remarques

- Le fichier `.env` doit rester local car il contient des identifiants privés.
- Si la recherche ne fonctionne pas, vérifier que la clé API Google est correctement configurée.
- Si Jupyter Lab n'affiche pas `agent_env`, relancer la commande d'installation du kernel.
- Si `adk web` ne trouve pas l'Agent, vérifier que `agent.py` définit bien `root_agent`.
