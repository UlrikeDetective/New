from bs4 import BeautifulSoup
import pandas as pd

html_path = '/Users/ulrike_imac_air/projects/UlrikeDetective/scripts/tech _layoffs _ TechCrunch.html'

# Open the HTML file and create a BeautifulSoup object
with open(html_path, 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Find elements containing the company, month, and layoffs count information
layoffs_data = []
company_tags = soup.find_all('div', class_='company')
month_tags = soup.find_all('div', class_='month')
count_tags = soup.find_all('div', class_='count')

# Extract data from the found elements
for i in range(len(company_tags)):
    company = company_tags[i].get_text(strip=True)
    month = month_tags[i].get_text(strip=True)
    count = count_tags[i].get_text(strip=True)
    layoffs_data.append({'Company': company, 'Month': month, 'Count': count})

# Create a DataFrame from the extracted data
layoffs_df = pd.DataFrame(layoffs_data)

# Save the DataFrame to a CSV file
layoffs_df.to_csv('tech_layoffs_from_html.csv', index=False)


