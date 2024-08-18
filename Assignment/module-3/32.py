my_dict = {'apple': 3, 'banana': 5, 'cherry': 2, 'date': 4}
sorted_dict_asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))
sorted_dict_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Ascending:", sorted_dict_asc)
print("Descending:", sorted_dict_desc)