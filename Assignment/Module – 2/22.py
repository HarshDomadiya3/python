string = "hello"

if len(string) < 2:
    result = ""
else:
    result = string[:2] + string[-2:]

print(result)