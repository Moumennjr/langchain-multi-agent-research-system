import streamlit as st
from src.pipeline.pipeline import run_research_pipeline

st.set_page_config(
    page_title="Multi-Agent Research System",
    page_icon="🔬",
    layout="wide",
)

st.title("Multi-Agent Research System")
st.caption("An AI-powered pipeline that searches, reads, writes, and critiques research reports.")

topic = st.text_input(
    "Enter a research topic",
    placeholder="e.g. The impact of AI on the job market in the next decade",
)

run = st.button("Run Research", type="primary", disabled=not topic.strip())

if run:
    status_text = st.empty()

    def report_status(msg: str):
        status_text.info(msg)

    with st.status("Research pipeline running...", expanded=True) as status:
        try:
            result = run_research_pipeline(topic.strip(), on_status=report_status)
            status.update(label="Research complete!", state="complete", expanded=False)
        except Exception as e:
            status.update(label="Pipeline failed", state="error")
            st.error(f"An error occurred: {e}")
            st.stop()

    st.divider()

    tab_report, tab_search, tab_scrape, tab_critic = st.tabs([
        "Report", "Search Results", "Scraped Content", "Critic Review"
    ])

    with tab_report:
        st.subheader("Final Report")
        st.markdown(result["report"])

    with tab_search:
        st.subheader("Search Results")
        st.text(result["search_results"])

    with tab_scrape:
        st.subheader("Scraped Content")
        st.text(result["scraped_content"])

    with tab_critic:
        st.subheader("Critic Review")
        st.text(result["feedback"])
