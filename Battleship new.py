from random import randint

board = []

for a in range(5):
  board.append(["O"] * 5)

def rand_row(board):
  return randint(0, len(board) - 1)

def rand_col(board):
  return randint(0, len(board[0]) - 1)

def print_map(board):
  for line in board:
    print " ".join(line)

print_map(board)

ship_x = rand_row(board)
ship_y = rand_col(board)

for turn in range(4):
  print "Turn", turn + 1
    
  user_x = int(raw_input("Guess Row: "))
  user_y = int(raw_input("Guess Col: "))

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
    if turn == 3:
      print "Game Over :("
  
  print_map(board)
