# list=[1,2]
# if len(list)>=0:
#     print("not empty")

def is_list_empty(lst):
    # Check if the list is empty
    return len(lst) == 0

# Example usage
my_list = []

if is_list_empty(my_list):
    print("The list is empty.")
else:
    print("The list is not empty.")
    