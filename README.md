# Lyrics Dataset 


## Data Information
- Data was scraped from https://en.wikipedia.org/wiki/Billboard_Year-End_Hot_100_singles_of_2022 (every 10 years from 1952-2022).
- Lyrics were scraped from Genius API and separated into 7 different files for each decade. 
- Each song is separated by "New Song" before the lyrics start.

## Files
- **ScrapeData.ipynb** : Scrapes data from website and outputs the songsOfYear.csv file
- **ScrapeLyrics.ipynb** : Scrapes the lyrics for each song and outputs it into individual lyrics{year}.txt files.
- **CleanLyrics.ipynb** : Cleans the lyrics scraped from ScrapeLyrics.ipynb and outputs lyricsDataset.csv
- **lyrics{year}.txt** : Lyrics of the songs from each decade
- **songsOfYear.csv** : Dataset without the lyrics. Only has song name, artist, song genre, artist gender.
- **lyricsDataset.csv** : Final dataset containing the lyrics corresponding to artist and song.

## Installations
Use pip or a conda environment to install the following packages [pandas, numpy, lyricsgenius, requests, re, BeautifulSoup, nltk]

Create an account with Genius API Client to get your authentication token and be able to scrape the lyrics (https://docs.genius.com/#/getting-started-h1)
 

## Steps to run
Step 1: Run main() funtion in the ScrapeData.ipynb file to get the output csv file of all the data the hits every decade from 1952-2022.

Step 2: Run main() function in the ScrapeLyrics.ipynb to get individual files for lyrics in each decade

Step 3: Run main() function in the CleanLyrics.ipynb to get the final file that includes song, artist, genre, gender, and lyrics.

Step 4: Clean dataset according to user use (removing stopwords, punctuation, uppercase, etc).

## Potential Issues

- In step 2, after scraping {Artist,Song,Gender,Genre} for the songs and artists, I went in manually to double check and filled in the missing Gender rows. The missing genders were mostly of "Group" category. 

- In step 3, if there were no lyrics, it sometimes created a API timeout so I had to manually input lyrics and switch index of where to start. It may also instead mark the "no results" as "instrumental song" as the early decades had many instrumental songs without lyrics. 

- After step 3, I manually went in checked the lyrics after scraping to ensure it was correct. A few songs 5-10 out of the 730 either did not have lyrics or scraped 'gibberish'. 
