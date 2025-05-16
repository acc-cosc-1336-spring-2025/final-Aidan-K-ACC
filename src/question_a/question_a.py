#write functions here, don't add input('') statements here!
def test_config():
    return True

class Stocks:
    def __init__(self, symbol, company_name):
        self.symbol= symbol
        self.company_name= company_name
    def get_symbol(self):
        return self.symbol
    def get_company_name(self):
        return self.company_name



def get_stock_list():
    stocklist= [Stocks('AAPL','Apple Inc'),Stocks('CAT','Caterpillar'),Stocks('EK','Eastman Kodak'),Stocks('GOOG','Google'),Stocks('MSFT','Microsoft')]
    return stocklist

def display_stock_list(list):
    stocklist= []
    templist= []
    for item in list:
        stock=item
        templist.append(item.symbol)
        templist.append(item.company_name)
        stocklist.append(templist)
        templist= []
    return stocklist

print(display_stock_list(get_stock_list()))