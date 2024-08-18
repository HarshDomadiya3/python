string = "play"

if len(string) >= 3:
    if string.endswith("ing"):
        string += "ly"
    else:
        string += "ing"
print(string)