value=[1,2,3,3,2,1]
def function(list):
    unique=[]
    for i in value:
        if i not in unique:
            unique.append(i)
    return unique
print(function(list))




# unique_list=list(set(value))
# print(unique_list)