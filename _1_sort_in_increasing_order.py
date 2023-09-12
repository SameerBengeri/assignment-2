def get_last_element(tuple):
    return tuple[-1]
tuple_list = [(1, 3), (2, 2), (4, 1), (3, 5)]
sorted_list = sorted(tuple_list, key=get_last_element)
print("Sorted list in increasing order by the last element:")
print(sorted_list)
