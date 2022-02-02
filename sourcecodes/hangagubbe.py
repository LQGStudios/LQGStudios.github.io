import random
import os
import time
tried = list()
tried.append('Försökt: ')
with open("ord.txt", "r") as file:
    data = file.read()
    words = data.split()
      
    # Generating a random number for word position
    word_pos = random.randint(0, len(words)-1)
    print(words[word_pos])

correct = list(words[word_pos])
guesslist = list()
for letter in correct:
  guesslist.append(' _')
dead = int(0)

def guessing():
  global dead  
  os.system('cls' if os.name == 'nt' else 'clear')
  def deadness():
    if dead == 9:
      os.system('cls' if os.name == 'nt' else 'clear')
      print('_____ \n|   |\n|   0\n|  /|\ \n|  / \ \n|_______')
      print('Du förlorade!')
      print('Rätt ord var %s' % (words[word_pos]))
      exit()
    elif dead == 8:
      print('_____ \n|   |\n|   0\n|  /|\ \n|  /  \n|_______')
    elif dead == 7:
      print('_____ \n|   |\n|   0\n|  /|\ \n|    \n|_______')
    elif dead == 6:
      print('_____ \n|   |\n|   0\n|  /| \n|    \n|_______')
    elif dead == 5:
      print('_____ \n|   |\n|   0\n|  | \n|    \n|_______')
    elif dead == 4:
      print('_____ \n|   |\n|   0\n|   \n|    \n|_______')
    elif dead == 3:
      print('_____ \n|   |\n|   \n|   \n|    \n|_______')
    elif dead == 2:
      print('_____ \n|   \n|   \n|   \n|    \n|_______')
    elif dead == 1:
      print(' \n|   \n|   \n|   \n|    \n|_______')
    elif dead == 0:
      print('\n \n \n \n \n________')
  deadness()
  print(" ".join(guesslist))
  print(" ".join(tried))
  guess = input('Gissa en bokstav: ')
  if guess in guesslist or guess in tried:
    print ("Du har redan gissat bokstaven %s, försök igen!" % (guess))
    time.sleep(1) 
    guessing()
  elif guess not in correct:
    tried.append(guess + ', ')
    print('Fel!')
    dead += 1
    time.sleep(1)
  elif guess in correct:
    #replace = int(correct.index(guess))
    #replace -= 1

    isitin = 0
    for _ in range(len(correct)):
      replace = correct[isitin]
      if replace == guess:
        guesslist[isitin] = guess
      isitin += 1



    #guesslist[replace] = guess
    
 
  
  #else:
    #tried.append(guess + ', ')
    #print('Fel: %s ' % (tried))
    #dead += 1

  
  
  
  
  l = [y.replace(' ', '') for y in guesslist]
  if l == correct:
    os.system('cls' if os.name == 'nt' else 'clear')
    deadness()
    print(" ".join(guesslist))
    print('You win!')
    exit()
  else:
    guessing()

  

guessing()

