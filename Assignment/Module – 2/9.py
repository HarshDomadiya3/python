# Write a Python program to sum of three given integers. However, if
# two values are equal sum will be zero.

a = int(input("Enter Value :-"))
b = int(input("Enter Value :-"))
c = int(input("Enter Value :-"))

if a == b or b == c or a == c:
     print("0")
else:
    print( a + b + c)