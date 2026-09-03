# Multi-Agent Research System

An AI-powered research pipeline that uses multiple autonomous agents to search, read, write, and critique research reports on any given topic.

## Architecture

```
User Input (topic)
       |
       v
┌─────────────────┐
│  Search Agent    │  -- Tavily web search (top 5 results)
└────────┬────────┘
         v
┌─────────────────┐
│  Reader Agent    │  -- Scrapes & extracts content from best URL
└────────┬────────┘
         v
┌─────────────────┐
│  Writer Chain    │  -- Generates a structured research report
└────────┬────────┘
         v
┌─────────────────┐
│  Critic Chain    │  -- Reviews & scores the report
└────────┬────────┘
         v
    Final Output
```

**Agents and chains:**

- **Search Agent** — LangGraph agent with Tavily search tool. Finds recent, reliable sources.
- **Reader Agent** — LangGraph agent with a web scraper tool. Extracts readable content using trafilatura, readability, and BeautifulSoup (cascading fallback).
- **Writer Chain** — LLM chain with a structured prompt. Produces an introduction, key findings, conclusion, and sources.
- **Critic Chain** — LLM chain that scores the report (X/10), highlights strengths, and suggests improvements.

## Technologies

| Component | Technology |
|---|---|
| LLM | OpenAI GPT-4o-mini via LangChain |
| Agent framework | LangGraph |
| Web search | Tavily Search API |
| Web scraping | trafilatura, readability-lxml, BeautifulSoup4 |
| UI | Streamlit |
| Environment | python-dotenv |
| CLI output | Rich |

## Installation

1. Clone the repository:

```bash
git clone <repo-url>
cd multi-agent-research-system
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root:

```bash
OPENAI_API_KEY="your-openai-api-key"
TAVILY_KEY="your-tavily-api-key"
```

Get your keys from:
- OpenAI: https://platform.openai.com/api-keys
- Tavily: https://tavily.com

## Usage

### CLI

```bash
python main.py
```

Edit the `topic` variable in `main.py` to change the research subject.

### Web UI

```bash
streamlit run app.py
```

Opens a browser interface where you can type a topic and run the full pipeline with live status updates.

## Project Structure

```
.
├── app.py                          # Streamlit web interface
├── main.py                         # CLI entry point
├── requirements.txt
├── .env                            # API keys (not committed)
└── src/
    ├── agents/
    │   └── agents.py               # Agent & chain definitions
    ├── pipeline/
    │   └── pipeline.py             # Orchestrates the 4-step pipeline
    └── tools/
        └── tools.py                # Tavily search + web scraper tools
```

## License

MIT
