import random
import string
import os
import time

def grid_maker(h, v):
  return '\n'.join(' '.join(row) for row in  [[str(random.randint(1, 100)) for _ in range(v)] for _ in range(h)])

def final_grid_maker(h,v):
 for y in range(1, 5):
  x = ('00 ')
  grid = [[str(x) for _ in range(v)] for _ in range (h)]
  return grid

def encryptionstart():
  placeinword = int(0)
  placeinkey = int(0)
  ogText = input('Input the text you want to encrypt: ')
  key = ''
  amountofnums = len(ogText)
  print(amountofnums)
  
  for _ in range(7):
    randnum = str(random.randrange(0,9))
    key = key + randnum
  print(key)
  
  new_string = ''

  for _ in range(amountofnums):
    letter = ogText[placeinword]
    if placeinkey == 6:
      placeinkey = int(0)
    elif letter == ' ':
      new_string = new_string + ' '
      placeinword += 1
    elif letter == "'":
      new_string == new_string + "'"
      placeinword += 1
    elif letter == '.':
      new_string = new_string + '.'
      placeinword += 1
    elif letter == '!':
      new_string = new_string + '.'
      placeinword += 1
    else:
      replaceletternum = string.ascii_letters.index(letter)
      numba = int(key[placeinkey])
      replaceletternum += numba
      replaceletter = string.ascii_letters[replaceletternum]
      new_string = new_string + replaceletter
      placeinword += 1
      placeinkey += 1

  for _ in range(15):
    print(grid_maker(10, 10))
    time.sleep(0.125)
    os.system('cls' if os.name == 'nt' else 'clear')
  print ('\n'.join(''.join(row) for row in final_grid_maker(10,10)))
  time.sleep(0.5)
  os.system('cls' if os.name == 'nt' else 'clear')
  print(new_string)
  print('Your decryption key is: %s' % (key))


def decryption():
  placeinword = int(0)
  ogText = input('Input the text you want to decrypt: ')
  key = input('\nEnter your decryption key: ')
  amountofnums = len(ogText)

  new_string = ''

  for _ in range(amountofnums):
    letter = ogText[placeinword]

    if letter == ' ':
      print(' ')
      new_string = new_string + ' '
      placeinword += 1
    else:
      replaceletternum = string.ascii_letters.index(letter)
      numba = int(key[placeinword])
      replaceletternum -= numba
      replaceletter = string.ascii_letters[replaceletternum]
      new_string = new_string + replaceletter
      placeinword += 1

  for _ in range(15):
    print(grid_maker(10, 10))
    time.sleep(0.125)
    os.system('cls' if os.name == 'nt' else 'clear')
  print ('\n'.join(''.join(row) for row in final_grid_maker(10,10)))
  time.sleep(0.5)
  os.system('cls' if os.name == 'nt' else 'clear')
  print(new_string)

def startup():

  print('Welcome to Spy Message Tool Deluxe v1.9')

  DeOrEn = input('Do want to decrypt or encrypt text? (d/e): ')

  if DeOrEn == 'e' or DeOrEn == 'E':
    os.system('cls' if os.name == 'nt' else 'clear')
    encryptionstart()
  elif DeOrEn == 'd' or DeOrEn == 'D':
    os.system('cls' if os.name == 'nt' else 'clear')
    decryption()
  else:
    print('That does not exist!')
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    startup()

startup()