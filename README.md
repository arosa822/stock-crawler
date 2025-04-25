# Stock Scraper

This project is a stock scraper that retrieves and cleans HTML content from stock analysis websites for a given stock ticker symbol. It uses Selenium to navigate web pages and BeautifulSoup to clean the HTML content.

## Features

- Scrapes stock overview, financials, balance sheet, cash flow statement, and ratios.
- Cleans HTML content by removing scripts and styles.
- Saves cleaned content in a structured format.
- Combines all cleaned content into a single file.

## Prerequisites

- Python 3.x
- Google Chrome browser
- ChromeDriver (managed automatically by `webdriver_manager`)

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

   Ensure `requirements.txt` includes:
   ```
   selenium
   webdriver_manager
   beautifulsoup4
   ```

## Usage

To run the stock scraper, use the following command:

```bash
python stock-scraper.py.py <stock_symbol>
```

Replace `<stock_symbol>` with the actual stock ticker symbol you want to scrape.

## Output

- **Cleaned Content Files**: The cleaned HTML content for each section (overview, financials, balance sheet, cash flow, and ratios) is saved in the `./data` directory. Each file is named in the format `<stock_symbol>_<section>_cleaned.html`.

- **Combined File**: All cleaned content is combined into a single file named `<stock_symbol>_data.html`, saved in the current working directory where the script is executed.

## Example

To scrape data for the stock symbol "AAPL":

```bash
python stock-scraper.py.py AAPL
```

This will create cleaned content files in the `./data` directory and a combined file `AAPL_data.html` in the current directory.

