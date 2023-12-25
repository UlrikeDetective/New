# PDF convert to csv or excel - Option2

import PyPDF2
import pandas as pd

# Extract text from PDF
pdf_file = open('Layoffs_Tracker.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)
text = ''
for page_num in range(len(pdf_reader.pages)):
    text += pdf_reader.pages[page_num].extract_text()

# Convert text to DataFrame and save as CSV
df = pd.DataFrame([x.split(',') for x in text.split('\n')])
df.to_csv('tech_layoffs_2023_02.csv', index=False)

# Save as Excel (XLSX) file
df.to_excel('tech_layoffs_2023_02.xlsx', index=False)

