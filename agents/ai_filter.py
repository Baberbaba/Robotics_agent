from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_article(title, link):
    prompt = f"""
You are a robotics and physical AI analyst.
Analyze this article and return ONLY valid JSON:

Title: {title}
Link: {link}

{{
  "importance_score": 7,
  "category": "Humanoid Robots",
  "key_advancement": "One line of what's new",
  "why_it_matters": "One line on significance",
  "summary": "2-3 sentence summary",
  "is_robotics_relevant": true
}}
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content