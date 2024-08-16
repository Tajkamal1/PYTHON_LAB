def sort_and_lowercase_words(source_file, destination_file):
    with open(source_file, 'r') as source:
        words = [word.strip().lower() for word in source]
    words.sort()
    with open(destination_file, 'w') as destination:
        for word in words:
            destination.write(word + '\n')

source_file = "original_words.txt"
destination_file = "sorted_lowercase_words.txt"
sort_and_lowercase_words(source_file, destination_file)
print("Words sorted and lowercased in", destination_file)
