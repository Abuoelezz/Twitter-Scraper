import time
from bs4 import BeautifulSoup
from selenium import webdriver

# Configuration settings
CONFIG = {
    "usernames": ['Mr_Derivatives', 'warrior_0719', 'ChartingProdigy', 'allstarcharts', 'yuriymatso',
                  'TriggerTrades', 'AdamMancini4', 'CordovaTrades', 'Barchart', 'RoyLMattox'], # Username of Twitter accounts to scrape
    "wait_time_sec": 6,  # Time to wait for each page to load (seconds)
    "scrape_interval_min": 4  # Time between scrapes (minutes)
}

# Dictionary to store stock symbol counts
stock_symbols_counts = {}

def scrape_user(username):
    
    target_url = f'https://twitter.com/{username}'

    # Initialize Chrome webdriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run Chrome in headless mode (no GUI)
    driver = webdriver.Chrome(options=options)

    try:
        # Get the webpage content
        driver.get(target_url)
        time.sleep(CONFIG['wait_time_sec'])  # Wait for the page to load

        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Find the section containing tweets
        tweets_section = soup.find('section', class_='css-175oi2r')

        # Extract stock symbols from tweet links
        if tweets_section:
            symbols = tweets_section.find_all('a', class_='css-1qaijid r-bcqeeo r-qvutc0 r-poiln3 r-1loqt21')

            for symbol_link in symbols:
                stock_symbol = symbol_link.text.upper()

                # Check if symbol starts with '$'
                if stock_symbol.startswith('$'):
                    # Update stock symbol count
                    stock_symbols_counts[stock_symbol] = stock_symbols_counts.get(stock_symbol, 0) + 1
    except Exception as e:
        print(f"Error encountered while processing {username}: {e}")
    finally:
        # Always close the browser window
        driver.quit()

def print_stock_symbol_counts():
    for symbol, count in stock_symbols_counts.items():
        print(f"'{symbol}' was mentioned {count} times in the last {CONFIG['scrape_interval_min']} minutes")
    print('........................................................')

def main():
    
    while True:
        # Scrape each user
        for username in CONFIG["usernames"]:
            scrape_user(username)

        # Print current stock symbol counts
        print_stock_symbol_counts()

        # Clear the dictionary
        stock_symbols_counts.clear()

        # Wait for the specified scrape interval
        time.sleep(CONFIG["scrape_interval_min"] * 60)  # Convert minutes to seconds

if __name__ == "__main__":
    main()