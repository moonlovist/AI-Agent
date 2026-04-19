from google.adk import Agent
from google.adk.tools import google_search
from google.adk.agents import SequentialAgent

research_agent = Agent(
    name="research_agent",
    model="gemini-2.5-flash",
    instruction="""
    You are a research assistant.

    Your job:
    - Use Google Search if needed
    - Extract key facts

    Output STRICTLY in JSON:
    {
      "key_points": ["...", "...", "..."],
      "frameworks": ["...", "..."]
    }

    Do NOT write paragraphs.
    """
    ,
    tools=[google_search]
)

outline_agent = Agent(
    name="outline_agent",
    model="gemini-2.5-flash",
    instruction="""
    You are an outlining assistant.

    Input is JSON.

    Convert it into a structured outline:

    - Title
    - 4–6 bullet points

    Do NOT write full paragraphs.
    """
)

final_agent = Agent(
    name="final_agent",
    model="gemini-2.5-flash",
    instruction="""
    You are a writer.

    Based on the outline, write a short, clean answer.

    Max 150 words.
    No repetition.
    """
)

root_agent = SequentialAgent(
    name="clean_pipeline",
    sub_agents=[research_agent, outline_agent, final_agent]
)