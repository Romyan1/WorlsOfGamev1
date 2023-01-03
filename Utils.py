import os

Score_File_Name = open("Score.txt", "r") #open and read file
#print(Score_File_Name.read())
Bad_Return_Code = 404
Clear_Screen = os.system('cls' if os.name == 'nt' else 'clear')
