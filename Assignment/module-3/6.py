string=["level", "radar", "hello", "world", "noon", "a"]
count=0
for i in string:
    if len(i)>=2 and i[0]==i[-1]:
        count+=1
print(count)


