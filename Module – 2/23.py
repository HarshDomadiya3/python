string = "hi"
if len(string) < 2:
    result = string
else:
    result = string[:2] + string[-2:]
print(result)