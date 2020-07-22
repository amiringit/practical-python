#Exercise 2.6

def read_prices(filename):
    import csv
    with open(filename , 'rt') as f:
        empty = {}
        rows = csv.reader(f)
        for row in rows:
            try:
                holding = {'name' : row[0], 'shares' : int(row[1]), 'price' : float(row[2])}
                empty.insert(holding)
            except ValueError:
                print(row)
    print(empty)

