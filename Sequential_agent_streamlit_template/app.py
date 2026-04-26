from __future__ import annotations

import os
from dataclasses import asdict

import streamlit as st
from dotenv import load_dotenv

try:
    from Sequential_agent_streamlit_template.pipeline import (
        DEFAULT_MODEL,
        PipelineResult,
        SequentialTeachingPipeline,
    )
except ModuleNotFoundError:
    from pipeline import DEFAULT_MODEL, PipelineResult, SequentialTeachingPipeline


load_dotenv()

st.set_page_config(
    page_title="Sequential Agent Template",
    page_icon="🧩",
    layout="wide",
    initial_sidebar_state="expanded",
)


MODELS = [
    "gemini-3-flash-preview",
    "gemini-3-pro-preview",
    "gemini-2.5-flash",
    "gemini-2.0-flash",
    "gemma-3-4b-it",
    "gemma-3-12b-it",
    "gemma-3-27b-it",
]


DEFAULTS = {
    "user_request": "",
    "model": DEFAULT_MODEL,
    "api_key": "",
    "result": None,
    "history": [],
}


def init_state() -> None:
    for key, value in DEFAULTS.items():
        if key not in st.session_state:
            st.session_state[key] = value


def render_sidebar() -> None:
    with st.sidebar:
        st.title("🧩 Sequential Agent")
        st.caption("Teaching template for multi-step prompting with custom layout")
        st.divider()

        st.session_state.model = st.selectbox(
            "Model",
            MODELS,
            index=MODELS.index(st.session_state.model)
            if st.session_state.model in MODELS
            else 0,
        )
        st.session_state.api_key = st.text_input(
            "Google API Key",
            type="password",
            value=st.session_state.api_key,
            placeholder="Paste key or use GOOGLE_API_KEY",
        )

        if st.session_state.api_key or os.getenv("GOOGLE_API_KEY"):
            st.success("API key available")
        else:
            st.info("Add a Google API key to run the pipeline")

        st.divider()
        st.markdown("**Teaching idea**")
        st.caption("Keep pipeline logic in one file and UI layout in another.")

        if st.button("Clear results", use_container_width=True):
            st.session_state.result = None
            st.rerun()


def run_pipeline() -> None:
    api_key = st.session_state.api_key or os.getenv("GOOGLE_API_KEY")
    pipeline = SequentialTeachingPipeline(
        model=st.session_state.model,
        api_key=api_key,
    )
    try:
        with st.spinner("Running research, outline, draft, review, and final answer..."):
            result = pipeline.run(st.session_state.user_request.strip())
        st.session_state.result = result
        st.session_state.history.append(
            {
                "request": st.session_state.user_request.strip(),
                "model": st.session_state.model,
                "final_answer": result.final_answer,
            }
        )
    except Exception as exc:
        st.session_state.result = None
        message = str(exc)
        if "503" in message or "UNAVAILABLE" in message:
            st.error(
                "The selected model is temporarily overloaded. "
                "Try again in a moment or switch to another model in the sidebar."
            )
            st.info(
                "Recommended fallback for class demos: `gemini-2.5-flash`, "
                "`gemini-2.0-flash`, or `gemma-3-4b-it`."
            )
        else:
            st.error(f"Pipeline run failed: {exc}")


def render_workspace() -> None:
    st.title("Sequential Agent Streamlit Template")
    st.caption("Students can change the layout here without touching the core pipeline.")

    left, right = st.columns([1.2, 0.8], gap="large")

    with left:
        st.subheader("User Request")
        st.session_state.user_request = st.text_area(
            "Prompt",
            value=st.session_state.user_request,
            height=180,
            placeholder=(
                "Example: Explain when a sequential agent is better than a single "
                "agent, and give a classroom-friendly example."
            ),
            label_visibility="collapsed",
        )

        c1, c2 = st.columns(2)
        if c1.button(
            "Run pipeline",
            type="primary",
            use_container_width=True,
            disabled=not st.session_state.user_request.strip(),
        ):
            run_pipeline()

        if c2.button("Load demo prompt", use_container_width=True):
            st.session_state.user_request = (
                "Explain the difference between a single agent and a sequential "
                "multi-agent workflow for beginner students."
            )
            st.rerun()

        result = st.session_state.result
        if result:
            st.divider()
            st.subheader("Final Answer")
            st.markdown(result.final_answer)

    with right:
        st.subheader("Pipeline Summary")
        result = st.session_state.result
        if not result:
            st.info("Run the pipeline to see intermediate outputs.")
            return

        st.metric("Research points", len(result.research_result.get("key_points", [])))
        st.metric("Outline sections", len(result.outline_result.get("sections", [])))
        st.metric("Review issues", len(result.review_result.get("issues", [])))


def render_details(result: PipelineResult) -> None:
    tab1, tab2, tab3 = st.tabs(["Intermediate Steps", "History", "Raw Data"])

    with tab1:
        col1, col2 = st.columns(2, gap="large")
        with col1:
            with st.expander("Research Result", expanded=True):
                st.json(result.research_result)
            with st.expander("Outline Result", expanded=True):
                st.json(result.outline_result)
        with col2:
            with st.expander("Draft Answer", expanded=True):
                st.markdown(result.draft_answer)
            with st.expander("Review Result", expanded=True):
                st.json(result.review_result)

    with tab2:
        if not st.session_state.history:
            st.caption("No history yet.")
        else:
            for item in reversed(st.session_state.history):
                with st.expander(item["request"]):
                    st.caption(f"Model: {item['model']}")
                    st.markdown(item["final_answer"])

    with tab3:
        st.json(asdict(result))


def main() -> None:
    init_state()
    render_sidebar()
    render_workspace()

    if st.session_state.result:
        st.divider()
        render_details(st.session_state.result)


if __name__ == "__main__":
    main()
