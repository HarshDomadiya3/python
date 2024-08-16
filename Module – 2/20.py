def find_longest_word(words):
    max_length = 0
    for word in words:
        if len(word) > max_length:
            max_length = len(word) 
    return max_length

words_list = ["apple", "banana", "cherry", "blueberry"]
print(find_longest_word(words_list))