# Beginner Guide: Start with Codex, Run Your First Agent, Then Build a Streamlit Frontend

This guide is written for you if you are new to:

- Git and GitHub
- terminal commands
- shell commands
- Python environments
- AI agent projects
- Streamlit frontend editing

You do not need to understand everything at the beginning. You only need to follow the steps in order.

The goal of this guide is to help you:

1. install the basic tools
2. install Codex
3. download this project from GitHub
4. run your first simple agent: `my_agent_project`
5. create the correct `.env` file in the correct place
6. run the Streamlit agent template
7. make small frontend changes
8. use Codex to help you edit the project

You should learn in this order:

1. `my_agent_project`
2. `Sequential_agent_streamlit_template`

This order matters because the Streamlit template is easier to understand after you have already seen one simpler agent example.

## 1. Understand the learning path

Before you install anything, you should understand that this guide has two stages.

### Stage 1: run a simple agent

You will start with:

```text
my_agent_project
```

You should start there because it is the simplest agent example in the repository.

It helps you learn:

- what an agent folder looks like
- what `agent.py` does
- what `root_agent` means
- why a local `.env` file is needed
- how `adk web` works

### Stage 2: run a Streamlit frontend

After that, you will move to:

```text
Sequential_agent_streamlit_template
```

You should move there second because it adds a frontend on top of the basic agent idea.

It helps you learn:

- how to build a visible interface
- how to separate UI from logic
- how to edit tabs, columns, buttons, and inputs
- how a multi-step pipeline works

## 2. Understand the two most important Streamlit files

Later in the guide, when you work with the Streamlit template, you only need to remember these two files:

- `Sequential_agent_streamlit_template/app.py`
- `Sequential_agent_streamlit_template/pipeline.py`

You should use them like this:

- edit `app.py` when you want to change the page layout, sidebar, buttons, text boxes, tabs, and displayed results
- edit `pipeline.py` when you want to change the prompts, the sequence of steps, the model, and the final answer behavior

This matters because many beginners change the wrong file and then do not understand why the page did not change.

## 3. Install Git

You should install Git first because Git is the tool you will use to download the project from GitHub and save your own changes later.

Without Git, you can still download a ZIP file, but that makes it much harder to update the project, track your changes, and push your work back to GitHub.

First, check whether Git is already installed:

```bash
git --version
```

If Git is installed, you will see a version number such as:

```text
git version 2.xx.x
```

If you get an error instead, install Git:

- macOS: install Xcode Command Line Tools or Git from https://git-scm.com/

After installation, run the command again:

```bash
git --version
```

You should always check that an installation worked before moving on.

## 4. Install Python 3.11

You should install Python because this project is a Python project. The agents, Streamlit app, and supporting packages all run through Python.

You should try to use Python 3.11 because that version is a safe choice for this repository.

Check whether Python is already available:

```bash
python3 --version
```

If Python is installed, you will see something like:

```text
Python 3.11.x
```

If you do not have Python 3.11, install it before continuing.

After installation, check again:

```bash
python3 --version
```

## 5. Install Node.js

You should install Node.js because Codex CLI is installed with `npm`, and `npm` comes with Node.js.

If Node.js is missing, you will not be able to install Codex from the terminal.

Check whether Node.js and npm are available:

```bash
node --version
npm --version
```

If both commands show version numbers, you can continue.

If not, install Node.js from:

- https://nodejs.org/

Then check again:

```bash
node --version
npm --version
```

## 6. Install Codex CLI

You should install Codex early because it can help you explore the repository, explain files, and make small edits while you are still learning basic commands.

That makes it a useful teaching assistant, especially if you are not yet comfortable reading code by yourself.

Install Codex:

```bash
npm install -g @openai/codex
```

Now check that Codex was installed correctly:

```bash
codex --version
```

If that command works, the installation is complete.

If you see `command not found: codex`, the installation did not finish correctly or your shell cannot find the installed command yet.

## 7. Log in to Codex

You should log in before starting the project so that Codex is ready when you need it.

Run:

```bash
codex --login
```

Then follow the sign-in steps in the browser.

When that finishes, return to the terminal.

You do not need to start using Codex immediately. The important part is that the tool is ready.

## 8. Learn the most basic terminal commands

Before downloading the project, you should learn a few commands that let you move around the filesystem.

You do not need to memorize many commands. At the beginning, these are enough.

### `pwd`

You should use `pwd` when you want to know where you are.

```bash
pwd
```

It prints your current folder.

### `ls`

You should use `ls` when you want to see what is inside the current folder.

```bash
ls
```

It lists files and folders.

### `cd`

You should use `cd` when you want to move into another folder.

```bash
cd folder_name
```

Example:

```bash
cd AI-Agent
```

### `cd ..`

You should use `cd ..` when you want to move up one level.

```bash
cd ..
```

### `mkdir`

You should use `mkdir` when you want to create a new folder.

```bash
mkdir my_folder
```

These commands may look simple, but they are the base for everything else you do in the terminal.

## 9. Download the project from GitHub

You should download the project with `git clone` because that gives you the full repository and keeps it connected to GitHub.

That is much better than copying files by hand.

First, open Terminal.

Now move to a folder where you want to keep the project.

For example:

```bash
cd ~/Documents
```

Before cloning, check where you are:

```bash
pwd
```

Then clone the repository:

```bash
git clone https://github.com/moonlovist/AI-Agent.git
```

This command creates a new folder called `AI-Agent`.

Now move into that folder:

```bash
cd AI-Agent
```

Check the contents:

```bash
ls
```

You should see folders such as:

```text
my_agent_project
Sequential_agent
Sequential_agent_improved
Sequential_agent_streamlit_template
```

If you do not see them, you are probably in the wrong folder.

## 10. Open the project in Codex

You should open the project in Codex now because this is the moment when you begin reading the repository, and Codex can help explain the structure in plain language.

First, make sure you are in the repository root:

```bash
pwd
ls
```

Then start Codex:

```bash
codex
```

Once Codex opens, you can ask simple questions such as:

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

At this stage, you should use Codex mainly to understand the project, not to redesign everything.

## 11. Create a Python environment

You should create a Python virtual environment because it keeps this project's packages separate from the rest of your computer.

Without a virtual environment, different projects can interfere with each other, especially if they need different package versions.

From the repository root, create the environment:

```bash
python3 -m venv .venv
```

This creates a hidden folder called `.venv`.

Now activate it:

```bash
source .venv/bin/activate
```

After activation, your terminal usually shows something like:

```text
(.venv)
```

That visual marker is important. It tells you that you are using the local project environment.

## 12. Install the Python packages

You should install the required packages only after activating the virtual environment.

That way, the packages go into the project environment instead of your global Python installation.

First, upgrade `pip`:

```bash
pip install --upgrade pip
```

Then install the packages needed for both the first simple agent and the Streamlit template:

```bash
pip install google-adk python-dotenv streamlit google-genai
```

If you also want to use Jupyter notebooks:

```bash
pip install jupyter ipykernel
```

You should install packages one step at a time when you are learning. That makes it easier to identify which step failed if there is a problem.

## 13. Run your first simple agent: `my_agent_project`

You should start with `my_agent_project` because it is the simplest working example in this repository.

It teaches you the core structure of an agent before you add a custom frontend.

### 13.1 Look inside the folder

You should first look at the folder so that the example feels concrete.

Run:

```bash
ls my_agent_project
```

You should see files such as:

```text
__init__.py
agent.py
```

The important file is:

```text
my_agent_project/agent.py
```

That file defines the agent.

### 13.2 Create the `.env` file for `my_agent_project`

You should create a `.env` file for this first agent because the agent needs access to your Google API key.

This is one place where beginners often get confused. The location of the `.env` file matters.

For this first simple agent, create the `.env` file here:

```text
my_agent_project/.env
```

Create it with:

```bash
touch my_agent_project/.env
```

Now open it in a text editor and add:

```text
GOOGLE_API_KEY=your_key_here
```

Replace `your_key_here` with your real key.

The file name must be exactly `.env`.

### 13.3 Understand why the `.env` location matters

You should understand this rule clearly:

- if you are running `my_agent_project`, put the key in `my_agent_project/.env`
- if you are running the Streamlit template later, put the key in `.env` at the repository root

If you put the key in the wrong place, the app may start but the model call will fail later.

### 13.4 Run the first agent with ADK

You should run the first agent with ADK because that is the simplest way to see how a basic agent folder becomes a working app.

Make sure you are still in the repository root:

```bash
pwd
ls
```

Now run:

```bash
adk web
```

If `adk` is not found, try:

```bash
python -m adk web
```

After that, open the local address shown in the terminal.

Inside the ADK page, you should be able to select:

```text
my_agent_project
```

### 13.5 What to test in the first agent

You should test a very simple question first.

For example:

```text
Explain AI agents in one sentence.
```

Then try a question that may use search:

```text
Tell me about a recent AI news item.
```

This helps you understand what the first agent can do before you move on to the more complex template.

When you finish testing, stop ADK in the terminal with:

```text
Ctrl+C
```

## 14. Create the root `.env` file for the Streamlit template

You should create a second `.env` file before running the Streamlit template because the template reads the API key from the repository root.

This is a different location from `my_agent_project/.env`.

For the Streamlit template, create:

```text
.env
```

From the repository root, run:

```bash
touch .env
```

Open that file in a text editor and add:

```text
GOOGLE_API_KEY=your_key_here
```

Replace `your_key_here` with your real key.

If you already created `my_agent_project/.env`, do not assume that the Streamlit template will automatically use it.

## 15. Run the Streamlit template

You should run the app now because once the project opens in the browser, you can finally connect the code to a visible interface after already understanding the simpler agent.

From the repository root, while the virtual environment is still active, run:

```bash
streamlit run Sequential_agent_streamlit_template/app.py
```

After a few seconds, the terminal will show a local address, usually:

```text
http://localhost:8501
```

Open that address in your browser.

If the page opens, the app is running correctly.

## 16. Understand exactly which file to change

Before editing anything, you should decide whether you want to change:

- the visible page
- the agent behavior

This matters because beginners often change the wrong file and then think nothing is working.

### If you want to change the visible page

You should edit:

```text
Sequential_agent_streamlit_template/app.py
```

This file controls:

- page title
- sidebar
- buttons
- text boxes
- tabs
- columns
- displayed results
- history display

### If you want to change how the agent works

You should edit:

```text
Sequential_agent_streamlit_template/pipeline.py
```

This file controls:

- the research step
- the outline step
- the draft step
- the review step
- the final answer step
- the model name
- the prompt instructions
- JSON parsing behavior

## 17. Make your first frontend change

You should start with a very small frontend change because that gives you a fast success and helps you learn where the layout is controlled.

Do not begin with a full redesign.

### Example 1: change the page title

Open:

```text
Sequential_agent_streamlit_template/app.py
```

Find this code:

```python
st.set_page_config(
    page_title="Sequential Agent Template",
```

Change it to:

```python
st.set_page_config(
    page_title="My Classroom Agent",
```

Save the file.

Then go back to the browser. Streamlit usually reloads automatically. If not, refresh the page.

### Example 2: change the sidebar title

Find:

```python
st.title("🧩 Sequential Agent")
```

Change it to:

```python
st.title("🧩 My First Agent")
```

Save the file and check the page again.

### Example 3: change help text

Find a line such as:

```python
st.caption("Students can change the layout here without touching the core pipeline.")
```

Change it into simpler course-specific text.

This is a good beginner exercise because it lets you see exactly where small UI text changes appear.

## 18. Make a slightly bigger frontend change

Once you are comfortable with text edits, you should try a structural change.

This teaches you that frontend work is not only about wording. It is also about layout.

### Example 1: add a new text box

In `render_workspace()` inside `app.py`, add:

```python
course_name = st.text_input("Course name", value="AI Agent 101")
st.caption(f"Current course: {course_name}")
```

This teaches you how user input appears on the page.

### Example 2: add a new tab

Find:

```python
tab1, tab2, tab3 = st.tabs(["Intermediate Steps", "History", "Raw Data"])
```

Change it to:

```python
tab1, tab2, tab3, tab4 = st.tabs(
    ["Intermediate Steps", "History", "Raw Data", "Notes"]
)
```

Then add:

```python
with tab4:
    st.write("Students can add their own notes here.")
```

This teaches you how the page is divided into sections.

### Example 3: change column width

Find:

```python
left, right = st.columns([1.2, 0.8], gap="large")
```

Change it to:

```python
left, right = st.columns([1, 1], gap="large")
```

This makes the left and right areas the same width.

## 19. Change the agent behavior

You should edit `pipeline.py` only after you understand the frontend a little.

That is because prompt changes are less visible than layout changes, and beginners often find them harder to debug.

### Example 1: make the final answer longer

Open:

```text
Sequential_agent_streamlit_template/pipeline.py
```

Find a rule such as:

```text
Keep the answer under 220 words.
```

Change it to:

```text
Keep the answer under 400 words.
```

Now the final answer can be more detailed.

### Example 2: make the tone more formal

Find the final prompt and add wording such as:

```text
Use a formal academic tone suitable for university teaching.
```

This is a good way to learn how prompts change output style.

## 20. Use Codex to help with small changes

You should use Codex for one small task at a time.

This matters because beginners often ask for a full redesign, then they cannot understand what changed.

A better workflow is:

1. decide one small change
2. ask Codex to make that one change
3. read the changed file
4. run the app again

Good prompts for Codex:

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

Bad beginner workflow:

- asking Codex to redesign the whole app at once
- changing frontend and pipeline at the same time
- making many edits before rerunning the app

## 21. Save your changes with Git

You should save your changes with Git so that you can keep a history of what you changed and go back if needed.

First, check what changed:

```bash
git status
```

Then add the changed files:

```bash
git add .
```

Then create a commit:

```bash
git commit -m "Update Streamlit layout"
```

If you are connected to your own GitHub repository, you can send the changes:

```bash
git push
```

You do not need to understand every Git feature at the beginning. At first, it is enough to understand:

- `git status` shows what changed
- `git add .` prepares the changes
- `git commit` saves a checkpoint
- `git push` sends the checkpoint to GitHub

## 22. Solve common problems

You should expect problems at the beginning. That is normal. The important thing is to read the error and fix one thing at a time.

### Problem: `command not found: codex`

This usually means Codex is not installed correctly, or your shell cannot find it.

Try reinstalling:

```bash
npm install -g @openai/codex
```

Then check:

```bash
codex --version
```

### Problem: `command not found: streamlit`

This usually means your virtual environment is not active.

Activate it again:

```bash
source .venv/bin/activate
```

Then run:

```bash
streamlit run Sequential_agent_streamlit_template/app.py
```

### Problem: `command not found: adk`

This usually means `google-adk` is not installed in your virtual environment.

Run:

```bash
pip install google-adk
```

Then try again:

```bash
adk web
```

### Problem: `ModuleNotFoundError`

This usually means the required packages were not installed.

For the Streamlit template, run:

```bash
pip install streamlit python-dotenv google-genai
```

For the simple ADK agent, if packages are missing, run:

```bash
pip install google-adk python-dotenv
```

### Problem: the model cannot find your API key

This usually means your `.env` file is in the wrong place.

Check this carefully:

- for the simple agent: `my_agent_project/.env`
- for the Streamlit template: `.env` in the repository root

### Problem: `503 UNAVAILABLE`

This usually means the model is temporarily overloaded.

You should try one of these actions:

- run the request again
- switch to another model in the sidebar
- wait a minute and retry

### Problem: the page opens but looks wrong

You should:

1. stop the app with `Ctrl+C`
2. save the edited file
3. start the app again
4. read the terminal output carefully

## 23. A realistic beginner learning order

You should learn in this order:

1. `cd`, `ls`, `pwd`
2. `git clone`
3. `python3 -m venv .venv`
4. `source .venv/bin/activate`
5. `pip install ...`
6. create `my_agent_project/.env`
7. run `adk web`
8. test `my_agent_project`
9. create root `.env`
10. run `streamlit run ...`
11. change text in `app.py`
12. change layout in `app.py`
13. change prompt rules in `pipeline.py`
14. ask Codex for one small improvement at a time

This order works because it moves from simple visible tasks to more abstract ones.

## 24. One complete example session

You can follow this exact sequence.

First terminal:

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

After testing `my_agent_project`, stop the app with `Ctrl+C`.

Then continue:

```bash
touch .env
streamlit run Sequential_agent_streamlit_template/app.py
```

Then open the local address in your browser.

Second terminal:

```bash
cd ~/Documents/AI-Agent
codex
```

Now ask Codex:

```text
Open Sequential_agent_streamlit_template/app.py and change the sidebar title to "AI Policy Classroom Agent". Then explain which line you changed.
```

## 25. Focus only on the files you need

At the beginning, you should ignore most of the repository.

For the first simple agent, you only need:

- `my_agent_project/agent.py`
- `my_agent_project/.env`

For the Streamlit template, you only need:

- `Sequential_agent_streamlit_template/app.py`
- `Sequential_agent_streamlit_template/pipeline.py`
- `Sequential_agent_streamlit_template/README.md`
- `.env`

That is enough for your first real project.
