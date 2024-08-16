def reverse_if_multiple_of_4(string):
    if len(string) % 4 == 0:
        return string[::-1]
    else:
        return string
print(reverse_if_multiple_of_4("abcd"))