from pathlib import Path


def add_Score(difficulty):
    Points_Of_Winning = int((difficulty * 3) + 5)
    score = Points_Of_Winning
    try:
        with open(Path("Score.txt"), "r") as f:
            score_from_file = f.readlines()
            if len(score_from_file) > 0:
                score += int(score_from_file[0])
    finally:
        with open(Path("Score.txt"), "w+") as f:
            f.write(str(score))



                

