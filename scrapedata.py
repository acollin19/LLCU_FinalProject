# Imports
import requests

from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


# Different format
Y1942 = "http://billboardtop100of.com/1942-2/"


def ScrapeSongsOfYear(YearSongsURL):
    page = requests.get(YearSongsURL)
    soup = bs4.BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id="main-wrapper")
    song_elems = results.find_all('div', class_='entry-content')
    print(song_elems)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Y2022 = "http://billboardtop100of.com/2022-2/"
    Y2012 = "http://billboardtop100of.com/2012-2/"
    Y2002 = "http://billboardtop100of.com/2002-2/"
    Y1992 = "http://billboardtop100of.com/1992-2/"
    Y1982 = "http://billboardtop100of.com/1982-2/"
    Y1972 = "http://billboardtop100of.com/1972-2/"
    Y1962 = "http://billboardtop100of.com/1962-2/"
    Y1952 = "http://billboardtop100of.com/1952-2/"

    ScrapeSongsOfYear(Y2022)

