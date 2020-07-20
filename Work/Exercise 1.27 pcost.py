#Exercise 1.27

import csv

with open('Data/portfolio.csv', 'rt') as file:
    headers = next(file)
    total_cost = 0.0
    for line in file:
        row = line.split(',')
        total_cost = total_cost + (int(row[1]) * float(row[2]))
    print('Total Cost:', total_cost)

