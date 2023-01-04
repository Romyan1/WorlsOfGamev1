import os
from pathlib import Path
Score_File_Name = open (Path("Score.txt"), "x") #open and read file
#print(Score_File_Name.read())
Bad_Return_Code = int(404)
Clear_Screen = os.system('cls' if os.name == 'nt' else 'clear')
