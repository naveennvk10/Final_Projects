#WEB SCRAPING FROM STACKOVERFLOW WEBSITE

from urllib import response
from bs4 import BeautifulSoup

import requests

url= 'https://stackoverflow.com/?tab=hot'
response=(requests.get(url))
stackoverflow=response.text

new_soup=BeautifulSoup(stackoverflow, 'html.parser')
new_soup.prettify()

question_tag=new_soup.find(name='h3', class_="s-post-summary--content-title")
question_title=question_tag.getText()

question_link=question_tag.find(name='a').get('href')


question_vote=new_soup.find(name='span', class_="s-post-summary--stats-item-number").getText()

print(question_title)
print(question_link)
print(question_vote)

#ALL QUESTIONS

questions=new_soup.find_all(name='h3', class_="s-post-summary--content-title")
question_titles=[]
question_links=[]
for i in questions:
    qt=i.getText().strip()
    question_titles.append(qt)
    ql='www.stackoverflow.com'+i.find(name='a').get('href')
    question_links.append(ql)

votes=[]
question_votes=new_soup.find_all(name='div', class_="s-post-summary--stats-item s-post-summary--stats-item__emphasized")
for i in question_votes:
    votes.append(i.getText())

print(len(votes))
print(len(question_links))

largestvote=max(votes)
index_of_max=votes.index(largestvote)
print(question_titles[index_of_max])
print(question_links[index_of_max])