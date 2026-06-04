import json
from agents.news_collector import get_articles
from agents.ai_filter import analyze_article
from database.db import init_db, save_article
from notifications.telegram import send_daily_briefing

def run():
    print("🤖 Robotics Intelligence Agent Starting...\n")
    init_db()

    articles = get_articles()
    print(f"📰 Fetched {len(articles)} articles\n")

    important = []

    for article in articles[:10]:
        print(f"Analyzing: {article['title'][:60]}...")
        raw = analyze_article(article["title"], article["link"])

        try:
            analysis = json.loads(raw)
            if analysis.get("is_robotics_relevant") and analysis.get("importance_score", 0) >= 6:
                merged = {**article, **analysis}
                save_article(merged)
                important.append(merged)
        except:
            pass

    print(f"\n⭐ {len(important)} important articles found:\n")
    for a in important:
        print(f"[{a.get('importance_score')}/10] {a['title']}")
        print(f"  → {a.get('summary')}\n")

    print("📤 Sending to Telegram...")
    send_daily_briefing(important)
    print("✅ Briefing sent to Telegram!")

if __name__ == "__main__":
    run()