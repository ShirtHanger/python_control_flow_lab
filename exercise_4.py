# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

yes_inputs = ['yes', 'y']
no_inputs = ['no', 'n']

valid_inputs = yes_inputs + no_inputs
invalid_message = '"Yes" or "No" only: '

def weather_advice():
    # Your control flow logic goes here
    
    cold = input('Is it cold: ').lower()
    while cold not in valid_inputs:
        cold = input(invalid_message)
        
    raining = input('Is it raining: ').lower()
    while raining not in valid_inputs:
        raining = input(invalid_message)
        
    if cold in yes_inputs:
        
        if raining in yes_inputs:
            print('Wear a waterproof coat.')
        else: # Cold and not raining
            print('Wear a warm coat')
            
    else: #It's warm
        if raining in yes_inputs:
            print('Carry an umbrella')
        else: # Warm and not raining
            print('Wear light clothing.')
    

# Call the function
weather_advice()
