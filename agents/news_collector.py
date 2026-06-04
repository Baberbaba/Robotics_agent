import feedparser

FEEDS = [
    # Current ones
    "https://feeds.feedburner.com/TechCrunch/artificial-intelligence",
    "https://arxiv.org/rss/cs.RO",
    "https://spectrum.ieee.org/feeds/topic/robotics.rss",
    
    # New ones
    "https://www.technologyreview.com/feed/",
    "https://venturebeat.com/ai/feed/",
    "https://www.wired.com/feed/tag/robots/rss",
    "https://arxiv.org/rss/cs.AI",
    "https://arxiv.org/rss/cs.LG",
]

def get_articles():
    articles = []
    for url in FEEDS:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            articles.append({
                "title": entry.title,
                "link": entry.link,
                "published": getattr(entry, "published", None),
                "source": url
            })
    return articles

if __name__ == "__main__":
    data = get_articles()
    print(f"\n✅ Collected {len(data)} articles\n")
    for a in data[:5]:
        print(a)
        print("-" * 60)