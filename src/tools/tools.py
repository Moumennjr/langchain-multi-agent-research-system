from langchain.tools import BaseTool
import requests
from dotenv import load_dotenv
import os
from tavily import TavilyClient

load_dotenv()


tavily = TavilyClient(api_key=os.getenv("TAVILY_KEY"))


def web_search(query : str):
    """Search the web for recent and reliable information on a topic . Returns Titles , URLs and snippets."""
    results = tavily.search(query=query,max_results=5)

    # out = []

    # for r in results['results']:
    #     out.append(
    #         f"Title: {r['title']}\nURL: {r['url']}\nSnippet: {r['content'][:300]}\n"
    #     )

    # return "\n----\n".join(out)
    
    for r in results['results']:
        print(f"Title: {r['title']}")
        print(f"URL: {r['url']}")
        print(f"Snippet: {r['content'][:300]}")
        print("---")
