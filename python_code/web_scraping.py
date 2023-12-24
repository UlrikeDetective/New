import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://techcrunch.com/2023/12/21/tech-layoffs-2023-list/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract company names, month, and number of layoffs
layoffs_data = []
layoffs = soup.find_all('div', class_='tc-layoffs__item')
for layoff in layoffs:
    company = layoff.find('h3', class_='tc-layoffs__company').text.strip()
    month = layoff.find('span', class_='tc-layoffs__date').text.strip()
    count = layoff.find('span', class_='tc-layoffs__number').text.strip()
    layoffs_data.append({'Company': company, 'Month': month, 'Count': count})

# Check if data is extracted
if layoffs_data:
    # Create a DataFrame from the extracted data
    layoffs_df = pd.DataFrame(layoffs_data)

    # Save the DataFrame to a CSV file
    layoffs_df.to_csv('tech_layoffs.csv', index=False)
else:
    print("No data found or extraction issue.")



