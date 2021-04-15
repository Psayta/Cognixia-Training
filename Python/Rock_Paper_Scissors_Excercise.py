Player1 = input("Please enter Rock(R), Paper(P) or Scissors(S): ") # Inputs for each player 
Player2 = input("Please enter Rock(R), Paper(P) or Scissors(S): ")


if (Player1 == 'R'): #if statements for player 1 selection
    print("Player 1 selected Rock")
elif(Player1 == 'P'):
    print("Player 1 selected Paper")
else:
    print("Player 2 selected Scissors")

if (Player2 == 'R'): #if statements for player 2 selection 
    print("Player 2 selected Rock")
elif(Player2 == 'P'):
    print("Player 2 selected Paper")
else:
    print("Player 2 selected Scissors")

if (Player1 == Player2): #The result of the player selection to determine the winner of RPS 
    print('Draw')
elif (Player1 == 'R' and Player2 == 'S'): 
    print ("Player 1 Wins")
elif (Player1 == 'S' and Player2 == 'P'): 
    print ("Player 1 Wins")
elif (Player1 == 'P' and Player2 == 'R'): 
    print ("Player 1 Wins")
else: 
    print("Player 2 Wins")
    
