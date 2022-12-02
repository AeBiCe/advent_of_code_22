"""

Author: Nick
Version: 1.0
Date: 2022-12-02

"""


with open("input.txt", "r", encoding="utf-8") as data:
    games_played = [
        "".join(tuple(line.strip().replace(" ", ""))) for line in data.readlines()
    ]

points_from_games = sum(
    [6 for game in games_played if game in ["AY", "BZ", "CX"]]      # win 6p
    + [3 for game in games_played if game in ["AX", "BY", "CZ"]]    # draw 3p
)

my_moves = [my_move for (op_move, my_move) in games_played]
# rock 1p | paper 2p | scissors 3p
points_from_moves = sum(
    [my_moves.count("X") + my_moves.count("Y") * 2 + my_moves.count("Z") * 3]
)

print(f"Total points: {points_from_moves + points_from_games}")
