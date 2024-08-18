my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
keys_to_check = ['name', 'age', 'city']
all_keys_present = True
for key in keys_to_check:
    if key not in my_dict:
        all_keys_present = False
        break

if all_keys_present:
    print("All keys are present.")
else:
    print("Some keys are missing.")