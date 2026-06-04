import requests
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    # Split message if too long
    max_length = 4000
    if len(text) <= max_length:
        requests.post(url, json={
            "chat_id": CHAT_ID,
            "text": text,
            "parse_mode": "Markdown"
        })
    else:
        # Send in chunks
        chunks = [text[i:i+max_length] for i in range(0, len(text), max_length)]
        for chunk in chunks:
            requests.post(url, json={
                "chat_id": CHAT_ID,
                "text": chunk,
                "parse_mode": "Markdown"
            })

def send_daily_briefing(articles):
    if not articles:
        send_message("🤖 No major robotics news today.")
        return

    # Send header first
    send_message("🦾 *Daily Robotics Intelligence Briefing*")

    # Send each article separately
    for a in articles:
        msg = f"⭐ [{a['importance_score']}/10] *{a['title']}*\n"
        msg += f"{a.get('summary', '')}\n"
        msg += f"[Read more]({a['link']})"
        send_message(msg)