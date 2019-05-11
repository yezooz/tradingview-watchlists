#!/usr/bin/env python3

import csv

symbols = []
prefix = 'NASDAQ'

with open('companylist.csv') as csvFile:
    csvReader = csv.reader(csvFile)
    for row in csvReader:
        if row[0] == 'Symbol': continue
        
        symbols.append(prefix + ':' + row[0])

watchlist = open('watchlist_nasdaq.txt', 'w')
watchlist.write(','.join(symbols))
watchlist.close()
