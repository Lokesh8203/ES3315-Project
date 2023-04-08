import requests
from bs4 import BeautifulSoup

url = 'https://www.screener.in/company/ITC/consolidated/#balance-sheet'

r = requests.get(url)
htmlContent = r.content

soup = BeautifulSoup(htmlContent, 'html.parser')

# #Get all anchor tags from the page
# anchors = soup.find_all('a')
# all_links = set()
# balancesheet = set()
# #Get all the links on the page
# for link in anchors:
#     if(link.get('href')!='#'):
#         linkText = "https://www.screener.in" + link.get('href')
#         all_links.add(link)


# for link in all_links:
#     if "#balance-sheet" in link.get('href'):
#         balancesheet.add(link)

import csv
import os

dirname = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(dirname, 'balancesheet_ITC.csv')
csv_writer = csv.writer(open(filename, 'w'))

#locate a section in soup with id
section = soup.find('section', attrs={'id':'balance-sheet'})

#locate a table in section with class
table = section.find('table', attrs={'class':'data-table responsive-text-nowrap'})

#Get all the rows of table
rows = table.find_all('tr')

for row in rows:
    #First row has the column names
    if row.find('th'):
        cols = row.find_all('th')
        cols = [ele.text.strip() for ele in cols]
        csv_writer.writerow(cols)
    else:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        #Trim the special character from the first element of row
        if(cols[0][-1] == '+'):
            cols[0] = (cols[0][:-2])
        csv_writer.writerow(cols)
        
