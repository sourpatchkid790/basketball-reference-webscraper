from urllib.request import urlopen
from bs4 import BeautifulSoup
# import pandas as pd

def extract_stats():
    
  year = 2022
  url = "https://www.basketball-reference.com/leagues/NBA_{}_per_game.html".format(year)
  html = urlopen(url)

  soup = BeautifulSoup(html, 'html.parser')
  # print(soup)

  soup.find_all('tr', limit=2)
  headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]
  headers = headers[1:]
  print(headers)

  rows = soup.findAll('tr')[1:]
  player_stats = [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]

  print(player_stats[0])
if __name__ == '__main__':
    print('helloworld')
    extract_stats()