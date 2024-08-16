def returnSum(dict):
    total = 0
    for value in dict.values():
        total += value
    return total

dict = {'a': 100, 'b': 200, 'c': 300}
print("Sum:", returnSum(dict))
