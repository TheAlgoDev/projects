# -*- coding: utf-8 -*-
"""
Created on Tue March 20 19:18:26 2024

@author: Brent Thompson
"""


def get_user_info():
    first_name = input('Enter your first name: \n')
    last_name = input('Enter your last name: \n')
    age = int(input('Enter your age: \n'))
    print(f'Thank you {first_name} for that information.... \n')

    return (first_name, last_name, age)
# This function gathers the users info to create username


def create_username(first_name, last_name, age):
    user_name = (first_name.lower() + last_name[0].lower() + str(age))
    return user_name
# Uses the inputs to create a username


def get_score_info():
    scores = []  # Lists are fun
    score = int(input("Please enter a bowling score (-1 to exit) \n"))
    while score != -1:  # Sentinal value is -1
        while score < 0 or score > 300:
            score = int(input("Please enter a valid number (0 to 300)\n"))
        scores.append(score)
        print("Score of " + str(score) + " accepted.")
        score = int(input("Please enter another score (-1 to exit)\n"))
    return scores
# Collects any number of scores from the user


def output_stats(scores):
    # Run calculations on the list to get data
    score_max = max(scores)
    score_min = min(scores)
    score_avg = int(sum(scores) / float(len(scores)))
# Display the data in proper format
    print('Here is a summary of your bowling stats: \n')
    print(f'Your highest score was {score_max}.')
    print(f'Your lowest score was {score_min}.')
    print(f'Your average score accross {len(scores)} games was {score_avg}.\n')
    return score_avg


def get_skill_level(score_avg):
    if score_avg < 81:
        skill_level = 'Beginner'
    elif score_avg < 176:
        skill_level = 'Intermediate'
    else:
        skill_level = 'Advanced'
    return skill_level
# Calculates the skill level from the score average


def main_program():

    user_info = get_user_info()
    user_name = create_username(user_info[0], user_info[1], user_info[2])
    print(f'Your username is {user_name}. \n')
    scores = get_score_info()
    stats = output_stats(scores)
    skill_level = get_skill_level(stats)
    print(f"Your skill level is {skill_level}, you're doing great!")
# Main program just uses the other functions in a particular order


main_program()
