#Exercise 2.5

def read_portfolio(filename):
    import csv
    with open(filename, 'rt') as input:
        rows = csv.reader(input)
        headers = next(rows)
        list1 = []
        for row in rows:
            holding = {'name': row[0], 'shares' : int(row[1]), 'price' : float(row[2])}
            list1.append(holding)
        print(list1)

