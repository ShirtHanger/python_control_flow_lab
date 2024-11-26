# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall

months = [
    'jan', 'feb', 'mar', 
    'apr', 'may', 'jun', 
    'jul', 'aug', 'sep', 
    'oct', 'nov', 'dec'
    ]

complete_spring = ['apr', 'may']  # Mar 20 - Jun 20
complete_summer = ['jul', 'aug']  # Jun 21 - Sep 21
complete_fall = ['oct', 'nov']    # Sep 22 - Dec 20
complete_winter = ['jan', 'feb']  # Dec 21 - Mar 19

def determine_season():
    
    season = ''
    
    month = input('Enter the month (Jan-Dec): ').lower()
    while month not in months:
        month = input('Invalid month, again: ').lower()
    day = int(input(f'Enter the day of the month of {month}: '))
    while day < 1 and day > 31:
        int(input(f'Invalid date, again: '))
    
    # First check if the month is in a completely covered month
    
    if month in complete_spring:
        season = 'spring'
    elif month in complete_summer:
        season = 'summer'
    elif month in complete_fall:
        season = 'fall'
    elif month in complete_winter:
        season = 'winter'
        
    # Then check for the in betweens
    
    # Mar 20 - Jun 20
    elif month == 'mar':
        if day < 20:
            season = 'winter' 
        else:
            season = 'spring'
            
    # Jun 21 - Sep 21
    elif month == 'jun':
        if day < 21:
            season = 'spring'
        else:
            season = 'summer'
            
    # Sep 22 - Dec 20
    elif month == 'sep':
        if day < 22:
            season = 'summer'
        else:
            season = 'fall'
            
    # Dec 21 - Mar 19
    elif month == 'dec':
        if day < 21:
            season = 'fall'
        else:
            season = 'winter' 
    
    print(f'{month} {day} is in the {season}')

# Call the function
determine_season()
