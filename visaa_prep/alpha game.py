def count_vowels_and_consonants(s):
    vowels = "aeiouAEIOU"
    vowels_count = 0
    consonants_count = 0
    
    for char in s:
        if char.isalpha(): 
            if char in vowels:
                vowels_count += 1
            else:
                consonants_count += 1

    print(f"{vowels_count},{consonants_count}")

s = input()


count_vowels_and_consonants(s)
