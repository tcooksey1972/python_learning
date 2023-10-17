import requests
from bs4 import BeautifulSoup

#headers to keep from being blocked 
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}


#page to access as a string
url = 'https://www.basketball-reference.com/Leagues/NBA_2022_games.html'

# request.get function fetches the raw HTML
page = requests.get(url, headers=headers)

# now, create the 'BeutifulSoup' object with parser specified
soup = BeautifulSoup(page.content, features="html.parser")

#find all the table cells(which have the tag 'td'
table_cells = soup.find_all('td')

#create a list to store all the data

data = []

#loop through the cells and extract the data

for cell in table_cells:
    data.append(cell.text)
    

