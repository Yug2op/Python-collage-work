#1. Write a menu driven program for the given string input : "This is Simple string":
#a Display Lenght
#b display count of character 's'
#c to split the string
#d If the given string has captaial letter then convert it into lower case

#2. Input a string and remove duplicate words from it.
#3. Display the string in reverse order consdring every word.
#4. Count the number of occurence of each vowel and consonant in the string.
#5. Check weather the string is palindrome or not.
#6. Input a string and convert ervery alertnate char to capital case.
#7. Input a string and count the uppercase letter and lowercase letter. and display


# Answer1

# String = input("Enter a Simple string:")
# print(f"Length of the string is:{len(String)}")
# print(f"You have entered s for {String.lower().count("s")} times" )
# print(f"{String.split()}")
# print(f"The given String is in LowerCase now: {String.lower()}")


# NewString =input("Enter a new string HERE:")
# lettersOfNewString = list(NewString)
# letterToCount = input("Enter a letter to count its number of occrence:")
# letterCount = NewString.count(letterToCount)
# print(f"You have entered {letterToCount} {letterCount} times.")

# Answer2 Input a string and remove duplicate words from it.

Test = input("Entre a simple String:")
count = Test.split()
for word in count:
    if word not in count:
        print(word)
    else:
        print("")    

