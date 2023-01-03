

def add_Score(difficulty):
    Points_Of_Winning = (difficulty * 3) +5
    try:
        with open("Score.txt", "r")as f: #f=open("Score.txt", "r")
            f.read()
    except FileNotFoundError:
        score = 0

    scores =+ Points_Of_Winning

    with open("Score.txt", "w")as f:
        f.write(str(scores))

    with open("Score.txt", "r") as f:  # f=open("Score.txt", "r")
        f.read()



