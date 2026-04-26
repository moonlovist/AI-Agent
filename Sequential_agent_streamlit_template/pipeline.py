from __future__ import annotations

import json
import os
from dataclasses import dataclass

from google import genai


DEFAULT_MODEL = "gemini-3-flash-preview"


RESEARCH_PROMPT = """
You are a research assistant for an AI Agent architecture lesson.

Task:
- Understand the user's topic or question.
- If the request needs recent, factual, external, or verifiable information,
  mention this limitation in the "limitations" field.
- If the request is conceptual, answer from general knowledge.
- Extract only the information needed for the next step.

Return STRICTLY valid JSON:
{
  "topic": "...",
  "key_points": ["...", "...", "..."],
  "architecture_pattern": "...",
  "tools_used": ["..."],
  "limitations": ["..."],
  "sources": ["..."]
}
"""


OUTLINE_PROMPT = """
You are an outlining assistant.

Use the research result below:
__RESEARCH_RESULT__

Create a concise outline for the final answer.

Return STRICTLY valid JSON:
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
"""


DRAFT_PROMPT = """
You are a writing assistant.

Use this outline:
__OUTLINE_RESULT__

Write a first draft answer for EEEA students.

Rules:
- Follow the user's language if the user clearly uses one language.
- If the user does not specify a language, write in English.
- Keep the answer under 220 words.
- Use simple explanations suitable for students who are new to AI Agents.
- Do not mention internal state keys or JSON.
"""


REVIEW_PROMPT = """
You are a quality reviewer for a teaching assistant pipeline.

Review this draft:
__DRAFT_ANSWER__

Compare it with this outline:
__OUTLINE_RESULT__

Return STRICTLY valid JSON:
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
"""


FINAL_PROMPT = """
You are the final answer writer.

Use this draft:
__DRAFT_ANSWER__

Use this review result:
__REVIEW_RESULT__

Produce the final answer for the user.

Rules:
- Apply the review advice if any issue is listed.
- Return only the final answer.
- Do not include JSON.
- Do not mention the review process.
- Keep the answer concise and classroom-friendly.
"""


@dataclass
class PipelineResult:
    research_result: dict
    outline_result: dict
    draft_answer: str
    review_result: dict
    final_answer: str


class SequentialTeachingPipeline:
    """Minimal sequential agent pipeline for custom Streamlit frontends."""

    def __init__(self, model: str = DEFAULT_MODEL, api_key: str | None = None):
        self.model = model
        self.api_key = api_key or os.getenv("GOOGLE_API_KEY")
        if not self.api_key:
            raise ValueError("Missing GOOGLE_API_KEY. Set it in .env or the Streamlit sidebar.")
        self.client = genai.Client(api_key=self.api_key)

    def run(self, user_request: str) -> PipelineResult:
        research_result = self._generate_json(
            f"{RESEARCH_PROMPT}\n\nUser request:\n{user_request}\n"
        )
        outline_result = self._generate_json(
            OUTLINE_PROMPT.replace(
                "__RESEARCH_RESULT__",
                json.dumps(research_result, ensure_ascii=False, indent=2),
            )
        )
        draft_answer = self._generate_text(
            DRAFT_PROMPT.replace(
                "__OUTLINE_RESULT__",
                json.dumps(outline_result, ensure_ascii=False, indent=2),
            )
        )
        review_result = self._generate_json(
            REVIEW_PROMPT.replace("__DRAFT_ANSWER__", draft_answer).replace(
                "__OUTLINE_RESULT__",
                json.dumps(outline_result, ensure_ascii=False, indent=2),
            )
        )
        final_answer = self._generate_text(
            FINAL_PROMPT.replace("__DRAFT_ANSWER__", draft_answer).replace(
                "__REVIEW_RESULT__",
                json.dumps(review_result, ensure_ascii=False, indent=2),
            )
        )
        return PipelineResult(
            research_result=research_result,
            outline_result=outline_result,
            draft_answer=draft_answer,
            review_result=review_result,
            final_answer=final_answer,
        )

    def _generate_text(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
        )
        return (response.text or "").strip()

    def _generate_json(self, prompt: str) -> dict:
        raw = self._generate_text(prompt)
        cleaned = self._extract_json_text(raw)
        try:
            return json.loads(cleaned)
        except json.JSONDecodeError as exc:
            raise ValueError(f"Model did not return valid JSON.\n\nRaw response:\n{raw}") from exc

    @staticmethod
    def _extract_json_text(raw: str) -> str:
        text = raw.strip()
        if text.startswith("```"):
            lines = text.splitlines()
            if lines and lines[0].startswith("```"):
                lines = lines[1:]
            if lines and lines[-1].strip() == "```":
                lines = lines[:-1]
            text = "\n".join(lines).strip()
        return text
