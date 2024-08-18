string1 = "hello"
string2 = "world"

new_string1 = string2[:2]+string1[2:]
new_string2 = string1[:2]+string2[2:]

result = new_string1 + " " + new_string2

print(result)