# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

vowels = ['a', 'e', 'i', 'o', 'u']

def check_letter():
    
    user_input = input('Give us a letter from A-Z: ')
    while len(user_input) > 1:
        user_input = input('... a singular letter: ')
    if user_input.lower() in vowels:
        print(f'{user_input} is a vowel')
    else:
        print(f'{user_input} is a consonant')

# Call the function

check_letter()
