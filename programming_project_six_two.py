# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 10:59:32 2024
Brent Thompson
Introduction to Programming Concepts
Programming Project Six
"""


def part_two():
    my_dictionary = {
        'First-Name': 'Brent',
        'Last-Name': 'Thompson',
        'Age': '27',
        'Hometown': 'Cocoa',
        'Favorite-food': 'Ice-Cream'
    }
    for key, value in my_dictionary.items():
        print(f"{key} {value},")
    print()
    my_dictionary['Age'] = '28'
    for key, value in my_dictionary.items():
        print(f"{key} {value},", end='')
    print()
    del my_dictionary['Favorite-food']
    print()
    for key in my_dictionary.keys():
        print(key)
    print()
    for value in my_dictionary.values():
        print(value)

    choice = input("Would you like to recieve encouragement?\n")
    if choice.lower() == 'yes':
        print("You are doing great and i'm thankful for you!")
    else:
        print("Thank you for your time!")


part_two()
