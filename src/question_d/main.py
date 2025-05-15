#add import
from question_d import create_multiplication_table
from question_d import display_multiplication_table

def qd_menu():
    choice = 0
    while choice ==0:
        choice = int(input("Multiplication Table Menu\n1 Create Table-\n2-Exit\n"))
        while choice == 1:
            key= ''
            listx= []
            print('Enter values for the X-Axis.Type type n to move on.')
            while key!= 'n':
                key= input()
                if key != 'n':
                    listx.append(key)
            listy= []
            print('Enter values for the Y-Axis.Type type n to move on.')
            key= ''
            while key!= 'n':
                key= input()
                if key != 'n':
                    listy.append(key)
            print("Multiplication Table Result: ")
            display_multiplication_table(create_multiplication_table(listx,listy))
            exvar = input("Do you want to continue?\ny or n\n")
            if exvar == "y":
                choice = 1
            else:
                choice = 0
        if choice == 2:
            print("Exiting Program...")
            exit

qd_menu()