def is_perfect(number):
    if number <= 0:
        return False
    
    sum_of_divisors = 0
    for i in range(1, number):
        if number % i == 0:
            sum_of_divisors += i
    
    return sum_of_divisors == number
print(is_perfect(6)) 