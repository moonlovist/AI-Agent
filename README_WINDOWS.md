# Windows Setup Guide

This guide is for students using Windows. It explains how to run the agents in this repository, including `my_agent_project`, with Google ADK.

## 1. Install Git

Install Git for Windows:

- https://git-scm.com/download/win

During installation, the default options are usually fine.

## 2. Download the Course Files from GitHub

Open **Command Prompt** or **Git Bash**, then go to a folder where you want to save the course files.

Example:

```bat
cd C:\Users\YourName\Downloads
```

Clone the teacher's GitHub repository:

```bat
git clone https://github.com/moonlovist/AI-Agent.git
```

Then enter the project folder:

```bat
cd AI-Agent
```

You should now be in the parent folder that contains folders such as:

```text
my_agent_project
Sequential_agent
Sequential_agent_improved
Astronomy_image_agent
```

Do not run `adk web` from inside `my_agent_project`. Run it from this parent folder.

## 3. Install Anaconda or Miniconda

Install one of the following:

- Anaconda: https://www.anaconda.com/download
- Miniconda: https://docs.conda.io/projects/miniconda/

After installation, open **Anaconda Prompt** again and go back to the cloned project folder:

```bat
cd C:\Users\YourName\Downloads\AI-Agent
```

## 4. Create the Conda Environment

```bat
conda create -n agent_env python=3.11
conda activate agent_env
```

When the environment is active, the prompt should start with:

```text
(agent_env)
```

## 5. Install the Required Packages

```bat
pip install google-adk python-dotenv ipykernel
python -m ipykernel install --user --name agent_env --display-name "agent_env"
```

## 6. Create the Google API Key File

Each agent needs access to a Google API key. For `my_agent_project`, create this file:

```text
my_agent_project\.env
```

The easiest way on Windows is:

```bat
notepad my_agent_project\.env
```

When Notepad asks whether to create the file, choose **Yes**.

Add this line:

```text
GOOGLE_API_KEY=Your key here
```

Replace `Your key here` with your real Google API key.

Important:

- The file name must be `.env`, not `.env.txt`.
- Do not upload your real API key to GitHub.
- If you want to run another agent folder, create a `.env` file in that folder too.

For example:

```bat
notepad Sequential_agent\.env
notepad Sequential_agent_improved\.env
notepad Astronomy_image_agent\.env
```

## 7. Run ADK Web

Make sure you are still in the parent folder of the agent folders.

Example:

```bat
cd C:\Users\YourName\Downloads\AI-Agent
conda activate agent_env
adk web
```

ADK will print a local web address, usually similar to:

```text
http://localhost:8000
```

Open that address in your browser.

Then select the agent you want to test, for example:

- `my_agent_project`
- `Sequential_agent`
- `Sequential_agent_improved`
- `Astronomy_image_agent`

## 8. Run the Notebook

If you use `Instruction.ipynb`, open Jupyter Lab from the same activated environment:

```bat
conda activate agent_env
jupyter lab
```

In Jupyter Lab, select the kernel named:

```text
agent_env
```

## Troubleshooting

### `adk` is not recognized

The package may not be installed in the active environment. Run:

```bat
conda activate agent_env
pip install google-adk
```

### The agent does not appear in ADK Web

Check that:

- You ran `adk web` from the parent folder.
- The agent folder contains `__init__.py`.
- The agent folder contains `agent.py`.
- `agent.py` defines `root_agent`.

For `my_agent_project`, the structure should be:

```text
my_agent_project
├── __init__.py
├── agent.py
└── .env
```

### The Google API key is not loaded

Check that the `.env` file is in the correct agent folder.

For `my_agent_project`, it should be:

```text
my_agent_project\.env
```

Also check that the file contains exactly one line like this:

```text
GOOGLE_API_KEY=Your real key
```

### Windows created `.env.txt`

Windows may hide file extensions. In File Explorer:

1. Open the folder.
2. Click **View**.
3. Enable **File name extensions**.
4. Rename `.env.txt` to `.env`.

Using this command usually avoids the problem:

```bat
notepad my_agent_project\.env
```

### Port 8000 is already in use

Stop the other program using the port, or run ADK Web on another port:

```bat
adk web --port 8001
```

Then open:

```text
http://localhost:8001
```
