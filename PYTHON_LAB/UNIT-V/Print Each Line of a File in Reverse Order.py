def print_lines_in_reverse(filename):
    try:
        with open(filename, 'r') as file:
            reversed_lines = [line[::-1].strip() for line in reversed(file.readlines())]
        for line in reversed_lines:
            print(line)
    except FileNotFoundError as e:
        print(f"Error: File '{filename}' not found.")

filename = "sample_file.txt"
print_lines_in_reverse(filename)
