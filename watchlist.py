#!/usr/bin/env python3

import urllib.request
import csv

exchanges = ['NASDAQ', 'NYSE', 'AMEX']

symbols = []

def filename_for_exchange(exchange):
    return 'companylist_%s.csv' % exchange

def download_file_for_exchange(exchange):
    url = 'https://www.nasdaq.com/screening/companies-by-region.aspx?exchange=%s&render=download' % exchange
    print('Downloading %s' % url)

    request = urllib.request.Request(url)
    
    file = open(filename_for_exchange(exchange), 'wb')
    with urllib.request.urlopen(request) as f:
        file.write(f.read())
    file.close()

def symbols_for_exchange(exchange):
    filename = filename_for_exchange(exchange)

    symbols = []

    with open(filename) as csvFile:
        csvReader = csv.reader(csvFile)
        for row in csvReader:
            if row[0] == 'Symbol': continue
            
            symbols.append(exchange + ':' + row[0].strip())
    
    return symbols

for exchange in exchanges:
    download_file_for_exchange(exchange)
    symbols = symbols_for_exchange(exchange)

    watchlist = open('watchlist_%s.txt' % exchange, 'w')
    watchlist.write(','.join(symbols))
    watchlist.close()
