data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(data_structure):
    sum_item = 0
    for item in data_structure:
        if isinstance(item, int):
            sum_item += item
        elif isinstance(item, str):
            sum_item += len(item)
        elif isinstance(item, (list, tuple, set)):
            sum_item += calculate_structure_sum(item)
        elif isinstance(item, dict):
            sum_item += calculate_structure_sum(item.keys())
            sum_item += calculate_structure_sum(item.values())

    return sum_item

# def calculate_structure_sum(data_structure):
#     sum_item = 0
#     for item in data_structure:
#         if isinstance(item, int):
#             sum_item += item
#         elif isinstance(item, str):
#             sum_item += len(item)
#         elif isinstance(item, (list, tuple, set)):
#             sum_item += calculate_structure_sum(item)
#         elif isinstance(item, dict):
#             for key in item.keys():
#                 if isinstance(key, int):
#                     sum_item += key
#                 else:
#                     sum_item += len(key)
#             for value in item.values():
#                 if isinstance(value, int):
#                     sum_item += value
#                 else:
#                     sum_item += len(value)
#
#     return sum_item

result = calculate_structure_sum(data_structure)
print(result)
