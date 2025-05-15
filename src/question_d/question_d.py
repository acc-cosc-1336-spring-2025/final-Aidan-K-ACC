#write functions here, don't add input('') statements here!
def table(list1,list2):
    table= ''
    temp= ''
    for item1 in list1:
        for item2 in list2:
            temp+= str(item1 * item2)+' '
        table+= temp +'\n'
        temp= ''
    return table


list1= [1,2,3,4,5,6,7,8,9,10]
list2= [1,2,3,4,5,6,7,8,9,10]
print(table(list1,list2))