def check_key_exists(my_dict, key):
    return key in my_dict

my_dict = {"name": "Alice", "age": 30, "city": "New York"}
key_to_check = "age"
if check_key_exists(my_dict, key_to_check):
    print("Key", key_to_check, "exists in the dictionary.")
else:
    print("Key", key_to_check, "does not exist in the dictionary.")
