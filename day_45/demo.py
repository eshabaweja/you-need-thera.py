from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text
soup = BeautifulSoup(yc_webpage,"html.parser")

articles = soup.find_all(name = "a", class_ = "titlelink")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.get_text()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

# using list comprehension
article_scores = [int (score.get_text().split()[0]) for score in soup.find_all(name="span", class_= "score")]

# print(article_texts)
# print(article_links)
# print(article_scores)

highest_upvoted = article_scores.index(max(article_scores))

print(article_texts[highest_upvoted])
print(article_links[highest_upvoted])
print(article_scores[highest_upvoted])
