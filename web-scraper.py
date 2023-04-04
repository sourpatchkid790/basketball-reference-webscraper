from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

# Gets the year that the user wants to analyze the stats from
def get_year():
  year = input('Enter year to collect stats from: ')
  print('year entered:', year)
  return int(year)


# Extracts the stats from the year into a array
def extract_stats():
    
  year = get_year()
  url = "https://www.basketball-reference.com/leagues/NBA_{}_per_game.html".format(year)
  html = urlopen(url)

  soup = BeautifulSoup(html, 'html.parser')

  soup.find_all('tr', limit=2)
  headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]
  headers = headers[1:]

  rows = soup.findAll('tr')[1:]
  player_stats = [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]


  create_dataframe(player_stats, headers)

# Uses the array created from extract_stats to put all stats into a pandas dataframe
def create_dataframe(player_stats, headers):
  stats = pd.DataFrame(player_stats, columns = headers)
  print(stats.head(10))

if __name__ == '__main__':
    extract_stats()