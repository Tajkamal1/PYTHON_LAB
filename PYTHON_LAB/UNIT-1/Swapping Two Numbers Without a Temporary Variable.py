def swap(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
x, y = swap(x, y)
print(f"After Swapping: x = {x}, y = {y}")
