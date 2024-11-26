import random

# Exercise 7: Number Guessing Game
#
# Write a Python function named `guess_number` that allows a user to guess a predetermined number within a range.
#
# Requirements:
# - Set a fixed number as the target for guessing (e.g., 42).
# - Prompt the user to guess a number within a range (e.g., 1 to 100).
# - Allow the user to guess up to five times.
# - After each guess, use conditional statements with AND, OR, and NOT to give the user hints like:
#   - "Guess is too low" or "Guess is too high."
#   - "Last chance!" when they are on their fifth guess.
# - Print "Congratulations, you guessed correctly!" if they guess the number.
# - Print "Sorry, you failed to guess the number in five attempts." if they do not succeed.
#
# Hints:
# - Use a for loop with a range to limit guesses to five.
# - Use logical AND, OR, and NOT to check conditions and provide appropriate feedback.



# These are here to add flavor

responses = ['So close!', "That ain't it", "Wrong!", "Nope", "Nah"]

re_prompts = ['1-100: ', 'Try again: ', 'You got this!:', 'Again!: ']

last_chances = ['Everything is riding on this: ', 'Last chance! ', "What's 9 + 10? ", 'Guess wrong and you will never see him again... ']

def guess_number():
    # Defining variables
    answer = 21
    attempts = 1
    
    # I've been known about input so this was easy
    guess = int(input(f'Gimme me a number between 1 to 100: '))
    
    # Initially had attempts > 5 🤦🏾‍♂️
    while guess != answer and attempts < 5:
        
        attempts += 1
        # Some flavor to the responses
        response = random.choice(responses)
        re_prompt = random.choice(re_prompts)
        last_chance = random.choice(last_chances)
        # last_chance = last_chances[2]
        
        if guess > answer:
            print(response, 'Its too low!')
        else:
            print(response, 'Its too high!')
        
        if attempts == 5:
            guess = int(input(last_chance))
        else:
            guess = int(input(re_prompt))
        
    # You know the vine
    if last_chance == last_chances[2] and guess == answer:
        print('You stupid!')
        if guess == answer:
            print('... jk you got it')
        else:
            print(f'Its {answer}, not {guess}, joking btw')
        return 
        
    if attempts > 5:
        print(f'Out of attempts! The answer was {answer}')
    elif attempts <= 5 and attempts > 1:
        print(f'Nice! It only took yah {attempts} time(s)')
    else:
        print(f'First try!')

# Call the function
guess_number()

