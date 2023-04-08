import requests
import csv
import os
from bs4 import BeautifulSoup

#popluate the list of stock symbols with Banks from BAnknifty nse website
# stock_symbols = ['ICICIBANK', 'HDFCBANK', 'KOTAKBANK', 'AXISBANK', 'INDUSINDBK', 'BANDHANBNK', 'BANKBARODA', 'BANKINDIA', 'CANBK', 'FEDERALBNK', 'IDBI', 'IDFCFIRSTB', 'PNB', 'RBLBANK', 'SBIN', 'YESBANK']

stock_symbol = 'hdfcbank'
ratio_url = 'https://www.moneycontrol.com/financials/hdfcbank/ratiosVI/HDF01'
balancesheet_url = 'https://www.moneycontrol.com/financials/hdfcbank/balance-sheetVI/HDF01'
pnl_url = 'https://www.moneycontrol.com/financials/hdfcbank/profit-lossVI/HDF01'
yearly_results_url = 'https://www.moneycontrol.com/financials/hdfcbank/consolidated-results/yearly/HDF01'

#create CSV file
dirname = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(dirname, 'balancesheet_' + stock_symbol + '.csv')
csv_writer = csv.writer(open(filename, 'w'))

#Get the HTML content of the page
r = requests.get(balancesheet_url)
htmlContent = r.content
soup = BeautifulSoup(htmlContent, 'html.parser')

table = soup.find('table', attrs={'class':'mctable1'})
#find all rows
rows = table.find_all('tr')
for row in rows:
    #get columns for each row
    cols = row.find_all('td')
    #get text from each column
    cols = [ele.text.strip() for ele in cols]
    #write to csv file
    csv_writer.writerow(cols)

#use ratio url
r = requests.get(ratio_url)
htmlContent = r.content
soup = BeautifulSoup(htmlContent, 'html.parser')

table = soup.find('table', attrs={'class':'mctable1'})
#find all rows
rows = table.find_all('tr')
for row in rows:
    #get columns for each row
    cols = row.find_all('td')
    #get text from each column
    cols = [ele.text.strip() for ele in cols]
    #write to csv file
    csv_writer.writerow(cols)

#use PNL url
r = requests.get(pnl_url)
htmlContent = r.content
soup = BeautifulSoup(htmlContent, 'html.parser')

table = soup.find('table', attrs={'class':'mctable1'})
#find all rows
rows = table.find_all('tr')
for row in rows:
    #get columns for each row
    cols = row.find_all('td')
    #get text from each column
    cols = [ele.text.strip() for ele in cols]
    #write to csv file
    csv_writer.writerow(cols)


#use yearly results url
r = requests.get(yearly_results_url)
htmlContent = r.content
soup = BeautifulSoup(htmlContent, 'html.parser')

table = soup.find('table', attrs={'class':'mctable1'})
#find all rows
rows = table.find_all('tr')
for row in rows:
    #get columns for each row
    cols = row.find_all('td')
    #get text from each column
    cols = [ele.text.strip() for ele in cols]
    #write to csv file
    csv_writer.writerow(cols)
    
#loop through the list of stock symbols
# for stock_symbol in stock_symbols:
#     url = 'https://www.screener.in/company/' + stock_symbol + '/consolidated/#balance-sheet'
    
#     r = requests.get(url)
#     htmlContent = r.content
#     soup = BeautifulSoup(htmlContent, 'html.parser')

#     dirname = os.path.dirname(os.path.abspath(__file__))
#     filename = os.path.join(dirname, 'balancesheet_' + stock_symbol + '.csv')
#     csv_writer = csv.writer(open(filename, 'w'))
#     #locate a section in soup with id
#     section = soup.find('section', attrs={'id':'balance-sheet'})

#     #locate a table in section with class
#     table = section.find('table', attrs={'class':'data-table responsive-text-nowrap'})

#     rows = table.find_all('tr')

#     for row in rows:
#         #First row has the column names
#         if row.find('th'):
#             cols = row.find_all('th')
#             cols = [ele.text.strip() for ele in cols]
#             csv_writer.writerow(cols)
#         else:
#             cols = row.find_all('td')
#             cols = [ele.text.strip() for ele in cols]
#             #Trim the special character from the first element of row
#             if(cols[0][-1] == '+'):
#                 cols[0] = (cols[0][:-2])
#             csv_writer.writerow(cols)





        
