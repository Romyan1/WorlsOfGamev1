from pathlib import Path


def add_Score(difficulty):
    Points_Of_Winning = str((difficulty * 3) +5)
    try:
        score_file = open(Path("Score.txt"), "r")
        score = open(Path("Score.txt"), "a")
        score.write(f" ,{Points_Of_Winning}")
    except FileNotFoundError:
        score = open(Path("Score.txt"), "x")
        score.write(Points_Of_Winning)





