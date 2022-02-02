import random
import time
import os

from inputimeout import inputimeout, TimeoutOccurred

def script():

  def Scromble():
    shuffled = list(word)
    random.shuffle(shuffled)
    shuffled = ''.join(shuffled)
    if shuffled == word:
      Scromble()
    else:
      print(shuffled)
      wordCount = shuffled.count(' ')
      print('There are %s spaces' % (wordCount))

  p1S = int(0)
  p2S = int(0)

  rounds = int(input('How many rounds do you want to play?: '))

  timelimit = int(input('Time limit for answering: '))

  P1 = input('Player 1 name: ')

  time.sleep(0.0625)

  P2 = input('Player 2 name: ')

  print('Lets play SCROMBLE!')
  time.sleep(0.0625)
  print('(⌐■_■)')
  time.sleep(0.125)
  print('YYYYYYYEEEEEAAAAAAAAAAHHHHHHHHHHHH')
  time.sleep(0.5)

  for _ in range(rounds):

    time.sleep(0.5)

    os.system('cls' if os.name == 'nt' else 'clear')

    word = input('Write the word you want to scramble: ').title()

    os.system('cls' if os.name == 'nt' else 'clear')

    Scromble()
    print('(Rembember to capitalize the first letter of every word!)')
    timer = int(timelimit)

    #TIMEOUT = 0,5
    while True:
      y = None
      try:
        y = inputimeout(prompt = "Guess the word: ", timeout=timer)
      except TimeoutOccurred:
        y = None

      if y == None:
        print("Out of time!")
        p1S+=1
        break
      elif y != word:
        print('Wrong!')
        print('Correct word was: %s' % (word))
        p1S+=1
        break
      elif y == word:
        print("Correct")
        p2S+=1
        break



    time.sleep(1)

    time.sleep(0.1)

  if p2S >= p1S:
   print('        P2\n  P1    /|\ \n  /|\  _/ \_\n _/ \_|  1  |___\n|  2          3 |') 
   print("%s wins!" % (P2))
   print("%s - %s" % (p2S, p1S))
  elif p2S == p1S:
    print("It's a tie! Nobody wins!")
  else:
    print('       P1\n  P2    /|\ \n  /|\  _/ \_\n _/ \_|  1  |___\n|  2          3 |') 
    print("%s wins!" % (P1))
    print("%s - %s" % (p1S, p2S))

  restart = input("Would you like play again? Y/N: ")
  if restart == "Y" or restart == "y":
    os.system('cls' if os.name == 'nt' else 'clear')
    script()
  if restart == "n" or restart == "N":
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Have a nice day! :)')


def h2p():
  os.system('cls' if os.name == 'nt' else 'clear')
  print(' __________________________________')
  print('| 1. Player 1 chooses a word       |\n| 2. The word gets scrambled       |\n| 3. Player 2 guesses the word     |')
  print('|                                  |\n| Yes, it is really that simple!   |')
  time.sleep(0.00000001)
  input('|__________________________________|\n\n   Press enter to return to menu: ')
  os.system('cls' if os.name == 'nt' else 'clear')
  menu()

def menu():
  os.system('cls' if os.name == 'nt' else 'clear')
  print('  ██████  ▄████▄   ██▀███   ▒█████   ███▄ ▄███▓ ▄▄▄▄    ██▓    ▓█████ ')
  print('▒██    ▒ ▒██▀ ▀█  ▓██ ▒ ██▒▒██▒  ██▒▓██▒▀█▀ ██▒▓█████▄ ▓██▒    ▓█   ▀ ')
  print('░ ▓██▄   ▒▓█    ▄ ▓██ ░▄█ ▒▒██░  ██▒▓██    ▓██░▒██▒ ▄██▒██░    ▒███   ')
  print('  ▒   ██▒▒▓▓▄ ▄██▒▒██▀▀█▄  ▒██   ██░▒██    ▒██ ▒██░█▀  ▒██░    ▒▓█  ▄ ')
  print('▒██████▒▒▒ ▓███▀ ░░██▓ ▒██▒░ ████▓▒░▒██▒   ░██▒░▓█  ▀█▓░██████▒░▒████▒')
  print('▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒░   ░  ░░▒▓███▀▒░ ▒░▓  ░░░ ▒░ ░')
  print('░ ░▒  ░ ░  ░  ▒     ░▒ ░ ▒░  ░ ▒ ▒░ ░  ░      ░▒░▒   ░ ░ ░ ▒  ░ ░ ░  ░')
  print('░  ░  ░  ░          ░░   ░ ░ ░ ░ ▒  ░      ░    ░    ░   ░ ░      ░   ')
  print('      ░  ░ ░         ░         ░ ░         ░    ░          ░  ░   ░  ░')
  print('         ░                                           ░                ')
  
  print('\n             ______________________________')
  print('            |      Welcome to Scromble     |')
  print('            |                              |\n            |                              |\n            |     1 - START                |\n            |     2 - HOW TO PLAY          |')
  print('            |     3 - QUIT                 |\n            |                              |\n            |______________________________|')
  menuchoice = input('                 Choose an option: ')
  print(menuchoice)

  if menuchoice == '1':
    os.system('cls' if os.name == 'nt' else 'clear')
    script()
  elif menuchoice == '2':
    h2p()
  elif menuchoice == '3':
    exit()
  else:
    print('Oops! That doesnt exist! :)')
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    menu()

time.sleep(1)

print('██╗      ██████╗  ██████╗     ███████╗████████╗██╗   ██╗██████╗ ██╗ ██████╗ ███████╗')
time.sleep(0.0625)
print('██║     ██╔═══██╗██╔════╝     ██╔════╝╚══██╔══╝██║   ██║██╔══██╗██║██╔═══██╗██╔════╝')
time.sleep(0.0625)
print('██║     ██║   ██║██║  ███╗    ███████╗   ██║   ██║   ██║██║  ██║██║██║   ██║███████╗')
time.sleep(0.0625)
print('██║     ██║▄▄ ██║██║   ██║    ╚════██║   ██║   ██║   ██║██║  ██║██║██║   ██║╚════██║')
time.sleep(0.0625)
print('███████╗╚██████╔╝╚██████╔╝    ███████║   ██║   ╚██████╔╝██████╔╝██║╚██████╔╝███████║')
time.sleep(0.0625)
print('╚══════╝ ╚══▀▀═╝  ╚═════╝     ╚══════╝   ╚═╝    ╚═════╝ ╚═════╝ ╚═╝ ╚═════╝ ╚══════╝')

time.sleep(0.5)

print('██████╗ ██████╗ ███████╗███████╗███████╗███╗   ██╗████████╗')
time.sleep(0.0625)
print('██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝████╗  ██║╚══██╔══╝')
time.sleep(0.0625)
print('██████╔╝██████╔╝█████╗  ███████╗█████╗  ██╔██╗ ██║   ██║')
time.sleep(0.0625)
print('██╔═══╝ ██╔══██╗██╔══╝  ╚════██║██╔══╝  ██║╚██╗██║   ██║')
time.sleep(0.0625)
print('██║     ██║  ██║███████╗███████║███████╗██║ ╚████║   ██║')
time.sleep(0.0625)
print('╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═══╝   ╚═╝')

time.sleep(1)

os.system('cls' if os.name == 'nt' else 'clear')

print('  ██████  ▄████▄   ██▀███   ▒█████   ███▄ ▄███▓ ▄▄▄▄    ██▓    ▓█████ ')
time.sleep(0.125)
print('▒██    ▒ ▒██▀ ▀█  ▓██ ▒ ██▒▒██▒  ██▒▓██▒▀█▀ ██▒▓█████▄ ▓██▒    ▓█   ▀ ')
time.sleep(0.125)
print('░ ▓██▄   ▒▓█    ▄ ▓██ ░▄█ ▒▒██░  ██▒▓██    ▓██░▒██▒ ▄██▒██░    ▒███   ')
time.sleep(0.125)
print('  ▒   ██▒▒▓▓▄ ▄██▒▒██▀▀█▄  ▒██   ██░▒██    ▒██ ▒██░█▀  ▒██░    ▒▓█  ▄ ')
time.sleep(0.125)
print('▒██████▒▒▒ ▓███▀ ░░██▓ ▒██▒░ ████▓▒░▒██▒   ░██▒░▓█  ▀█▓░██████▒░▒████▒')
time.sleep(0.125)
print('▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒░   ░  ░░▒▓███▀▒░ ▒░▓  ░░░ ▒░ ░')
time.sleep(0.125)
print('░ ░▒  ░ ░  ░  ▒     ░▒ ░ ▒░  ░ ▒ ▒░ ░  ░      ░▒░▒   ░ ░ ░ ▒  ░ ░ ░  ░')
time.sleep(0.125)
print('░  ░  ░  ░          ░░   ░ ░ ░ ░ ▒  ░      ░    ░    ░   ░ ░      ░   ')
time.sleep(0.125)
print('      ░  ░ ░         ░         ░ ░         ░    ░          ░  ░   ░  ░')
time.sleep(0.125)
print('         ░                                           ░                ')
time.sleep(0.125)
print('Welcome to Scromble')

menu()


