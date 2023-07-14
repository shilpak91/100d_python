from bs4 import BeautifulSoup

import requests

with open("/Users/shilpak/Documents/Code100/100d_python/Web Development/bs4-start/website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents,"html.parser")
print(soup.title)
print(soup.title.string)

all_anchor_tag = soup.find_all(name="a")
print(all_anchor_tag)

for tag in all_anchor_tag:
    print(tag.getText())
    print(tag.get("href"))


heading = soup.find(name="h1",id="name")
print(heading)