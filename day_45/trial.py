from bs4 import BeautifulSoup
import lxml

with open('website.html', 'r') as file:
    data = file.read()
    # print(data)

soup = BeautifulSoup(data, 'lxml')
# returns an object 
# soup.a gives only the first anchor tag
# print(soup.a)
# print(soup.title.name)
# print(soup.prettify())

all_anchor_tags = soup.find_all(name="a")
for tag in all_anchor_tags:
    # print(tag.getText())
    # use get() with attribute name to access attributes
    print(tag.get("href"))

# find using id
heading = soup.find(name="h1", id="name")
print(heading)
# find using class but class is a keyword in python
# so use class_
section_headings = soup.find_all(name="h3", class_="heading")
print(section_headings)

# select tag is used for css selectors
# eg: paragraph > anchor
company_url = soup.select_one("p a")
print(company_url)