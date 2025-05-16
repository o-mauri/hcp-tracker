from datetime import datetime
import json
import math
from utils import calculate_handicap
print("Adding round information")

print()
while True:
    date = input("Enter the date of the round (YYYY-MM-DD): ")
    if len(date) == 10 and date[4] == '-' and date[7] == '-':
        try:
            datetime.strptime(date, '%Y-%m-%d')
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
    else:
        print("Invalid date format. Please use YYYY-MM-DD.")

print()
while True:
    parScore = input("Enter par score: ")
    if parScore.isdigit() and 54 <= int(parScore) <= 80:
        parScore = int(parScore)
        break
    else:
        print("Invalid par score. Please enter a number between 54 and 80.")


print()
while True:
    course = input("Enter course rating: ")
    try:
        course_val = float(course)
        if 50 <= course_val <= 100:
            course = course_val
            break
        else:
            print("Invalid course rating. Please enter a number between 50 and 100.")
    except ValueError:
        print("Invalid course rating. Please enter a number between 50 and 100.")

print()
while True:
    slope = input("Enter slope rating: ")
    if slope.isdigit() and 100 <= int(slope) <= 160:
        slope = int(slope)
        break
    else:
        print("Invalid slope rating. Please enter a number between 100 and 160.")

lastHcp = 54.0

with open('differentials.json', 'r') as file:
    data = json.load(file)

    data.sort(key=lambda x: x['date'], reverse=True)
    if len(data) > 2:
        lastHcp = data[0]['HCPafter']

print()
print(f"Handicap prior to round: {lastHcp}")
print("------------------------------------")

print()

print(lastHcp)

playingHcp = round((lastHcp * (float(slope) / 113.0)) + (float(course) - float(parScore)), 1)

print()
print("------------------------------------")
print(f"Playing Handicap for this round: {playingHcp}")
print("------------------------------------")

hole_pars = []
hole_indexes = []

raw_scores = []
adjusted_scores = []

for i in range(18):
    print()
    print()
    print(f"Hole {i+1}")
    print("------------------------------------")

    while True:
        hole_par = input("Enter par: ")
        if hole_par.isdigit() and 1 <= int(hole_par) <= 10:
            hole_par = int(hole_par)
            break
        else:
            print("Invalid par. Please enter a number between 1 and 10.")
    while True:
        hole_index = input("Enter hole stroke index: ")
        if hole_index.isdigit() and 1 <= int(hole_index) <= 18:
            hole_index = int(hole_index)
            break
        else:
            print("Invalid hole stroke index. Please enter a number between 1 and 18.")
            
    hole_pars.append(hole_par)
    hole_indexes.append(hole_index)


    tot = int(playingHcp)
    p1 = math.floor(tot / 18)
    p2 = tot % 18

    if hole_index <= p2:
        holeStrokes = p1 + 1
    else:
        holeStrokes = p1

    hole_max = hole_par + 2 + holeStrokes

    print(f"Strokes on this hole: {holeStrokes}")

    while True:
        raw_score = input("Enter score: ")
        if raw_score.isdigit() and 1 <= int(raw_score):
            raw_score = int(raw_score)
            break
        else:
            print("Invalid score. Please enter a number greater than 0.")

    raw_scores.append(raw_score)

    adjusted_score = min(raw_score, hole_max)
    print()
    print(f"Adjusted score on hole {i+1}: {adjusted_score}")
    print("------------------------------------")
    adjusted_scores.append(adjusted_score)


totalRoundScore = sum(raw_scores)
totalAdjustedScore = sum(adjusted_scores)

print()
print("------------------------------------")
print(f"Total round score: {totalRoundScore}")
print(f"Total adjusted score: {totalAdjustedScore}")
print("------------------------------------")

differential = (113/slope) * (totalAdjustedScore - course)

print()
print("------------------------------------")
print(f"Round differential: {differential}")
print("------------------------------------")

roundDict = {
    "date": date,
    "differential": differential,
    "courseRating": course,
    "slopeRating": slope,
    "score": totalRoundScore,
    "HCPbefore": lastHcp
}

sample = data.copy()
sample.append(roundDict)

newHcp = calculate_handicap(sample)

print()
print("------------------------------------")
print(f"New handicap: {newHcp}")
print("------------------------------------")


roundDict["HCPafter"] = newHcp

data.append(roundDict)

with open('differentials.json', 'w') as file:
    json.dump(data, file, indent=4)
