from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

class bbrefScraper:
  dataframe = []
  headers = []
  
# Gets the year that the user wants to analyze the stats from
  def get_year(self):
    year = input('Enter year to collect stats from: ')
    print('year entered:', year)
    return int(year)


  # Extracts the stats from the year into a array
  def extract_stats(self):
      
    year = self.get_year()
    url = "https://www.basketball-reference.com/leagues/NBA_{}_per_game.html".format(year)
    html = urlopen(url)

    soup = BeautifulSoup(html, 'html.parser')

    soup.find_all('tr', limit=2)
    self.headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]
    self.headers = self.headers[1:]

    rows = soup.findAll('tr')[1:]
    player_stats = [[td.getText() for td in rows[i].findAll('td')]
              for i in range(len(rows))]


    self.create_dataframe(player_stats, self.headers)

  # Uses the array created from extract_stats to put all stats into a pandas dataframe
  def create_dataframe(self, player_stats, headers):
    stats = pd.DataFrame(player_stats, columns = headers)
    # print(stats.head(10))
    self.dataframe = stats

  def get_player_stats(self, player_name):
    print("Player Name:", player_name)
    # print(self.dataframe.loc[player_name])
    print(self.dataframe.loc[(self.dataframe["Player"] == player_name)] )
   


  def __init__(self):
    # self.get_year()
    self.extract_stats()
    print("headers:", self.headers)


if __name__ == '__main__':
    scraper = bbrefScraper()
    # print('first 10')
    # print(scraper.dataframe.head(10))
    scraper.get_player_stats("Quincy Acy")
    