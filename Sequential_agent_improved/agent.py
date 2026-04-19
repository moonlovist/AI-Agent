from google.adk import Agent
from google.adk.agents import SequentialAgent
from google.adk.tools import google_search


MODEL = "gemini-2.5-flash"


research_agent = Agent(
    name="research_agent",
    model=MODEL,
    description="Collects and structures factual information for the requested topic.",
    instruction="""
You are a research assistant for an AI Agent architecture lesson.

Your task:
- Understand the user's topic or question.
- Use Google Search when the request needs recent, factual, external, or verifiable information.
- If the request is conceptual and does not require current facts, answer from general knowledge.
- Extract only the information needed for the next agent.

Return STRICTLY valid JSON with this schema:
{
  "topic": "...",
  "key_points": ["...", "...", "..."],
  "architecture_pattern": "...",
  "tools_used": ["..."],
  "limitations": ["..."],
  "sources": ["..."]
}

Rules:
- Do not write paragraphs.
- If no external source is needed, use an empty list for "sources".
- If you are uncertain, include the uncertainty in "limitations".
""",
    tools=[google_search],
    output_key="research_result",
)


outline_agent = Agent(
    name="outline_agent",
    model=MODEL,
    description="Turns the research result into a clear answer structure.",
    instruction="""
You are an outlining assistant.

Use the research result below:
{research_result}

Create a concise outline for the final answer.

Return STRICTLY valid JSON with this schema:
{
  "title": "...",
  "target_audience": "EEEA students learning AI Agents",
  "sections": [
    {
      "heading": "...",
      "points": ["...", "..."]
    }
  ],
  "must_include": ["...", "..."],
  "avoid": ["...", "..."]
}

Rules:
- Use 3 to 5 sections.
- Keep the outline short.
- Do not write the final answer yet.
""",
    output_key="outline_result",
)


draft_agent = Agent(
    name="draft_agent",
    model=MODEL,
    description="Writes a first answer from the structured outline.",
    instruction="""
You are a writing assistant.

Use this outline:
{outline_result}

Write a first draft answer for EEEA students.

Rules:
- Follow the user's language if the user clearly uses one language.
- If the user does not specify a language, write in English.
- Keep the answer under 180 words.
- Use simple explanations suitable for students who are new to AI Agents.
- Do not mention internal state keys or JSON.
""",
    output_key="draft_answer",
)


review_agent = Agent(
    name="review_agent",
    model=MODEL,
    description="Checks the draft for clarity, grounding, length, and classroom usefulness.",
    instruction="""
You are a quality reviewer for a teaching assistant pipeline.

Review this draft:
{draft_answer}

Compare it with this outline:
{outline_result}

Return STRICTLY valid JSON with this schema:
{
  "passes": true,
  "issues": ["...", "..."],
  "revision_advice": ["...", "..."]
}

Check:
- Does the draft follow the outline?
- Is it clear for EEEA students?
- Is it concise?
- Does it avoid unsupported factual claims?
- Does it answer the user's request?

If there are no meaningful issues, return:
{
  "passes": true,
  "issues": [],
  "revision_advice": []
}
""",
    output_key="review_result",
)


final_agent = Agent(
    name="final_agent",
    model=MODEL,
    description="Produces the final student-facing answer after review.",
    instruction="""
You are the final answer writer.

Use this draft:
{draft_answer}

Use this review result:
{review_result}

Produce the final answer for the user.

Rules:
- Apply the review advice if any issue is listed.
- Return only the final answer.
- Do not include JSON.
- Do not mention the review process.
- Keep the answer concise and classroom-friendly.
""",
)


root_agent = SequentialAgent(
    name="teaching_agent_architecture_pipeline",
    description=(
        "Runs a teaching-oriented AI Agent pipeline: research, outline, draft, "
        "review, and final answer."
    ),
    sub_agents=[
        research_agent,
        outline_agent,
        draft_agent,
        review_agent,
        final_agent,
    ],
)
