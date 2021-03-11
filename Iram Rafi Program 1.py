sentence = str(input("Enter a sentence: "))
vowels = {}
num = 0
for letter in sentence:
    if letter in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        num = num + 1
        vowels[letter] = vowels.get(letter, 0) + 1

print("\nTotal vowels in sentence: ", num)
print("\nVowels in sentence: ")
for vowel, num in vowels.items():
    print(vowel," : ", num)
