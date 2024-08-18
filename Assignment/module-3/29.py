tuple_list = [(1, 'a', 3.5), (2, 'b', 4.5), (3, 'c', 5.5)]

# Use zip to unzip the list of tuples into individual lists
list1, list2, list3 = zip(*tuple_list)

# Convert tuples to lists
list1 = list(list1)
list2 = list(list2)
list3 = list(list3)

# Print the individual lists
print("List 1:", list1)
print("List 2:", list2)
print("List 3:", list3)