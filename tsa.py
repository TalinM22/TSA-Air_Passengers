import pandas as pd
import requests
from bs4 import BeautifulSoup

# URL to retrieve data
url = 'https://www.tsa.gov/coronavirus/passenger-throughput'

# Creating a GET request
try:
    req = requests.get(url)
except:
    print("Data TSA GET Failed")

# Parsing through the content and selecting relevant table
soup = BeautifulSoup(req.content,  "html.parser")
table = soup.find_all('table')[0]

# Loading the Parsed data to a dataframe
df = pd.read_html(str(table))[0]

# Set Date column as index to change to a datetime entity
df.set_index('Date', inplace=True)
df.index = pd.to_datetime(df.index)
-
df = df.reset_index()

print(df)

