# Write a Python program that will return true if the two given integer
# values are equal or their sum or difference is 5.

a = int(input("Enter Value :-"))
b = int(input("Enter Value :-"))

if a == b or (a + b) == 5 and (a - b) == 5:
    print("True")
else:
    print("False")