def perform_list_operations(my_list):
    list_length = len(my_list)
    sorted_list = sorted(my_list)
    minimum_value = min(my_list)
    maximum_value = max(my_list)
    list_sum = sum(my_list)
    return list_length, sorted_list, minimum_value, maximum_value, list_sum

my_list = [5, 2, 8, 1, 3]
results = perform_list_operations(my_list)
print("Original list:", my_list)
print("Length:", results[0])
print("Sorted list:", results[1])
print("Minimum value:", results[2])
print("Maximum value:", results[3])
print("Sum:", results[4])
