# -*- coding: utf-8 -*-
"""
Brent Thompson
Introduction to programming concepts
Programming Project Four
3/13/2024
"""


def getInput():
    scores = []  # Lists are fun
    score = int(input("Please enter a bowling score (-1 to exit)"))
    while score != -1:  # Sentinal value is -1
        while score < 0 or score > 300:
            score = int(input("Please enter a valid number (0 to 300)"))
        scores.append(score)
        print("Score " + str(score) + " accepted.")
        score = int(input("Please enter another score (-1 to exit)"))
    return scores


def calculateAverage(scores):
    average = sum(scores) / len(scores)
    return average


def displayResults(scores, average):
    print("You bowled the folling scores: ")
    for score in scores:
        print(str(score))
    print("Your bowling average is {:.0f}".format(average))


bowlingScores = getInput()
average = calculateAverage(bowlingScores)
displayResults(bowlingScores, average)
