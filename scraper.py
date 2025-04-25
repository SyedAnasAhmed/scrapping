import requests
from bs4 import BeautifulSoup
from textblob import TextBlob

# URL of the page
url = 'https://en.wikipedia.org/wiki/Karachi'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all paragraphs
paragraphs = soup.find_all('p')

# Create/open a text file to save results
with open('karachi_sentiment.txt', 'w', encoding='utf-8') as file:
    file.write("🧠 Sentiment analysis of Wikipedia page on Karachi\n\n")

    for i, p in enumerate(paragraphs):
        text = p.get_text(strip=True)
        if len(text) < 20:
            continue  # skip very short lines
        sentiment = TextBlob(text).sentiment.polarity
        if sentiment > 0:
            label = "Positive"
        elif sentiment < 0:
            label = "Negative"
        else:
            label = "Neutral"

        file.write(f"{i+1}. {text}\n")
        file.write(f"   → Sentiment: {label} (Score: {sentiment:.2f})\n\n")

print("✅ Sentiment analysis saved to 'karachi_sentiment.txt'")
