def count_vowels(text):
    vowels = 'aeiouAEIOU'
    return sum(c in vowels for c in text)

text = "This is a sample string"
vowel_count = count_vowels(text)
print("Number of vowels:", vowel_count)
