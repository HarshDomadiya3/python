def insert_in_middle(main_string, insert_string):
    middle_index = len(main_string) // 2
    result = main_string[:middle_index] + " " + insert_string + " " + main_string[middle_index:]
    
    return result
main_str = "helloworld"
insert_str = "beautiful"
print(insert_in_middle(main_str, insert_str))
