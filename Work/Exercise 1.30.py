#Exercise 1.30

def portfolio_cost(filename):
    total_cost = 0.0
    with open('Data/portfolio.csv', 'rt') as f:
        headers = next(f)
        for line in f:
            row = line.split(',')
            nshares = int(row[1])
            price = float(row[2])
            total_cost = total_cost + nshares * price
    print('Total cost', total_cost)    
cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', total_cost)

