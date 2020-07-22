# Exercise 2.4
# report.py

def read_portfolio(filename):
    import csv
    with open(filename, 'rt') as input:
        rows = csv.reader(input)
        headers = next(rows)
        list1 = []
        for row in rows:
            holding = (row[0], int(row[1]), float(row[2]))
            list1.append(holding)
        print(list1)

