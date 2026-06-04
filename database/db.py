import sqlite3
import os

os.makedirs("database", exist_ok=True)

def init_db():
    conn = sqlite3.connect("database/robotics.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT UNIQUE,
            link TEXT,
            published TEXT,
            source TEXT,
            importance_score INTEGER,
            category TEXT,
            summary TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def save_article(article):
    conn = sqlite3.connect("database/robotics.db")
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT OR IGNORE INTO articles
            (title, link, published, source, importance_score, category, summary)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            article["title"], article["link"], article["published"],
            article["source"], article.get("importance_score"),
            article.get("category"), article.get("summary")
        ))
        conn.commit()
    except Exception as e:
        print(f"DB Error: {e}")
    finally:
        conn.close()