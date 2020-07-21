#Exercise 1.30

def portfolio_cost(filename):
    import csv
    with open(filename, 'rt') as input:
        headers = next(input)
        total_cost = 0
        for line in input:
            row = line.split(',')
            total_cost += (int(row[1]) * float(row[2]))
        print('Total cost:', total_cost)


