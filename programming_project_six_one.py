# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 10:59:32 2024
Brent Thompson
Introduction to Programming Concepts
Programming Project Six
"""


def collect_input():
    print("Please enter eight numbers, one at a time \n")
    number_list = []  # Create list to add inputs
    while len(number_list) < 8:
        for i in input("Enter a number: ").split():
            number_list.append(int(i))
    return number_list


def sort_input(number_list):
    sorted_list = number_list[:]
    sorted_list = sorted(sorted_list, reverse=True)
    return sorted_list


def display_input(number_list):
    for i in number_list:
        print(i, end='    ')
    print()


def add_list(number_list):
    total = sum(number_list)
    print(f"The sum total of the list is {total:.2f}\n")
    return total


def average_list(number_list, total):
    average = total / len(number_list)
    print(f"The average of the list is {average:.2f}\n")
    return average


def higher_than_average(number_list, average):
    higher = [i for i in number_list if i > average]
    print("Here are numbers higher than the average: ")
    for i in higher:
        print(i, end='          ')


def part_one():
    number_list = collect_input()
    print("\nCalculations in progress...\n")
    sorted_list = sort_input(number_list)
    total = add_list(number_list)
    average = average_list(number_list, total)
    print("Here are the numbers you entered")
    display_input(number_list)
    display_input(sorted_list)
    add_list(number_list)
    average_list(number_list, total)
    higher_than_average(number_list, average)


part_one()
