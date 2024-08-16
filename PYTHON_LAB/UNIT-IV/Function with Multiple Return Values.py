def calculate_val(num1, num2):
    sum = num1 + num2
    difference = num1 - num2
    product = num1 * num2
    return sum, difference, product

result = calculate_val(10, 5)
print("Sum:", result[0])
print("Difference:", result[1])
print("Product:", result[2])
