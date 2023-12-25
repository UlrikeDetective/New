# pdf to csv file - Option 1

import tabula

# make sure your pdf file is in the same directory as your notebook
df = tabula.read_pdf("Layoffs_Tracker.pdf", pages='all')[0]
# convert PDF into CSV
tabula.convert_into("Layoffs_Tracker.pdf", "layoffs01.csv", output_format="csv", pages='all')
print(df)

