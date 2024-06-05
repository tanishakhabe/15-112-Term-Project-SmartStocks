#Creating a 'database' or class to organize the different attributes of the stocks. 
import csv

class Stock: 
    def __init__(self, name, symbol, price, sector, risk, description):
        self.name = name
        self.symbol = symbol
        # self.logo =  logo
        self.price = float(price)
        self.sector = sector
        self.risk = risk
        self.description = description

    def __repr__(self):
        return f'{self.name}'

def readStocksFromCSV(filename):
    stocksList = []

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            stock = Stock(
                name = row[0],
                symbol = row[1],
                # logo = row[x],
                price = float(row[2]),
                sector = row[3],
                risk = row[4],
                description = row[5],
            )
            stocksList.append(stock)
    return stocksList

stockFile = 'stocks.csv'
stocksList = readStocksFromCSV(stockFile)

tesla = stocksList[0]
adobe = stocksList[1]
apple = stocksList[2]
microsoft = stocksList[3]
moderna = stocksList[4]
pfizer = stocksList[5]
jnj = stocksList[6]
block = stocksList[7]
paypal = stocksList[8]
boa = stocksList[9]
elf = stocksList[10]
costco = stocksList[11]
pepsi = stocksList[12]
meta = stocksList[13]
spotify = stocksList[14]
atat = stocksList[15]

def readGraphFromCSV(filename):
    companyGraph = {}

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            companyName = row[0]
            prices = [float(price) for price in row[1:]]
            companyGraph[companyName] = prices
    return companyGraph

graphFile = 'stocks - graph.csv'
pricesDict = readGraphFromCSV(graphFile)