import requests
import csv
import os
from bs4 import BeautifulSoup

#popluate the list of stock symbols with Banks from BAnknifty nse website
stock_symbols = ['ICICIBANK', 'HDFCBANK', 'KOTAKBANK', 'AXISBANK', 'INDUSINDBK', 'BANDHANBNK', 'BANKBARODA', 'BANKINDIA', 'CANBK', 'FEDERALBNK', 'IDBI', 'IDFCFIRSTB', 'PNB', 'RBLBANK', 'SBIN', 'YESBANK']

#loop through the list of stock symbols
for stock_symbol in stock_symbols:
    url = 'https://www.screener.in/company/' + stock_symbol + '/consolidated/#balance-sheet'
    
    r = requests.get(url)
    htmlContent = r.content
    soup = BeautifulSoup(htmlContent, 'html.parser')

    dirname = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(dirname, 'balancesheet_' + stock_symbol + '.csv')
    csv_writer = csv.writer(open(filename, 'w'))
    #locate a section in soup with id
    section = soup.find('section', attrs={'id':'balance-sheet'})

    #locate a table in section with class
    table = section.find('table', attrs={'class':'data-table responsive-text-nowrap'})

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





        
