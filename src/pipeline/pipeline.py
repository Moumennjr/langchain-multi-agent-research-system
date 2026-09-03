from src.agents.agents import build_search_agent, build_reader_agent, writer_chain, critic_chain

def _default_log(msg: str):
    print(msg)


def run_research_pipeline(topic: str, on_status=None) -> dict:
    log = on_status or _default_log
    state = {}

    log("Searching the web for relevant information...")
    search_agent = build_search_agent()
    search_result = search_agent.invoke({
        "messages": [("user", f"Find recent, reliable and detailed information about: {topic}")]
    })
    state["search_results"] = search_result["messages"][-1].content
    log("Search complete.")

    log("Reading and scraping top results...")
    reader_agent = build_reader_agent()
    reader_result = reader_agent.invoke({
        "messages": [("user",
            f"Based on the following search results about '{topic}', "
            f"pick the most relevant URL and scrape it for deeper content.\n\n"
            f"Search Results:\n{state['search_results'][:800]}"
        )]
    })
    state["scraped_content"] = reader_result["messages"][-1].content
    log("Scraping complete.")

    log("Writing the research report...")
    research_combined = (
        f"SEARCH RESULTS : \n {state['search_results']} \n\n"
        f"DETAILED SCRAPED CONTENT : \n {state['scraped_content']}"
    )
    state["report"] = writer_chain.invoke({
        "topic": topic,
        "research": research_combined
    })
    log("Report drafted.")

    log("Critic is reviewing the report...")
    state["feedback"] = critic_chain.invoke({
        "report": state["report"]
    })
    log("Review complete.")

    return state