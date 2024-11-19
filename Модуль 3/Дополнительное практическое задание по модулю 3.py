data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_sum(data_structure):
    summ = 0

    if isinstance(data_structure, (list, tuple, set)):
        for item in data_structure:
            summ += calculate_sum(item)
    elif isinstance(data_structure, dict):
        for key, value in data_structure.items():
            summ += calculate_sum(key)
            summ += calculate_sum(value)
    elif isinstance(data_structure, str):
        return len(data_structure)
    elif isinstance(data_structure, (int, float)):
        return data_structure
    return summ


result = calculate_sum(data_structure)

print(result)
