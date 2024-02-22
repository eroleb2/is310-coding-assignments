from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv
df = pd.read_csv('cleaned_pudding_data.csv')
link = df['link']
with open('pudding_movie_dialogue.csv', mode='w') as file:
    writer = csv.writer(file)
    writer.writerow(['Link', 'Script'])
    for i in link:
        response = requests.get(i)
        if response.status_code != 200:
            continue
        soup = bs4.beautifulsoup(response.text, 'html.parser')
        writer.writerow([i, soup.get_text()[:1000]])
