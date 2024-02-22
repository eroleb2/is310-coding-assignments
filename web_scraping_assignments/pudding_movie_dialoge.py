from bs4 import BeautifulSoup
import requests
import pandas as pd
url = pd.read_csv('cleaned_pudding_data.csv')
url = url[:1000]
def scrape_script(url):
    response = requests.get(url)
    response = response.text
    html_string = response
    return html_string
url['text'] = url['link'].apply(scrape_script)
url.to_csv('/Users/erolb/OneDrive/pictures/screenshots/Desktop/is310-coding-assignments/pudding_movie_dialoge.csv', index=False)