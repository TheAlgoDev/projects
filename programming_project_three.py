# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 19:18:26 2024

@author: Brent Thompson
"""
import sys
# Ask the user to enter their first name, last name, and age

first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
age = int(input('Enter your age: '))

# Concatenate the two names with one space between

full_name = (first_name + " " + last_name)
print(f'Thank you {first_name} for that information.')


# Create username using the data provided
user_name = (first_name.lower() + last_name[0].lower() + str(age))
print()
print()


# Prompt the user to start entering scores

print(f'{first_name}, Enter your three bowling scores...')
print()


score1 = int(input('What is the first score? :'))
score2 = int(input('What is the second score? :'))
score3 = int(input('What is the third score? :'))
print()

# Build a list out of the scores

score_list = [score1, score2, score3]

# Check the scores to check validity
for score in score_list:
    if (score < 0) or (score > 300):
        print(f'{score} is invalid, please enter a value 0-300')
        sys.exit('Program closing...')
    else:
        print('Valid score')
print()

# Run calculations on the list to get data

score_max = max(score_list)
score_min = min(score_list)
score_avg = sum(score_list) / float(len(score_list))

# Display the data in proper format

print(f'Your highest score was {score_max}.')
print(f'Your lowest score was {score_min}.')
print(f'Your average score was {int(score_avg)}.')

print('Here is a summary of your bowling stats')
print()

print(f'Player Name: {full_name}')
print(f'Username: {user_name}')

if score_avg < 81:
    print('Your skill level is Beginner')
elif score_avg < 176:
    print('Your skill level is Intermediate')
else:
    print('Your skill level is Advanced')
