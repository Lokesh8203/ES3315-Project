import requests
import csv
import os
from bs4 import BeautifulSoup

#popluate the list of stock symbols with Banks from BAnknifty nse website

# stock_symbols = ['ICICIBANK', 'HDFCBANK', 'KOTAKBANK', 'AXISBANK', 'INDUSINDBK', 'BANDHANBNK', 'BANKBARODA', 'BANKINDIA', 'CANBK', 'FEDERALBNK', 'IDBI', 'IDFCFIRSTB', 'PNB', 'RBLBANK', 'SBIN', 'YESBANK']

#We need to get financial data from moneycontrol website

stock_symbol = 'hdfcbank'
ratio_url = 'https://www.moneycontrol.com/financials/hdfcbank/ratiosVI/HDF01'
balancesheet_url = 'https://www.moneycontrol.com/financials/hdfcbank/balance-sheetVI/HDF01'
pnl_url = 'https://www.moneycontrol.com/financials/hdfcbank/profit-lossVI/HDF01'
yearly_results_url = 'https://www.moneycontrol.com/financials/hdfcbank/consolidated-results/yearly/HDF01'

#create CSV file
dirname = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(dirname, 'final_balancesheet_' + stock_symbol + '.csv')
filename2 = os.path.join(dirname, 'balancesheet_' + stock_symbol + '.csv')
csv_writer = csv.writer(open(filename, 'w'))

balancesheet_url_page2 = 'https://www.moneycontrol.com/financials/hdfcbank/balance-sheetVI/HDF01/2#HDF01'

#Append data from page two to the same csv file
r = requests.get(balancesheet_url_page2)
htmlContent = r.content
soup = BeautifulSoup(htmlContent, 'html.parser')

table = soup.find('table', attrs={'class':'mctable1'})
#find all rows
rows = table.find_all('tr')
for row in rows:
    #find the same named row from previous csv file
    #traverse thorugh csv file and compare the first element of each row
    #if the first element of each row is same, then append the rest of the elements to the same row
    # print(filename)
    csv_traverse = csv.reader(open(filename2, 'r'))
    
    for csv_row in csv_traverse:
        #if csv_row had not element then skip
        if(len(csv_row) == 0):
            continue
        elif (csv_row[0] == row.find('td').text.strip()):
            print('I')
            #get columns for each row
            cols = row.find_all('td')
            #get text from each column
            cols = [ele.text.strip() for ele in cols]
            #write to csv file
            #remove the first element from the list
            cols.pop(0)
            csv_writer.writerow(csv_row + cols)




        
