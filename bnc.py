#Import the random library
from random import randint

#make an array
roles = ["Bear", "Ninja" , "Cowboy"]
player = False

#start game 
start_game = input("Would you like to play Bear, Ninja, Cowboy? (yes/no) > ").lower()
if start_game == 'yes':
   player = False
   computer = roles[randint(0,2)]
else:
   print("Okay! Maybe next time!")
   exit()#exit the program

while player == False:
  player = input("Bear, Ninja, or Cowboy? > ").capitalize()
  computer = roles[randint(0,2)]
  if computer == player:
    print("DRAW!!")
  elif computer == "Cowboy":
    if player == "Bear":
      print("You lose!", computer, "shoots", player)
    else: # computer is cowboy, player is ninja
      print("You win!", player, "sneaks up on", computer)
  elif computer =="Bear":
    if player =="Cowboy":
        print("You win!", player, "shoots", computer)
    else: # computer is bear, player is ninja
        print("You lose!", player, "is eaten by" , computer)
  elif computer == "Ninja":
    if player == "Cowboy":
          print("You lose!", player, "is caught by surprise by", computer)
    else: # computer is ninja, player is bear
        print("You win!", player, "eats", computer)

  player = False
  computer = roles[randint(0,2)]

  #ask to play again
  play_again = input("Would you like to play again? (yes/no) > ").lower()
  #reset player to false
  if play_again == 'yes':
    player = False
    computer = roles[randint(0,2)]
  else:
    print("Thank you for playing!!")
    break 
    #breaks out of the loop