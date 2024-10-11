# Twitter Scraper

This Python script is designed to scrape Twitter pages of specified usernames to extract stock symbols mentioned in their tweets. It utilizes Selenium WebDriver along with BeautifulSoup for web scraping. The script periodically visits the Twitter profiles, extracts stock symbols from the tweets, and counts their occurrences.

## Requirements
- Python 3.x
- Selenium (pip install selenium)
- BeautifulSoup (pip install beautifulsoup4)
- Chrome WebDriver (ensure it's compatible with your Chrome browser version)

## Usage
1. Ensure all the required packages are installed.
2. Download the Chrome WebDriver and place it in a directory accessible to the script.
3. Configure the CONFIG dictionary according to your preferences.
4. Run the script using Python.

## How it works
- The script iterates through the specified usernames and visits their Twitter pages using Selenium WebDriver.
- It waits for the page to load, extracts the HTML content, and parses it using BeautifulSoup.
- Stock symbols are extracted from tweet links and stored in a dictionary along with their counts.
- After processing all usernames, it prints the counts of each stock symbol mentioned.
- The process repeats at regular intervals specified in the CONFIG dictionary.
