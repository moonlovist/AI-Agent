# Guide Débutant : Commencer avec Codex, Exécuter Votre Premier Agent, Puis Construire une Interface Streamlit

Ce guide est écrit pour vous si vous débutez avec :

- Git et GitHub
- les commandes de terminal
- les commandes shell
- les environnements Python
- les projets d'AI agents
- l'édition d'interfaces Streamlit

Vous n'avez pas besoin de tout comprendre au début. Vous devez simplement suivre les étapes dans l'ordre.

L'objectif de ce guide est de vous aider à :

1. installer les outils de base
2. installer Codex
3. télécharger ce projet depuis GitHub
4. exécuter votre premier agent simple : `my_agent_project`
5. créer le bon fichier `.env` au bon endroit
6. exécuter le modèle d'agent Streamlit
7. faire de petites modifications de frontend
8. utiliser Codex pour vous aider à modifier le projet

Vous devriez apprendre dans cet ordre :

1. `my_agent_project`
2. `Sequential_agent_streamlit_template`

Cet ordre est important, car le modèle Streamlit est plus facile à comprendre après avoir déjà vu un exemple d'agent plus simple.

## 1. Comprendre le parcours d'apprentissage

Avant d'installer quoi que ce soit, vous devez comprendre que ce guide comporte deux étapes.

### Étape 1 : exécuter un agent simple

Vous allez commencer par :

```text
my_agent_project
```

Vous devez commencer par ce dossier, car c'est l'exemple d'agent le plus simple du dépôt.

Il vous aide à apprendre :

- à quoi ressemble un dossier d'agent
- à quoi sert `agent.py`
- ce que signifie `root_agent`
- pourquoi un fichier `.env` local est nécessaire
- comment fonctionne `adk web`

### Étape 2 : exécuter une interface Streamlit

Ensuite, vous passerez à :

```text
Sequential_agent_streamlit_template
```

Vous devez passer à ce dossier en second, car il ajoute une interface frontend au-dessus de l'idée de base de l'agent.

Il vous aide à apprendre :

- comment construire une interface visible
- comment séparer l'interface utilisateur de la logique
- comment modifier des onglets, colonnes, boutons et champs de saisie
- comment fonctionne un pipeline en plusieurs étapes

## 2. Comprendre les deux fichiers Streamlit les plus importants

Plus tard dans le guide, lorsque vous travaillerez avec le modèle Streamlit, vous n'aurez besoin de retenir que ces deux fichiers :

- `Sequential_agent_streamlit_template/app.py`
- `Sequential_agent_streamlit_template/pipeline.py`

Vous devez les utiliser ainsi :

- modifiez `app.py` lorsque vous voulez changer la mise en page, la barre latérale, les boutons, les champs de texte, les onglets et les résultats affichés
- modifiez `pipeline.py` lorsque vous voulez changer les prompts, la séquence des étapes, le modèle et le comportement de la réponse finale

Ce point est important, car beaucoup de débutants modifient le mauvais fichier et ne comprennent ensuite pas pourquoi la page n'a pas changé.

## 3. Installer Git

Vous devez installer Git en premier, car Git est l'outil que vous utiliserez pour télécharger le projet depuis GitHub et enregistrer vos propres modifications plus tard.

Sans Git, vous pouvez toujours télécharger un fichier ZIP, mais cela rend beaucoup plus difficile la mise à jour du projet, le suivi de vos modifications et l'envoi de votre travail vers GitHub.

Commencez par vérifier si Git est déjà installé :

```bash
git --version
```

Si Git est installé, vous verrez un numéro de version, par exemple :

```text
git version 2.xx.x
```

Si vous obtenez une erreur à la place, installez Git :

- macOS : installez Xcode Command Line Tools ou Git depuis https://git-scm.com/

Après l'installation, exécutez à nouveau la commande :

```bash
git --version
```

Vous devez toujours vérifier qu'une installation a bien fonctionné avant de passer à l'étape suivante.

## 4. Installer Python 3.11

Vous devez installer Python parce que ce projet est un projet Python. Les agents, l'application Streamlit et les packages associés fonctionnent tous avec Python.

Vous devriez essayer d'utiliser Python 3.11, car c'est une version sûre pour ce dépôt.

Vérifiez si Python est déjà disponible :

```bash
python3 --version
```

Si Python est installé, vous verrez quelque chose comme :

```text
Python 3.11.x
```

Si vous n'avez pas Python 3.11, installez-le avant de continuer.

Après l'installation, vérifiez de nouveau :

```bash
python3 --version
```

## 5. Installer Node.js

Vous devez installer Node.js parce que Codex CLI s'installe avec `npm`, et `npm` est fourni avec Node.js.

Si Node.js manque, vous ne pourrez pas installer Codex depuis le terminal.

Vérifiez si Node.js et npm sont disponibles :

```bash
node --version
npm --version
```

Si les deux commandes affichent un numéro de version, vous pouvez continuer.

Sinon, installez Node.js depuis :

- https://nodejs.org/

Puis vérifiez de nouveau :

```bash
node --version
npm --version
```

## 6. Installer Codex CLI

Vous devez installer Codex assez tôt, car il peut vous aider à explorer le dépôt, expliquer les fichiers et faire de petites modifications pendant que vous apprenez encore les commandes de base.

Cela en fait un bon assistant pédagogique, surtout si vous n'êtes pas encore à l'aise avec la lecture du code.

Installez Codex :

```bash
npm install -g @openai/codex
```

Vérifiez ensuite que Codex a bien été installé :

```bash
codex --version
```

Si cette commande fonctionne, l'installation est terminée.

Si vous voyez `command not found: codex`, l'installation ne s'est pas terminée correctement ou votre shell ne trouve pas encore la commande installée.

## 7. Se connecter à Codex

Vous devez vous connecter avant de commencer le projet afin que Codex soit prêt quand vous en aurez besoin.

Exécutez :

```bash
codex --login
```

Puis suivez les étapes de connexion dans le navigateur.

Quand c'est terminé, revenez au terminal.

Vous n'avez pas besoin de commencer à utiliser Codex immédiatement. Le plus important est que l'outil soit prêt.

## 8. Apprendre les commandes de terminal les plus simples

Avant de télécharger le projet, vous devez apprendre quelques commandes qui permettent de vous déplacer dans le système de fichiers.

Vous n'avez pas besoin de mémoriser beaucoup de commandes. Au début, celles-ci suffisent.

### `pwd`

Vous devez utiliser `pwd` quand vous voulez savoir où vous êtes.

```bash
pwd
```

Cette commande affiche votre dossier courant.

### `ls`

Vous devez utiliser `ls` quand vous voulez voir ce qu'il y a dans le dossier courant.

```bash
ls
```

Cette commande liste les fichiers et les dossiers.

### `cd`

Vous devez utiliser `cd` quand vous voulez entrer dans un autre dossier.

```bash
cd nom_du_dossier
```

Exemple :

```bash
cd AI-Agent
```

### `cd ..`

Vous devez utiliser `cd ..` quand vous voulez remonter d'un niveau.

```bash
cd ..
```

### `mkdir`

Vous devez utiliser `mkdir` quand vous voulez créer un nouveau dossier.

```bash
mkdir mon_dossier
```

Ces commandes peuvent paraître simples, mais elles sont la base de tout ce que vous ferez ensuite dans le terminal.

## 9. Télécharger le projet depuis GitHub

Vous devez télécharger le projet avec `git clone`, car cela vous donne le dépôt complet et le garde connecté à GitHub.

C'est bien mieux que de copier les fichiers à la main.

Ouvrez d'abord le Terminal.

Déplacez-vous ensuite dans un dossier où vous voulez conserver le projet.

Par exemple :

```bash
cd ~/Documents
```

Avant de cloner, vérifiez où vous êtes :

```bash
pwd
```

Puis clonez le dépôt :

```bash
git clone https://github.com/moonlovist/AI-Agent.git
```

Cette commande crée un nouveau dossier appelé `AI-Agent`.

Entrez maintenant dans ce dossier :

```bash
cd AI-Agent
```

Vérifiez le contenu :

```bash
ls
```

Vous devriez voir des dossiers comme :

```text
my_agent_project
Sequential_agent
Sequential_agent_improved
Sequential_agent_streamlit_template
```

Si vous ne les voyez pas, vous êtes probablement dans le mauvais dossier.

## 10. Ouvrir le projet dans Codex

Vous devez ouvrir le projet dans Codex maintenant, car c'est le moment où vous commencez à lire le dépôt, et Codex peut vous aider à en expliquer la structure en langage simple.

Commencez par vérifier que vous êtes bien à la racine du dépôt :

```bash
pwd
ls
```

Puis lancez Codex :

```bash
codex
```

Une fois Codex ouvert, vous pouvez poser des questions simples comme :

```text
Explain the structure of this repository in simple words.
```

```text
What is inside my_agent_project?
```

```text
Which file controls the Streamlit layout?
```

```text
Show me the difference between app.py and pipeline.py.
```

À ce stade, vous devez surtout utiliser Codex pour comprendre le projet, pas pour tout redessiner.

## 11. Créer un environnement Python

Vous devez créer un environnement virtuel Python parce qu'il garde les packages de ce projet séparés du reste de votre ordinateur.

Sans environnement virtuel, différents projets peuvent interférer entre eux, surtout s'ils ont besoin de versions différentes des mêmes packages.

Depuis la racine du dépôt, créez l'environnement :

```bash
python3 -m venv .venv
```

Cela crée un dossier caché appelé `.venv`.

Activez-le maintenant :

```bash
source .venv/bin/activate
```

Après activation, votre terminal affiche généralement quelque chose comme :

```text
(.venv)
```

Ce repère visuel est important. Il vous indique que vous utilisez bien l'environnement local du projet.

## 12. Installer les packages Python

Vous devez installer les packages nécessaires seulement après avoir activé l'environnement virtuel.

Ainsi, les packages sont installés dans l'environnement du projet et non dans votre installation globale de Python.

Commencez par mettre `pip` à jour :

```bash
pip install --upgrade pip
```

Installez ensuite les packages nécessaires à la fois pour le premier agent simple et pour le modèle Streamlit :

```bash
pip install google-adk python-dotenv streamlit google-genai
```

Si vous voulez également utiliser des notebooks Jupyter :

```bash
pip install jupyter ipykernel
```

Quand vous apprenez, vous devez installer les packages étape par étape. Cela vous aide à repérer plus facilement l'étape qui a échoué en cas de problème.

## 13. Exécuter votre premier agent simple : `my_agent_project`

Vous devez commencer avec `my_agent_project`, car c'est l'exemple fonctionnel le plus simple de ce dépôt.

Il vous apprend la structure de base d'un agent avant que vous n'ajoutiez une interface personnalisée.

### 13.1 Regarder le contenu du dossier

Vous devez d'abord regarder le dossier pour que l'exemple soit concret.

Exécutez :

```bash
ls my_agent_project
```

Vous devriez voir des fichiers comme :

```text
__init__.py
agent.py
```

Le fichier important est :

```text
my_agent_project/agent.py
```

C'est ce fichier qui définit l'agent.

### 13.2 Créer le fichier `.env` pour `my_agent_project`

Vous devez créer un fichier `.env` pour ce premier agent, car l'agent a besoin d'accéder à votre clé API Google.

C'est un point qui embrouille souvent les débutants. L'emplacement du fichier `.env` est important.

Pour ce premier agent simple, créez le fichier `.env` ici :

```text
my_agent_project/.env
```

Créez-le avec :

```bash
touch my_agent_project/.env
```

Ouvrez ensuite ce fichier dans un éditeur de texte et ajoutez :

```text
GOOGLE_API_KEY=your_key_here
```

Remplacez `your_key_here` par votre vraie clé.

Le nom du fichier doit être exactement `.env`.

### 13.3 Comprendre pourquoi l'emplacement du `.env` est important

Vous devez bien comprendre cette règle :

- si vous exécutez `my_agent_project`, mettez la clé dans `my_agent_project/.env`
- si vous exécutez ensuite le modèle Streamlit, mettez la clé dans `.env` à la racine du dépôt

Si vous placez la clé au mauvais endroit, l'application peut démarrer, mais l'appel au modèle échouera plus tard.

### 13.4 Exécuter le premier agent avec ADK

Vous devez exécuter le premier agent avec ADK, car c'est la manière la plus simple de voir comment un dossier d'agent basique devient une application fonctionnelle.

Vérifiez que vous êtes toujours à la racine du dépôt :

```bash
pwd
ls
```

Exécutez ensuite :

```bash
adk web
```

Si `adk` n'est pas trouvé, essayez :

```bash
python -m adk web
```

Ouvrez ensuite l'adresse locale affichée dans le terminal.

Dans la page ADK, vous devriez pouvoir sélectionner :

```text
my_agent_project
```

### 13.5 Que tester dans le premier agent

Vous devez commencer par tester une question très simple.

Par exemple :

```text
Explain AI agents in one sentence.
```

Puis essayez une question qui peut utiliser la recherche :

```text
Tell me about a recent AI news item.
```

Cela vous aide à comprendre ce que ce premier agent peut faire avant de passer au modèle plus complexe.

Quand vous avez terminé, arrêtez ADK dans le terminal avec :

```text
Ctrl+C
```

## 14. Créer le fichier `.env` à la racine pour le modèle Streamlit

Vous devez créer un second fichier `.env` avant d'exécuter le modèle Streamlit, car ce modèle lit la clé API à la racine du dépôt.

Cet emplacement est différent de `my_agent_project/.env`.

Pour le modèle Streamlit, créez :

```text
.env
```

Depuis la racine du dépôt, exécutez :

```bash
touch .env
```

Ouvrez ce fichier dans un éditeur de texte et ajoutez :

```text
GOOGLE_API_KEY=your_key_here
```

Remplacez `your_key_here` par votre vraie clé.

Si vous avez déjà créé `my_agent_project/.env`, ne supposez pas que le modèle Streamlit l'utilisera automatiquement.

## 15. Exécuter le modèle Streamlit

Vous devez maintenant exécuter l'application, car une fois le projet ouvert dans le navigateur, vous pouvez enfin relier le code à une interface visible après avoir déjà compris l'agent plus simple.

Depuis la racine du dépôt, pendant que l'environnement virtuel est toujours actif, exécutez :

```bash
streamlit run Sequential_agent_streamlit_template/app.py
```

Après quelques secondes, le terminal affichera une adresse locale, en général :

```text
http://localhost:8501
```

Ouvrez cette adresse dans votre navigateur.

Si la page s'ouvre, l'application fonctionne correctement.

## 16. Comprendre exactement quel fichier modifier

Avant de modifier quoi que ce soit, vous devez décider si vous voulez changer :

- la page visible
- le comportement de l'agent

Ce point est important, car les débutants modifient souvent le mauvais fichier et pensent ensuite que rien ne fonctionne.

### Si vous voulez changer la page visible

Vous devez modifier :

```text
Sequential_agent_streamlit_template/app.py
```

Ce fichier contrôle :

- le titre de la page
- la barre latérale
- les boutons
- les champs de texte
- les onglets
- les colonnes
- les résultats affichés
- l'historique affiché

### Si vous voulez changer le fonctionnement de l'agent

Vous devez modifier :

```text
Sequential_agent_streamlit_template/pipeline.py
```

Ce fichier contrôle :

- l'étape de recherche
- l'étape de plan
- l'étape de brouillon
- l'étape de relecture
- l'étape de réponse finale
- le nom du modèle
- les instructions des prompts
- le comportement de parsing JSON

## 17. Faire votre première modification de frontend

Vous devez commencer par une très petite modification de frontend, car cela vous donne un premier succès rapide et vous aide à comprendre où la mise en page est contrôlée.

Ne commencez pas par une refonte complète.

### Exemple 1 : changer le titre de la page

Ouvrez :

```text
Sequential_agent_streamlit_template/app.py
```

Trouvez ce code :

```python
st.set_page_config(
    page_title="Sequential Agent Template",
```

Changez-le en :

```python
st.set_page_config(
    page_title="My Classroom Agent",
```

Enregistrez le fichier.

Revenez ensuite au navigateur. Streamlit recharge généralement la page automatiquement. Sinon, rafraîchissez la page.

### Exemple 2 : changer le titre de la barre latérale

Trouvez :

```python
st.title("🧩 Sequential Agent")
```

Changez-le en :

```python
st.title("🧩 My First Agent")
```

Enregistrez le fichier et vérifiez de nouveau la page.

### Exemple 3 : changer le texte d'aide

Trouvez une ligne comme :

```python
st.caption("Students can change the layout here without touching the core pipeline.")
```

Remplacez-la par un texte plus simple, adapté à votre cours.

C'est un bon exercice pour débuter, car il vous permet de voir exactement où apparaissent les petites modifications de texte de l'interface.

## 18. Faire une modification de frontend un peu plus importante

Une fois que vous êtes à l'aise avec les modifications de texte, vous devez essayer une modification de structure.

Cela vous apprend que le travail frontend ne concerne pas seulement le texte, mais aussi la mise en page.

### Exemple 1 : ajouter un nouveau champ de texte

Dans `render_workspace()` à l'intérieur de `app.py`, ajoutez :

```python
course_name = st.text_input("Course name", value="AI Agent 101")
st.caption(f"Current course: {course_name}")
```

Cela vous apprend comment une entrée utilisateur apparaît sur la page.

### Exemple 2 : ajouter un nouvel onglet

Trouvez :

```python
tab1, tab2, tab3 = st.tabs(["Intermediate Steps", "History", "Raw Data"])
```

Changez-le en :

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

Cela vous apprend comment la page est divisée en sections.

### Exemple 3 : changer la largeur des colonnes

Trouvez :

```python
left, right = st.columns([1.2, 0.8], gap="large")
```

Changez-le en :

```python
left, right = st.columns([1, 1], gap="large")
```

Cela rend les zones de gauche et de droite de même largeur.

## 19. Changer le comportement de l'agent

Vous ne devriez modifier `pipeline.py` qu'après avoir un peu compris le frontend.

C'est parce que les changements de prompt sont moins visibles que les changements de mise en page, et les débutants les trouvent souvent plus difficiles à déboguer.

### Exemple 1 : rendre la réponse finale plus longue

Ouvrez :

```text
Sequential_agent_streamlit_template/pipeline.py
```

Trouvez une règle comme :

```text
Keep the answer under 220 words.
```

Changez-la en :

```text
Keep the answer under 400 words.
```

La réponse finale pourra alors être plus détaillée.

### Exemple 2 : rendre le ton plus formel

Trouvez le prompt final et ajoutez une formulation comme :

```text
Use a formal academic tone suitable for university teaching.
```

C'est une bonne manière d'apprendre comment les prompts changent le style des réponses.

## 20. Utiliser Codex pour vous aider avec de petites modifications

Vous devez utiliser Codex pour une seule petite tâche à la fois.

Ce point est important, car les débutants demandent souvent une refonte complète, puis ne comprennent plus ce qui a changé.

Un meilleur workflow est :

1. décider d'un petit changement
2. demander à Codex de faire ce seul changement
3. lire le fichier modifié
4. relancer l'application

Bons prompts pour Codex :

```text
In Sequential_agent_streamlit_template/app.py, change the sidebar title to "My First AI Agent App" and explain what you changed.
```

```text
Add one new tab called Notes in the Streamlit app.
```

```text
Make the left and right columns equal width.
```

```text
In pipeline.py, make the final answer more formal for classroom use.
```

Mauvais workflow débutant :

- demander à Codex de redessiner toute l'application d'un coup
- modifier le frontend et le pipeline en même temps
- faire beaucoup de changements avant de relancer l'application

## 21. Enregistrer vos modifications avec Git

Vous devez enregistrer vos modifications avec Git afin de garder un historique de ce que vous avez changé et pouvoir revenir en arrière si besoin.

Commencez par vérifier ce qui a changé :

```bash
git status
```

Ajoutez ensuite les fichiers modifiés :

```bash
git add .
```

Créez ensuite un commit :

```bash
git commit -m "Update Streamlit layout"
```

Si vous êtes connecté à votre propre dépôt GitHub, vous pouvez envoyer les modifications :

```bash
git push
```

Vous n'avez pas besoin de comprendre toutes les fonctionnalités de Git au début. Au départ, il suffit de comprendre :

- `git status` montre ce qui a changé
- `git add .` prépare les changements
- `git commit` enregistre un point de sauvegarde
- `git push` envoie ce point de sauvegarde vers GitHub

## 22. Résoudre les problèmes fréquents

Vous devez vous attendre à rencontrer des problèmes au début. C'est normal. Le plus important est de lire l'erreur et de corriger une seule chose à la fois.

### Problème : `command not found: codex`

Cela signifie généralement que Codex n'est pas installé correctement ou que votre shell ne le trouve pas.

Essayez de le réinstaller :

```bash
npm install -g @openai/codex
```

Puis vérifiez :

```bash
codex --version
```

### Problème : `command not found: streamlit`

Cela signifie généralement que votre environnement virtuel n'est pas actif.

Activez-le de nouveau :

```bash
source .venv/bin/activate
```

Puis exécutez :

```bash
streamlit run Sequential_agent_streamlit_template/app.py
```

### Problème : `command not found: adk`

Cela signifie généralement que `google-adk` n'est pas installé dans votre environnement virtuel.

Exécutez :

```bash
pip install google-adk
```

Puis essayez de nouveau :

```bash
adk web
```

### Problème : `ModuleNotFoundError`

Cela signifie généralement que les packages nécessaires ne sont pas installés.

Pour le modèle Streamlit, exécutez :

```bash
pip install streamlit python-dotenv google-genai
```

Pour l'agent ADK simple, si des packages manquent, exécutez :

```bash
pip install google-adk python-dotenv
```

### Problème : le modèle ne trouve pas votre clé API

Cela signifie généralement que votre fichier `.env` est au mauvais endroit.

Vérifiez bien ceci :

- pour l'agent simple : `my_agent_project/.env`
- pour le modèle Streamlit : `.env` à la racine du dépôt

### Problème : `503 UNAVAILABLE`

Cela signifie généralement que le modèle est temporairement surchargé.

Vous devez essayer l'une de ces actions :

- relancer la requête
- changer de modèle dans la barre latérale
- attendre une minute puis réessayer

### Problème : la page s'ouvre mais l'affichage est incorrect

Vous devez :

1. arrêter l'application avec `Ctrl+C`
2. enregistrer le fichier modifié
3. relancer l'application
4. lire attentivement la sortie du terminal

## 23. Un ordre d'apprentissage réaliste pour débuter

Vous devriez apprendre dans cet ordre :

1. `cd`, `ls`, `pwd`
2. `git clone`
3. `python3 -m venv .venv`
4. `source .venv/bin/activate`
5. `pip install ...`
6. créer `my_agent_project/.env`
7. exécuter `adk web`
8. tester `my_agent_project`
9. créer le `.env` à la racine
10. exécuter `streamlit run ...`
11. modifier du texte dans `app.py`
12. modifier la mise en page dans `app.py`
13. modifier les règles de prompt dans `pipeline.py`
14. demander à Codex une petite amélioration à la fois

Cet ordre fonctionne, car il va des tâches simples et visibles vers des tâches plus abstraites.

## 24. Une session complète d'exemple

Vous pouvez suivre exactement cette séquence.

Premier terminal :

```bash
cd ~/Documents
git clone https://github.com/moonlovist/AI-Agent.git
cd AI-Agent
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install google-adk python-dotenv streamlit google-genai
touch my_agent_project/.env
adk web
```

Après avoir testé `my_agent_project`, arrêtez l'application avec `Ctrl+C`.

Puis continuez :

```bash
touch .env
streamlit run Sequential_agent_streamlit_template/app.py
```

Ouvrez ensuite l'adresse locale dans votre navigateur.

Second terminal :

```bash
cd ~/Documents/AI-Agent
codex
```

Vous pouvez alors demander à Codex :

```text
Open Sequential_agent_streamlit_template/app.py and change the sidebar title to "AI Policy Classroom Agent". Then explain which line you changed.
```

## 25. Concentrez-vous seulement sur les fichiers dont vous avez besoin

Au début, vous devriez ignorer la majeure partie du dépôt.

Pour le premier agent simple, vous n'avez besoin que de :

- `my_agent_project/agent.py`
- `my_agent_project/.env`

Pour le modèle Streamlit, vous n'avez besoin que de :

- `Sequential_agent_streamlit_template/app.py`
- `Sequential_agent_streamlit_template/pipeline.py`
- `Sequential_agent_streamlit_template/README.md`
- `.env`

Cela suffit pour votre premier vrai projet.
