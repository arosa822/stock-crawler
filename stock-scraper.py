import os
import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def setup_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    return driver

def navigate_and_get_content(driver, url):
    driver.get(url)
    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        return driver.page_source
    except Exception as e:
        print("Error loading page:", e)
        return None

def clean_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    for script_or_style in soup(['script', 'style']):
        script_or_style.decompose()
    body = soup.body
    return body.get_text(separator='\n', strip=True) if body else ""

def save_cleaned_content(filename, content):
    # Ensure the data directory exists
    os.makedirs('./data', exist_ok=True)
    filepath = os.path.join('./data', filename)
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Cleaned content saved to {filepath}")

def main():
    parser = argparse.ArgumentParser(description="Scrape and clean HTML content for a given stock ticker.")
    parser.add_argument('stock_symbol', help="The stock ticker symbol to scrape and clean")
    args = parser.parse_args()

    driver = setup_driver()
    try:
        base_url = f"https://stockanalysis.com/stocks/{args.stock_symbol}"
        endpoints = {
            "stock_content": "",
            "financial_content": "/financials",
            "balance_content": "/financials/balance-sheet",
            "cash_content": "/financials/cash-flow-statement",
            "ratio_content": "/financials/ratios"
        }

        cleaned_contents = {}
        for key, endpoint in endpoints.items():
            url = base_url + endpoint
            content = navigate_and_get_content(driver, url)
            if content:
                cleaned_content = clean_html(content)
                filename = f"{args.stock_symbol}_{key}_cleaned.html"
                save_cleaned_content(filename, cleaned_content)
                cleaned_contents[key] = filename

        # Combine all cleaned content into a single file
        combined_file = f"{args.stock_symbol}_data.html"
        with open(combined_file, 'w', encoding='utf-8') as file:
            for filename in cleaned_contents.values():
                filepath = os.path.join('./data', filename)
                with open(filepath, 'r', encoding='utf-8') as f:
                    file.write(f.read())
                    file.write("\n\n")  # Add some spacing between sections
            print(f"All data combined and saved to {combined_file}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
