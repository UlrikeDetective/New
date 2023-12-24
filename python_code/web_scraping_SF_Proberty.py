from bs4 import BeautifulSoup
import requests
import csv

# Part 1 - Scrape the links, addresses, and prices of the rental properties

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

# Use our Zillow-Clone website (instead of Zillow.com)
response = requests.get("https://appbrewery.github.io/Zillow-Clone/", headers=header)

data = response.text
soup = BeautifulSoup(data, "html.parser")

# Create a list of all the links on the page using a CSS Selector
all_link_elements = soup.select(".StyledPropertyCardDataWrapper a") 
all_links = [link["href"] for link in all_link_elements] 

# Create a list of all the addresses on the page using a CSS Selector
all_address_elements = soup.select(".StyledPropertyCardDataWrapper address")
all_addresses = [address.get_text().replace(" | ", " ").strip() for address in all_address_elements]

# Create a list of all the prices on the page using a CSS Selector
all_price_elements = soup.select(".PropertyCardWrapper span")
all_prices = [price.get_text().replace("/mo", "").split("+")[0] for price in all_price_elements if "$" in price.text]

# Combine the scraped data into a list of dictionaries
property_data = []
for i in range(len(all_links)):
    property_data.append({
        'Address': all_addresses[i],
        'Price': all_prices[i],
        'Link': all_links[i]
    })

# Function to save data to CSV
def save_to_csv(data):
    header = ['Address', 'Price', 'Link']
    file_exists = False
    try:
        # Check if the file already exists
        with open('property_data.csv', 'r') as file:
            file_exists = True
    except FileNotFoundError:
        pass
    
    # Write data to CSV
    with open('property_data.csv', 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=header)
        if not file_exists:
            writer.writeheader()  # Write header only if the file is created newly
        for row in data:
            writer.writerow(row)

# Save data to CSV
save_to_csv(property_data)
