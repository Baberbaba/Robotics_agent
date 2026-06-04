#  Robotics Intelligence Agent

I got tired of manually searching for robotics news every day. So I built something that does it for me.
This is an autonomous AI agent that wakes up every morning, scans hundreds of sources across the internet — research papers, news outlets, company blogs, arXiv — filters out the noise, and sends me a curated intelligence briefing straight to my Telegram. No dashboards to check. No feeds to scroll. Just the signal, delivered.
## What It Does
Every day at 6:00 AM UTC, the agent:
1. Pulls from 8+ sources across robotics and physical AI — arXiv, TechCrunch, IEEE Spectrum, MIT Technology Review, VentureBeat, Wired, and more
2. Collects 800+ articles from across the web
3. Pre-filters them by keyword to find only robotics-relevant content
4. Sends the relevant ones through OpenAI's GPT-4o-mini, which scores each article 1–10, categorizes it, and writes a concise summary
5. Keeps only the articles that score 6 or higher
6. Saves everything to a local SQLite database to avoid duplicates
7. Fires off a Telegram message with the day's most important developments

The whole thing runs in the cloud via GitHub Actions. Free. Automatic. No server needed.
## Why I Built This

Robotics and physical AI are moving faster than anyone can keep up with manually. New papers drop on arXiv every day. Companies like Figure AI, Boston Dynamics, and Tesla are shipping updates constantly. Conferences like ICRA and NeurIPS produce hundreds of relevant results per cycle.
Reading all of it is a full-time job. I wanted a system that could do the reading for me and only surface what actually matters — not just what's trending, but what represents a genuine advancement worth knowing about.
This agent is the first version of that system.

## Tech Stack

| Layer | Tool |
|-------|------|
| Language | Python |
| AI Filter | OpenAI GPT-4o-mini |
| News Collection | RSS feeds via feedparser |
| Database | SQLite |
| Notifications | Telegram Bot API |
| Automation | GitHub Actions (runs daily, free) |
| Secret Management | GitHub Secrets + python-dotenv |

## Pipeline

```
RSS Feeds (800+ articles)
         ↓
  Keyword Pre-filter
         ↓
  OpenAI Analysis
  (importance score, category, summary)
         ↓
  Score Filter (≥ 6/10)
         ↓
  SQLite Database
         ↓
  Telegram Briefing 
```

## Sources Monitored

**News & Media**
- TechCrunch AI
- MIT Technology Review
- VentureBeat AI
- Wired Robotics
- IEEE Spectrum Robotics

**Research**
- arXiv cs.RO (Robotics)
- arXiv cs.AI (Artificial Intelligence)
- arXiv cs.LG (Machine Learning)

## Project Structure

```
robotics_agent/
├── agents/
│   ├── news_collector.py     # Pulls articles from RSS feeds
│   └── ai_filter.py          # Sends articles through OpenAI for analysis
├── database/
│   └── db.py                 # SQLite setup and article storage
├── notifications/
│   └── telegram.py           # Sends daily briefing to Telegram
├── .github/
│   └── workflows/
│       └── daily.yml         # GitHub Actions automation
├── main.py                   # Orchestrates the full pipeline
├── requirements.txt
└── .env.example              # Template for required environment variables
```

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/Baberbaba/Robotics_agent.git
cd Robotics_agent
```

### 2. Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```
### 4. Configure environment variables
Create a `.env` file in the root directory:

```
OPENAI_API_KEY=your_openai_key_here
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_telegram_chat_id
```
To get a Telegram bot token, message [@BotFather](https://t.me/BotFather) on Telegram and follow the instructions.

### 5. Run locally

```bash
python main.py
```
## Automated Daily Runs

The agent runs automatically every day via GitHub Actions. To enable this on your own fork:
1. Go to your repository → Settings → Secrets and variables → Actions
2. Add the three secrets: `OPENAI_API_KEY`, `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`
3. The workflow in `.github/workflows/daily.yml` handles the rest

You can also trigger it manually from the Actions tab at any time.

## Roadmap

This is Phase 1. Here's where it's going:

- **Phase 2** — Smarter filtering, keyword pre-screening, analyze more articles per run
- **Phase 3** — GitHub trending repos monitoring, conference paper tracking (ICRA, NeurIPS, CVPR)
- **Phase 4** — LangGraph multi-agent workflow with specialized agents per source type
- **Phase 5** — Company blog scrapers, funding tracker, researcher social media monitoring
- **Phase 6** — Vector database (ChromaDB) for semantic search across all stored articles

The end goal is a personal robotics intelligence analyst that knows what changed, why it matters, and what to watch next.
## Requirements

feedparser
openai
python-dotenv
requests

Built with Python and a desire to stop manually scrolling through robotics news every morning.
