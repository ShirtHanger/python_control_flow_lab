# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
    dog_age = int(input("Give me your dog's age: "))
    # Declare conditional variables ahead of time
    subsequent_years = 0
    dog_years = 0
    
    
    if dog_age > 2:
        subsequent_years = dog_age - 2
        
    if subsequent_years > 0:
        dog_years = (2 * 10) + (subsequent_years * 7)
    else: 
        dog_years = dog_age * 10
    
    print(dog_years)
    # Your control flow logic goes here

# Call the function
calculate_dog_years()
