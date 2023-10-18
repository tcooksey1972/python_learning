from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Set up the selenium driver (assuming you're using Chrome)
driver = webdriver.Chrome()

# Open the Zillow page for Indiana
url = 'https://www.zillow.com/in/houses/'
driver.get(url)

# Wait for the page to load fully. Adjust the waiting time as needed.
wait = WebDriverWait(driver, 200)

# Once the page is loaded, capture the content
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Close the driver
driver.close()

# Parsing the soup object to extract relevant data 
# (The following selectors are hypothetical and should be adjusted based on Zillow's actual structure)

listings = soup.find_all('div', class_='list-card-info')
homes = []

for listing in listings:
    price_tag = listing.find('div', class_='list-card-price')
    est_price_tag = listing.find('div', class_='list-card-estimate')

    if price_tag and est_price_tag:
        price = int(price_tag.get_text().replace('$', '').replace(',', ''))
        est_price = int(est_price_tag.get_text().replace('$', '').replace(',', ''))
        
        if price < 0.7 * est_price:
            homes.append({
                'Address': listing.find('address', class_='list-card-addr').get_text(),
                'Price': price,
                'Estimated Price': est_price
            })

# Print the homes that match the criteria
for home in homes:
    print(home)
