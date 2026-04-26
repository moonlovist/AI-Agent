# Sequential Agent Streamlit Template

This folder is a teaching template for students who want to build:

- a more structured multi-step agent
- a basic custom frontend with Streamlit
- a clear separation between agent logic and UI layout

## Why this template

`Sequential_agent_improved` is useful for explaining multi-step prompting, but it does not give students a custom interface.

This template adds a simple Streamlit app so students can:

- choose a model
- enter a prompt
- run a sequential pipeline
- inspect intermediate outputs
- redesign the layout without rewriting the pipeline logic

## File Structure

```text
Sequential_agent_streamlit_template/
├── __init__.py
├── app.py
├── pipeline.py
└── README.md
```

## Design Idea

- `pipeline.py`: the multi-step logic
- `app.py`: the Streamlit interface

Students should mostly edit:

- prompts and workflow in `pipeline.py`
- layout, tabs, sidebars, and widgets in `app.py`

## Install

From the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install streamlit python-dotenv google-genai
```

## API Key

Create a local `.env` file in the repository root:

```text
GOOGLE_API_KEY=your_key_here
```

Or paste the key into the Streamlit sidebar at runtime.

## Run

From the repository root:

```bash
streamlit run Sequential_agent_streamlit_template/app.py
```

## Good student extensions

1. Add a mode selector:
   single agent, sequential agent, or RAG agent.
2. Add a file uploader:
   let the agent answer from uploaded notes or PDFs.
3. Add step toggles:
   enable or disable review, outline, or critique stages.
4. Add editable system prompts:
   expose prompts in the sidebar for experimentation.
5. Add export:
   save the final answer and intermediate JSON as Markdown.

## Teaching advice

For beginner students, this is a good progression:

1. `my_agent_project`
2. `Sequential_agent_improved`
3. `Sequential_agent_streamlit_template`
4. a domain app such as policy, astronomy, or education
