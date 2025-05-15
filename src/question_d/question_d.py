#write functions here, don't add input('') statements here!
def create_multiplication_table(listx,listy):
    table_list= []
    templist= []
    for itemy in listy:
        for itemx in listx:
            templist.append(str(int(itemy)*int(itemx)))
        table_list.append(templist)
        templist= []
    return table_list

def display_multiplication_table(table_list):
    table= ''
    for row in table_list:
        for item in row:
            table+= item + ' '
        table+= '\n'
    print(table)
