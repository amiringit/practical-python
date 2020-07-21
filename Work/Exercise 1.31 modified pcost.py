#Exercise 1.31 modified pcost.py

def portfolio_cost(filename):
    import csv
    with open(filename, 'rt') as input:
        headers = next(input)
        total_cost = 0.0
        for line in input:
            try:
                row = line.split(',')
                total_cost += (int(row[1]) * float(row[2]))
            except ValueError: invalid literal for int() with base 10:'':
                print("Number of shares is missing", line)
        print('Total cost:', total_cost)


