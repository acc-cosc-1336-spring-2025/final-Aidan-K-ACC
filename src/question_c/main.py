#add import
from question_c import get_stock_list

def qc_menu():
    choice = 0
    while choice ==0:
        choice = int(input("Stock List Menu\n1 Display Stock Purchase History-\n2-Exit\n"))
        while choice == 1:
            stocklist= get_stock_list()
            for stock in stocklist:
                print(stock[0]+' '+stock[1]+'\n')
            choice = 0
        if choice == 2:
            print("Exiting Program...")
            exit

qc_menu()