from itertools import product
data = {'1': ['a', 'b'], '2': ['c', 'd']}
letter_lists = [letters for letters in data.values()]
combinations = product(*letter_lists)
for combination in combinations:
    print(''.join(combination))