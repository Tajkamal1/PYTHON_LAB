def perform_list_operations(my_list):
    modified_list = my_list.copy()
    modified_list.append(10)
    modified_list.insert(2, 5)
    sliced_list = modified_list[1:4]
    return modified_list, sliced_list

my_list = [1, 2, 3, 4]
modified_list, sliced_list = perform_list_operations(my_list)
print("Original list:", my_list)
print("Modified list:", modified_list)
print("Sliced list:", sliced_list)
