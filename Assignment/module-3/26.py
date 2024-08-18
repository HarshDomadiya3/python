tuple_list = [(1, 2, 3)]
modified_list = []
for t in tuple_list:
    t = list(t)  
    t[-1] = 100  
    modified_list.append(tuple(t))
print("Modified List:", modified_list)
