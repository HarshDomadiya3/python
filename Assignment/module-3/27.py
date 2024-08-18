tuple=(1,1,2,2,3,4)
count=set()
for i in tuple:
    if tuple.count(i)>1:
        count.add(i)
print(list(count))
