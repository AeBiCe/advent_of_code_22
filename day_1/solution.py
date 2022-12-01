"""

Author: Nick
Version: 1.0
Date: 2022-12-01

"""


with open("input.txt", "r", encoding="utf-8") as data:
    gathered_calories = [line.strip() for line in data.readlines()]


calories = 0
elfs = []


for calorie in gathered_calories:
    if calorie == "":
        elfs.append(calories)
        calories = 0
    else:
        calories += int(calorie)

elfs.sort()
print(f"Highest: {elfs[-1]}")
