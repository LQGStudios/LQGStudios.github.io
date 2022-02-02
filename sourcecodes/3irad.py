import os
import time
board = []
numba = 1
used = list()
for row in range(3):
    board.append([])
    for column in range(3):
        num = str(numba)
        board[row].append(num)
        numba +=1
     
def print_board(board):
    for row in board:
        print(" ".join(row))
     
p1n = input('Enter name for player 1: ')

p2n = input('Enter name for player 2: ')

p1turn = p1n + "'s"

p2turn = p2n + "'s"

print_board(board)

def animationwin():
  time.sleep(1)
  yes = True

  while yes == True:
      print('\n         O\n   O    /|\ \n  /|\  _/_\_\n _/_\_|  1  |_____\n|  2           3  |') 
      time.sleep(0.5)
      os.system('cls' if os.name == 'nt' else 'clear')
      print('        \O/\n         |  \n   O    / \ \n  /|\  _____\n _/_\_|  1  |_____\n|  2           3  |') 
      time.sleep(0.5)
      os.system('cls' if os.name == 'nt' else 'clear')

def player1turn():

  os.system('cls' if os.name == 'nt' else 'clear')

  print_board(board)

  chs = int(input('%s turn: ' % (p1turn)))

  #bruh = board.index(chs)

  #board[bruh] = 'x'

  if chs in used:
    print('That space is already occupied!\n Try again!')
    time.sleep(5)
    os.system('cls' if os.name == 'nt' else 'clear')
    player1turn()
  elif chs == 0 or chs > 9:
    print('That doesnt exist!')
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    player1turn()
  else:
    used.append(chs)

  if chs == 1:
    board[0][0] = 'x'
  elif chs == 2:
    board[0][1] = 'x'
  elif chs == 3:
    board[0][2] = 'x'
  elif chs == 4:
    board[1][0] = 'x'
  elif chs == 5:
    board[1][1] = 'x'
  elif chs == 6:
    board[1][2] = 'x'
  elif chs == 7:
    board[2][0] = 'x'
  elif chs == 8:
    board[2][1] = 'x'
  elif chs == 9:
    board[2][2] = 'x'

  os.system('cls' if os.name == 'nt' else 'clear')

  print_board(board)

def player2turn():

  os.system('cls' if os.name == 'nt' else 'clear')

  print_board(board)

  chs = int(input('%s turn: ' % (p2turn)))

  #bruh = board.index(chs)

  #board[bruh] = 'x'

  if chs in used:
    print('That space is already occupied!\n Try again!')
    time.sleep(5)
    os.system('cls' if os.name == 'nt' else 'clear')
    player2turn()
  elif chs == 0 or chs >= 9:
    print('That doesnt exist!')
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    player2turn()
  else:
    used.append(chs)

  if chs == 1:
    board[0][0] = 'o'
  elif chs == 2:
    board[0][1] = 'o'
  elif chs == 3:
    board[0][2] = 'o'
  elif chs == 4:
    board[1][0] = 'o'
  elif chs == 5:
    board[1][1] = 'o'
  elif chs == 6:
    board[1][2] = 'o'
  elif chs == 7:
    board[2][0] = 'o'
  elif chs == 8:
    board[2][1] = 'o'
  elif chs == 9:
    board[2][2] = 'o'

  os.system('cls' if os.name == 'nt' else 'clear')

  print_board(board)

def winning():
    if board[0] == ['x', 'x', 'x'] or board[1] == ['x', 'x', 'x'] or board[2] == ['x', 'x', 'x']:
      print('%s wins!' % (p1n))
      animationwin()
    elif board[0][0] == 'x' and board[1][0] == 'x' and board[2][0] == 'x':
      print('%s wins!' % (p1n))
      animationwin()
    elif board[0][1] == 'x' and board[1][1] == 'x' and board[2][1] == 'x':
      print('%s wins!' % (p1n))
      animationwin()
    elif board[0][2] == 'x' and board[1][2] == 'x' and board[2][2] == 'x':
      print('%s wins!' % (p1n))
      animationwin()
    elif board[0][0] == 'x' and board[1][1] == 'x' and board[2][2] == 'x':
      print('%s wins!' % (p1n))
      animationwin()
    elif board[0][2] == 'x' and board[1][1] == 'x' and board[2][0] == 'x':
      print('%s wins!' % (p1n))
      animationwin()

def winning2():
    if board[0] == ['o', 'o', 'o'] or board[1] == ['o', 'o', 'o'] or board[2] == ['o', 'o', 'o']:
        print('%s wins!' % (p2n))
        animationwin()
    elif board[0][0] == 'o' and board[1][0] == 'o' and board[2][0] == 'o':
        print('%s wins!' % (p2n))
        animationwin()
    elif board[0][1] == 'o' and board[1][1] == 'o' and board[2][1] == 'o':
        print('%s wins!' % (p2n))
        animationwin()
    elif board[0][2] == 'o' and board[1][2] == 'o' and board[2][2] == 'o':
        print('%s wins!' % (p2n))
        animationwin()
    elif board[0][0] == 'o' and board[1][1] == 'o' and board[2][2] == 'o':
        print('%s wins!' % (p2n))
        animationwin()
    elif board[0][2] == 'o' and board[1][1] == 'o' and board[2][0] == 'o':
        print('%s wins!' % (p2n))
        animationwin()
    #else:
        #playing()

def playing():
    player1turn()

    winning()

    player2turn()

    winning2()

for _ in range(9):
  playing()
print('Draw')