from random import randint

#create an empty list
board = []
#loop 5 times to create a 5x5 O board
for i in range(5):
  board.append(["O"] * 5)

def print_board(board_in):
  for row in board_in:
    #omits the ' ' and , in each 'O',
    print " ".join(row)
    
print_board(board)

#generates random row,col between 0-4
def random_row(board_in):
  return randint(0, len(board_in) - 1)
def random_col(board_in):
  return randint(0, len(board_in) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

#debug lines for ship location
print ship_row
print ship_col

for turn in range(4):
  print "Turn", turn + 1
  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Col: "))
  if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sunk my battleship!"
    break
  elif guess_row not in range(5) and guess_col not in range(5):
    print "Oops, that's not even in the ocean."
  elif board[guess_row][guess_col] == "X":
    print "You guessed that one already."
  else:
    board[guess_row][guess_col] = "X"
    if turn == 3:
      print "Game Over"
    else:
      print "You missed my battleship!"
print_board(board)
