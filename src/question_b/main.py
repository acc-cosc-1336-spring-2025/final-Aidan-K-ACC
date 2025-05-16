#add import
from question_b import get_most_likely_ancestor_consensus, validate_sequence, validate_subsequence

def qb_menu():
    choice = 0
    while choice ==0:
        choice = int(input("DNA Sequence Match Menu\n1 Enter Sequence-\n2-Exit\n"))
        while choice == 1:
            key= ''
            string= ''
            print('Enter a DNA sequence between 9 and 16 characters long. Press enter and ype n to move on.')
            while key!= 'n':
                    key= input()
                    if key != 'n':
                        string+= str(key)
            
            
            substring= ''
            print('Enter a 4 character subsequence. Press enter and ype n to move on.')
            key= ''
            while key!= 'n':
                key= input()
                if key != 'n':
                    substring+= str(key)
            if validate_sequence(string)==False or validate_subsequence(substring)==False:
                print('Invalid input. Please try again.')
                choice= 1
            if validate_sequence(string)==True or validate_subsequence(substring)==True:
                print("Match Results: ")
                print(get_most_likely_ancestor_consensus(string,substring))
            exvar = input("Do you want to continue?\ny or n\n")
            if exvar == "y":
                choice = 1
            else:
                choice = 0
        if choice == 2:
            print("Exiting Program...")
            exit

qb_menu()