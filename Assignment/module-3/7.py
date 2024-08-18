# list=[1,1,2,3,4,4,5,5]
# unique=[]
# for i in list:
#     if i not in unique:
#         unique.append(i)
# print(unique)


list=[1,1,2,3,4,4,5,5]
def function(list):
    unique=[]
    for i in list:
        if i not in unique:
            unique.append(i)
    return unique
print(function(list))