number = int(input("Enter a number: "))
total = 0
for i in range(1, number + 1):
    if number % i == 0:  
        total += i  
print(f"The sum of all divisors of {number} is {total}")