vowels = ['a', 'e', 'i', 'o', 'u']

word = input("Provide a word to search for vowels: ")

for letter in word:
    if letter in vowels:
        print(letter)
