from collections import defaultdict
data = [
    {'item': 'item1', 'amount': 400},
    {'item': 'item2', 'amount': 300},
    {'item': 'item1', 'amount': 750}
]
combined = defaultdict(int)
for entry in data:
    item = entry['item']
    amount = entry['amount']
    combined[item] += amount
combined_dict = dict(combined)
print(combined_dict)