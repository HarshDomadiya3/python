# Write a Python program to get the Fibonacci series of given range.


a=0
b=1
d=10
for i in range(1,d+1):
    c=a+b
    a=b
    b=c
    print(c) 