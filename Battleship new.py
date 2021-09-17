from random import randint

#Create the list where the game board will be created and stores
board = []

#Add an "O" as a placeholder for each location on the map
for a in range(5):
  board.append(["O "] * 5)

#Create functions to assign a random location for the battleship
def rand_row(board):
  return randint(0, len(board) - 1)

def rand_col(board):
  return randint(0, len(board[0]) - 1)

#Create a function that puts together and prints the map using .join()
def print_map(board):
  for line in board:
    print " ".join(line)

print_map(board)

ship_x = rand_row(board)
ship_y = rand_col(board)

#Everything within this loop repeats for each turn
for turn in range(5):
  print "Turn", turn + 1

  #Take the user's guess for the row and column of the battleship
  user_x = int(raw_input("Guess Row: "))
  user_y = int(raw_input("Guess Col: "))

  #Instructions for all the possibile outcomes of the users guess
  #Actions that end the game are accompanied with a break statement, otherwise the for loop runs again to prompt the user with another turn
  if (user_x == ship_x) and (user_y == ship_y):
    print "You sunk the battleship! You win!!"
    break
  else:
    if (user_x < 0 or user_x > 4) or (user_y < 0 or user_y > 4):
      print "Invalid guess, outside of game bounds."
    elif(board[user_x][user_y] == "1"):
      print "Location already guessed."
    else:
      print "Miss."
      if (user_x < 0 or user_x > 4) or (user_y < 0 or user_y > 4):
        board[user_x][user_y] = "1"
    if turn == 4:
      print "Game Over :("
  
  print_map(board)
