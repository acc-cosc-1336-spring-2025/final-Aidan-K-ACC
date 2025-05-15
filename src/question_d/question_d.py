#write functions here, don't add input('') statements here!
def table(listx,listy):
    table= ''
    temp= ''
    for itemy in listy:
        for itemx in listx:
            temp+= str(itemy * itemx)+' '
        table+= temp +'\n'
        temp= ''
    return table
