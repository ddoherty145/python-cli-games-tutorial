# json import
import json

def start_game(greetings)
     
# open the file and parse the JSON
with open('me-capitals.json', 'r') as f:
    data = json.load(f)

total = len(data["cards"])
score = 0
#for loop here
for i in data["cards"]:
    guess = input(i["q"] + " > ")
    
    #if statement
    if guess.lower() == i["a"].lower():
        score += 1
        print(f"Correct! Current score: {score}/{total}")
    else:
        print("Incorrect! The correct answer was", i["a"])
        print(f"Current Score: {score}/{total}")

#returns final score and tells you how many questions you missed
if score == total:
        print(f"Congraulations! You got all questions correct!!")

else:
        print(f"Too bad you missed {total - score} better luck next time!")

