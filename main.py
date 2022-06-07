import requests
from bs4 import BeautifulSoup
import pandas as pd

# with open('website.html','r') as f:
#     contents = f.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
# print(soup.title.string)

# request = requests.get('https://news.ycombinator.com/news')
# soup = BeautifulSoup(request.text, 'html.parser')
# titlelinks = soup.find_all(name='a',class_='titlelink')
# scores = soup.find_all(name='span',class_='score')
#
# text = [titlelink.getText() for titlelink in titlelinks ]
# link = [titlelink.get('href') for titlelink in titlelinks]
# upvote = [int(score.getText().split(' ')[0]) for score in scores]
#
# data = pd.DataFrame({'text':text,'link':link,'upvote':upvote})
# data[data.upvote == max(data.upvote)]



URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

request = requests.get(URL)
soup = BeautifulSoup(request.text, 'html.parser')
titles = [title.getText().replace(':',')').split(')')[1] for title in soup.find_all(name='h3', class_='title')]
titles_position = [int(title.getText().replace(':',')').split(')')[0]) for title in soup.find_all(name='h3', class_='title')]

movies = pd.DataFrame({'title':titles, 'position':titles_position})
movies = movies.set_index(movies.position)
movies.sort_index()