"""

Author: Nick
Version: 1.0
Date: 2022-12-03

"""


with open("input.txt", "r", encoding="utf-8") as data:
    games_played = [
        "".join(tuple(line.strip().replace(" ", ""))) for line in data.readlines()
    ]

second_column = [moves[1] for moves in games_played]

strategy_one_points = sum( # Strategy 1
      [6 for game in games_played if game in ["AY", "BZ", "CX"]]  # win 6p
    + [3 for game in games_played if game in ["AX", "BY", "CZ"]]  # draw 3p
    + [second_column.count("X") + second_column.count("Y") * 2 + second_column.count("Z") * 3]
)

strategy_two_points = sum( # Strategy 2
      [1 for game in games_played if game == "BX"]
    + [2 for game in games_played if game == "CX"]
    + [3 for game in games_played if game == "AX"]
    + [4 for game in games_played if game == "AY"]
    + [5 for game in games_played if game == "BY"]
    + [6 for game in games_played if game == "CY"]
    + [7 for game in games_played if game == "CZ"]
    + [8 for game in games_played if game == "AZ"]
    + [9 for game in games_played if game == "BZ"]

)

print(f"Strategy one: {strategy_one_points} | Strategy two: {strategy_two_points}")
