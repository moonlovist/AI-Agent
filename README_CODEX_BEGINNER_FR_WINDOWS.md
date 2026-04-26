# Guide Débutant Windows : Commencer avec Codex, Exécuter un Premier Agent, Puis Utiliser Streamlit

Ce guide est écrit pour vous si :

- vous utilisez Windows
- vous débutez avec Git et GitHub
- vous débutez avec le terminal
- vous débutez avec Python
- votre ordinateur n'est pas très puissant
- vous voulez avancer étape par étape sans vous perdre

Le but de ce guide est simple :

1. installer seulement les outils nécessaires
2. installer Codex
3. télécharger le projet depuis GitHub
4. exécuter un premier agent simple
5. créer les fichiers `.env` au bon endroit
6. exécuter ensuite le modèle Streamlit
7. faire de petites modifications sans casser le projet

Ce guide est écrit pour des débutants. Vous n'avez pas besoin de tout comprendre au début. Vous devez seulement suivre les étapes dans l'ordre.

## 1. Comprendre l'ordre de travail

Vous ne devez pas commencer directement par Streamlit.

Vous devez apprendre dans cet ordre :

1. `my_agent_project`
2. `Sequential_agent_streamlit_template`

Cet ordre est important parce que :

- `my_agent_project` est plus simple
- il demande moins d'effort à votre ordinateur
- il vous permet de comprendre ce qu'est un agent avant d'ajouter une interface plus complexe

## 2. Comprendre les deux étapes du projet

### Étape 1 : un agent simple

Vous commencerez par :

```text
my_agent_project
```

Ce dossier vous aide à comprendre :

- ce qu'est un dossier d'agent
- à quoi sert `agent.py`
- pourquoi un fichier `.env` est nécessaire
- comment lancer `adk web`

### Étape 2 : une interface Streamlit

Ensuite, vous passerez à :

```text
Sequential_agent_streamlit_template
```

Ce dossier vous aide à comprendre :

- comment afficher une interface visible
- comment changer la mise en page
- comment modifier des boutons, onglets, colonnes et champs texte
- comment séparer le frontend de la logique de l'agent

## 3. Installer Git

Vous devez installer Git d'abord parce que Git sert à télécharger le projet depuis GitHub.

Sans Git, vous pouvez télécharger un ZIP, mais cela rend la suite plus difficile, surtout si vous devez mettre à jour le projet ou envoyer vos changements plus tard.

### 3.1 Vérifier si Git est déjà installé

Ouvrez **Invite de commandes**, **PowerShell**, ou **Git Bash**.

Tapez :

```bat
git --version
```

Si Git est installé, vous verrez une version.

Si ce n'est pas le cas, installez Git ici :

- https://git-scm.com/download/win

Pendant l'installation, les options par défaut sont généralement suffisantes.

Après l'installation, fermez la fenêtre de terminal, ouvrez-en une nouvelle, puis vérifiez encore :

```bat
git --version
```

## 4. Installer Python 3.11

Vous devez installer Python parce que ce projet est un projet Python.

Pour un ordinateur peu puissant, vous devez éviter d'installer trop d'outils lourds si ce n'est pas nécessaire. Ici, nous utilisons simplement Python et un environnement virtuel léger.

### 4.1 Vérifier si Python est déjà installé

Dans le terminal, tapez :

```bat
python --version
```

Si cela ne marche pas, essayez :

```bat
python3 --version
```

Si vous avez une version 3.11, vous pouvez continuer.

Sinon, installez Python 3.11 depuis :

- https://www.python.org/downloads/windows/

Pendant l'installation, cochez bien :

```text
Add Python to PATH
```

Après l'installation, fermez le terminal, ouvrez-en un nouveau, puis vérifiez :

```bat
python --version
```

## 5. Installer Node.js

Vous devez installer Node.js parce que Codex CLI s'installe avec `npm`.

Sans Node.js, vous ne pourrez pas installer Codex.

### 5.1 Vérifier si Node.js est déjà installé

Tapez :

```bat
node --version
npm --version
```

Si les deux commandes affichent un numéro de version, vous pouvez continuer.

Sinon, installez Node.js ici :

- https://nodejs.org/

Après l'installation, fermez le terminal, ouvrez-en un nouveau, puis vérifiez encore :

```bat
node --version
npm --version
```

## 6. Installer Codex CLI

Vous devez installer Codex tôt, même si vous n'allez pas l'utiliser tout de suite.

Pourquoi :

- Codex peut expliquer les fichiers du projet
- Codex peut vous aider à faire de petites modifications
- Codex peut vous éviter de vous bloquer sur une erreur simple

Installez Codex :

```bat
npm install -g @openai/codex
```

Puis vérifiez :

```bat
codex --version
```

Si vous voyez `command not found` ou un message similaire, fermez le terminal, ouvrez-en un nouveau, puis essayez encore.

## 7. Vous connecter à Codex

Vous devez vous connecter avant de commencer à travailler, pour éviter de perdre du temps plus tard.

Tapez :

```bat
codex --login
```

Puis suivez les étapes dans le navigateur.

## 8. Apprendre les commandes les plus simples

Avant de télécharger le projet, vous devez comprendre quelques commandes très simples.

Vous n'avez pas besoin d'en connaître beaucoup au début.

### `cd`

Cette commande sert à entrer dans un dossier.

Exemple :

```bat
cd Documents
```

### `cd ..`

Cette commande sert à remonter d'un dossier.

```bat
cd ..
```

### `dir`

Sous Windows, `dir` sert à voir les fichiers et dossiers du répertoire courant.

```bat
dir
```

### `mkdir`

Cette commande sert à créer un dossier.

```bat
mkdir mon_dossier
```

## 9. Télécharger le projet depuis GitHub

Vous devez télécharger le projet avec `git clone`, parce que cela crée une vraie copie du dépôt sur votre ordinateur.

Ouvrez **Invite de commandes** ou **PowerShell**.

Placez-vous dans un dossier simple, par exemple `Documents` :

```bat
cd %USERPROFILE%\Documents
```

Vous pouvez vérifier ce qu'il y a dans le dossier :

```bat
dir
```

Clonez ensuite le dépôt :

```bat
git clone https://github.com/moonlovist/AI-Agent.git
```

Entrez dans le dossier du projet :

```bat
cd AI-Agent
```

Vérifiez le contenu :

```bat
dir
```

Vous devriez voir des dossiers comme :

```text
my_agent_project
Sequential_agent
Sequential_agent_improved
Sequential_agent_streamlit_template
```

## 10. Ouvrir le projet avec Codex

Vous devez maintenant ouvrir le projet avec Codex pour commencer à comprendre ce qui se trouve dans le dépôt.

Depuis le dossier `AI-Agent`, tapez :

```bat
codex
```

Vous pouvez poser des questions simples comme :

```text
Explain the structure of this repository in simple words.
```

```text
What is inside my_agent_project?
```

```text
Which file controls the Streamlit layout?
```

À ce stade, vous devez surtout utiliser Codex pour comprendre le projet.

## 11. Créer un environnement Python léger

Vous devez créer un environnement virtuel, parce que cela évite de mélanger ce projet avec d'autres installations Python.

Pour un ordinateur peu puissant, c'est une bonne solution : c'est plus léger qu'un outil plus grand comme Anaconda.

Depuis le dossier `AI-Agent`, tapez :

```bat
python -m venv .venv
```

Cela crée un dossier `.venv`.

Activez-le :

```bat
.venv\Scripts\activate
```

Si cela fonctionne, vous verrez souvent :

```text
(.venv)
```

au début de la ligne du terminal.

## 12. Installer les packages Python nécessaires

Vous devez installer seulement les packages nécessaires.

Sur un ordinateur peu puissant, il vaut mieux éviter d'ajouter des outils inutiles.

D'abord, mettez `pip` à jour :

```bat
python -m pip install --upgrade pip
```

Ensuite, installez les packages nécessaires pour le premier agent et pour Streamlit :

```bat
pip install google-adk python-dotenv streamlit google-genai
```

Si cette installation prend du temps, soyez patient. Sur un ordinateur lent, c'est normal.

## 13. Exécuter votre premier agent simple : `my_agent_project`

Vous devez commencer par `my_agent_project`, parce que c'est l'exemple le plus simple du dépôt.

### 13.1 Regarder le contenu du dossier

Tapez :

```bat
dir my_agent_project
```

Vous devriez voir des fichiers comme :

```text
__init__.py
agent.py
```

Le fichier important est :

```text
my_agent_project\agent.py
```

### 13.2 Créer le fichier `.env` pour `my_agent_project`

Vous devez créer ce fichier, parce que l'agent a besoin de votre clé API Google.

Pour ce premier agent, le fichier `.env` doit être ici :

```text
my_agent_project\.env
```

Le moyen le plus simple sous Windows est :

```bat
notepad my_agent_project\.env
```

Quand Notepad demande si vous voulez créer le fichier, cliquez sur **Yes**.

Ajoutez cette ligne :

```text
GOOGLE_API_KEY=your_key_here
```

Remplacez `your_key_here` par votre vraie clé.

Attention :

- le fichier doit s'appeler `.env`
- il ne doit pas s'appeler `.env.txt`

### 13.3 Comprendre pourquoi l'emplacement du `.env` est important

Vous devez bien retenir cette règle :

- pour `my_agent_project`, le fichier doit être `my_agent_project\.env`
- pour le modèle Streamlit, le fichier sera plus tard `.env` à la racine du projet

Si le fichier est au mauvais endroit, le projet peut démarrer mais échouer quand il essaie d'appeler le modèle.

### 13.4 Lancer le premier agent avec ADK

Vous devez lancer le premier agent avec ADK, parce que c'est le moyen le plus simple de voir un agent fonctionner.

Depuis le dossier `AI-Agent`, tapez :

```bat
adk web
```

Si cela ne marche pas, essayez :

```bat
python -m adk web
```

Ouvrez ensuite l'adresse locale affichée dans le terminal.

Dans l'interface ADK, vous devriez pouvoir sélectionner :

```text
my_agent_project
```

### 13.5 Que tester dans le premier agent

Commencez par quelque chose de très simple :

```text
Explain AI agents in one sentence.
```

Puis essayez :

```text
Tell me about a recent AI news item.
```

Quand vous avez terminé, arrêtez l'application avec :

```text
Ctrl+C
```

## 14. Créer le fichier `.env` à la racine pour Streamlit

Vous devez créer un second fichier `.env`, parce que le modèle Streamlit lit la clé API à la racine du projet.

Pour Streamlit, le fichier doit être ici :

```text
.env
```

Le moyen le plus simple est :

```bat
notepad .env
```

Ajoutez :

```text
GOOGLE_API_KEY=your_key_here
```

Remplacez `your_key_here` par votre vraie clé.

Ne supposez pas que `my_agent_project\.env` sera utilisé automatiquement par Streamlit. Ce n'est pas le cas ici.

## 15. Lancer le modèle Streamlit

Vous devez lancer Streamlit seulement après avoir compris l'agent simple.

Depuis le dossier `AI-Agent`, avec l'environnement activé, tapez :

```bat
streamlit run Sequential_agent_streamlit_template/app.py
```

Après quelques secondes, le terminal affichera une adresse locale, souvent :

```text
http://localhost:8501
```

Ouvrez cette adresse dans votre navigateur.

Si l'application semble lente, c'est normal sur un ordinateur peu puissant. Attendez quelques secondes après chaque action.

## 16. Comprendre quel fichier modifier

Avant de modifier quoi que ce soit, vous devez savoir quel fichier contrôle quoi.

### Pour changer l'interface visible

Modifiez :

```text
Sequential_agent_streamlit_template\app.py
```

Ce fichier contrôle :

- le titre
- la barre latérale
- les boutons
- les colonnes
- les onglets
- les champs texte
- les résultats affichés

### Pour changer la logique de l'agent

Modifiez :

```text
Sequential_agent_streamlit_template\pipeline.py
```

Ce fichier contrôle :

- les étapes du pipeline
- les prompts
- le modèle
- la réponse finale

## 17. Faire votre première petite modification de frontend

Vous devez commencer par une petite modification visible.

Ne commencez pas par une grande refonte.

### Exemple 1 : changer le titre de la page

Dans `Sequential_agent_streamlit_template\app.py`, trouvez :

```python
page_title="Sequential Agent Template",
```

et changez-le en :

```python
page_title="My Classroom Agent",
```

Enregistrez, puis revenez au navigateur.

### Exemple 2 : changer le titre de la barre latérale

Trouvez :

```python
st.title("🧩 Sequential Agent")
```

et changez-le en :

```python
st.title("🧩 My First Agent")
```

## 18. Faire une modification un peu plus importante

Quand vous êtes à l'aise avec les changements de texte, vous pouvez modifier un peu la structure.

### Exemple 1 : ajouter un onglet

Dans `app.py`, trouvez :

```python
tab1, tab2, tab3 = st.tabs(["Intermediate Steps", "History", "Raw Data"])
```

et changez-le en :

```python
tab1, tab2, tab3, tab4 = st.tabs(
    ["Intermediate Steps", "History", "Raw Data", "Notes"]
)
```

Puis ajoutez :

```python
with tab4:
    st.write("Students can add their own notes here.")
```

### Exemple 2 : rendre les deux colonnes égales

Trouvez :

```python
left, right = st.columns([1.2, 0.8], gap="large")
```

et changez-le en :

```python
left, right = st.columns([1, 1], gap="large")
```

## 19. Utiliser Codex pour vous aider

Vous devez utiliser Codex pour une seule petite tâche à la fois.

Sur un ordinateur peu puissant, il vaut mieux aussi éviter de lancer trop de choses compliquées d'un seul coup.

Depuis le dossier `AI-Agent`, vous pouvez lancer :

```bat
codex
```

Puis demander par exemple :

```text
In Sequential_agent_streamlit_template/app.py, change the sidebar title to "My First AI Agent App" and explain what you changed.
```

Ou :

```text
Add one new tab called Notes in the Streamlit app.
```

## 20. Enregistrer vos changements avec Git

Vous devez enregistrer vos changements avec Git, pour garder une trace de ce que vous avez modifié.

Vérifiez d'abord ce qui a changé :

```bat
git status
```

Ajoutez ensuite les fichiers modifiés :

```bat
git add .
```

Créez ensuite un commit :

```bat
git commit -m "Update Streamlit layout"
```

Si vous avez votre propre dépôt GitHub, vous pouvez ensuite envoyer les changements :

```bat
git push
```

## 21. Problèmes fréquents

### `command not found: codex`

Essayez :

```bat
npm install -g @openai/codex
```

puis :

```bat
codex --version
```

### `command not found: streamlit`

Réactivez l'environnement :

```bat
.venv\Scripts\activate
```

Puis relancez :

```bat
streamlit run Sequential_agent_streamlit_template/app.py
```

### `command not found: adk`

Essayez :

```bat
pip install google-adk
```

Puis :

```bat
adk web
```

### Le fichier `.env` devient `.env.txt`

Sous Windows, cela arrive souvent.

Pour éviter ce problème, utilisez toujours :

```bat
notepad my_agent_project\.env
```

ou :

```bat
notepad .env
```

### Le projet est lent

Si votre ordinateur est lent :

- ne laissez pas trop de programmes ouverts
- commencez par `my_agent_project`
- attendez quelques secondes entre les actions
- utilisez de petites modifications au lieu de gros changements

### `503 UNAVAILABLE`

Cela signifie généralement que le modèle est temporairement surchargé.

Essayez :

- de relancer la requête
- de changer de modèle dans la barre latérale
- d'attendre un peu

## 22. Un ordre réaliste pour un débutant sous Windows

Vous devriez travailler dans cet ordre :

1. installer Git
2. installer Python
3. installer Node.js
4. installer Codex
5. faire `git clone`
6. créer `.venv`
7. activer `.venv`
8. installer les packages Python
9. créer `my_agent_project\.env`
10. lancer `adk web`
11. tester `my_agent_project`
12. créer `.env` à la racine
13. lancer Streamlit
14. modifier un petit texte dans `app.py`
15. demander une petite aide à Codex

## 23. Une session complète d'exemple

Vous pouvez suivre exactement cette suite de commandes.

```bat
cd %USERPROFILE%\Documents
git clone https://github.com/moonlovist/AI-Agent.git
cd AI-Agent
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install google-adk python-dotenv streamlit google-genai
notepad my_agent_project\.env
adk web
```

Après le test du premier agent, arrêtez avec `Ctrl+C`, puis continuez :

```bat
notepad .env
streamlit run Sequential_agent_streamlit_template/app.py
```

## 24. Concentrez-vous seulement sur les fichiers importants

Au début, vous ne devez pas essayer de comprendre tout le dépôt.

Pour le premier agent simple, concentrez-vous sur :

- `my_agent_project\agent.py`
- `my_agent_project\.env`

Pour le modèle Streamlit, concentrez-vous sur :

- `Sequential_agent_streamlit_template\app.py`
- `Sequential_agent_streamlit_template\pipeline.py`
- `.env`

Cela suffit pour commencer.
