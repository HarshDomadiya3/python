tuple_list=[(1,2),(),(3,4)]
list=[]
for i in tuple_list:
    if i != () :
        list.append(i)
print(list)
