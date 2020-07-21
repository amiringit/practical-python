#Exercise 1.33



def portfolio_cost(filename):
    import csv
    import sys
    with open(filename, 'rt') as input:
        headers = next(input)
        total_cost = 0
        for line in input:
            row = line.split(',')
            total_cost += (int(row[1]) * float(row[2]))
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
print('Total cost:', total_cost)


