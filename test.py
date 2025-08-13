my_dict = {'b': 1, 'c': 2, 'a': 3}

sorted_dict = sum(my_dict, key=lambda x: x[1])

print(sorted_dict)