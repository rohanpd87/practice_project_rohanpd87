import pandas as pd
import requests
from bs4 import BeautifulSoup
import time   # ✅ added

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'}

url = 'https://techcrunch.com/'
response = requests.get(url, headers=headers)

if response.status_code != 200:
    print('Something went wrong. Please try again.')
    exit()

soup = BeautifulSoup(response.content, 'html.parser')

top_section = soup.find("div", class_="hero-package-2__list")

data = []

# 🔹 Function to get summary
def get_summary(article_url):
    try:
        res = requests.get(article_url, headers=headers)
        soup1 = BeautifulSoup(res.content, 'html.parser')

        summary_tag = soup1.find("p", id="speakable-summary")

        if summary_tag:
            for a in summary_tag.find_all("a"):
                a.unwrap()

            return summary_tag.get_text(strip=True)

        return "Summary not available"

    except requests.exceptions.RequestException:
        return "Request failed"


# 🔹 Main scraping
if top_section:
    for tag in top_section.select("a.loop-card__title-link")[:10]:

        title = tag.get_text(strip=True)
        link = tag.get("href")

        print(title)
        print(link)

        summary = get_summary(link)

        print("SUMMARY:", summary)
        print("-----")

        data.append({
            "headline": title,
            "link": link,
            "summary": summary
        })

        time.sleep(1)   # ✅ delay after each request


# 🔹 Save
df = pd.DataFrame(data)
df.to_csv("techcrunch_news.csv", index=False)

print("\n✅ Data saved to techcrunch_news.csv")