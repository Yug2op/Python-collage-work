def count_vowels(text):
    vowels = "aeiouAEIOU" 
    vowel_count = {}  
    for char in text:  
        if char in vowels: 
            if char in vowel_count:
                vowel_count[char] += 1  
            else:
                vowel_count[char] = 1  

    for vowel, count in vowel_count.items():
        print(f"{vowel}: {count}")

text = input("Enter a string: ")
count_vowels(text)
