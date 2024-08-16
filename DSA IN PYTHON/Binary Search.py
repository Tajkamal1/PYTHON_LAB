def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Example usage


arr = [1, 2, 3, 4, 5, 6, 7]
target = 4
position = binary_search(arr, target)
if position != -1:
    print(f"Position: {position + 1}")
else:
    print("Element not found")