from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

service = Service()  # Automatically uses chromedriver in PATH
driver = webdriver.Chrome(service=service, options=options)

url = "https://www.geo.tv/category/pakistan"
driver.get(url)

# Wait for articles to load
WebDriverWait(driver, 15).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.cat-latest__desc'))
)

articles = driver.find_elements(By.CSS_SELECTOR, 'div.cat-latest__desc')

with open('karachi_articles.txt', 'w', encoding='utf-8') as file:
    for article in articles:
        try:
            title = article.find_element(By.TAG_NAME, 'a').text.strip()
            snippet = article.find_element(By.TAG_NAME, 'p').text.strip()
            link = article.find_element(By.TAG_NAME, 'a').get_attribute('href')

            if 'karachi' in title.lower() or 'karachi' in snippet.lower():
                file.write(f"Title: {title}\n")
                file.write(f"Link: {link}\n")
                file.write(f"Snippet: {snippet}\n")
                file.write("-" * 50 + "\n")
                print(f"✓ {title}")
        except:
            continue

driver.quit()
