#write functions here, don't add input('') statements here!

class Stocks:
    def __init__(self, symbol, company_name):
        self.symbol= symbol
        self.company_name= company_name
    def get_symbol(self):
        return self.symbol
    def get_company_name(self):
        return self.company_name



def get_stock_list():
    stockdata= [Stocks('AAPL','Apple Inc'),Stocks('CAT','Caterpillar'),Stocks('EK','Eastman Kodak'),Stocks('GOOG','Google'),Stocks('MSFT','Microsoft')]
    stocklist= []
    templist= []
    for item in stockdata:
        stock=item
        templist.append(item.symbol)
        templist.append(item.company_name)
        stocklist.append(templist)
        templist= []
    return stocklist

