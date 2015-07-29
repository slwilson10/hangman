# 
# Hangman
#

import random
import string

WORDLIST_FILENAME = "words.txt"
wordlist = []

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print ("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    for w in inFile:
        word = (w.rstrip())
        wordlist.append(word)
    print ("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    return random.choice(wordlist)

def hide_word(randword, board, guesses):
  for letter in randword:
    if letter not in guesses:
      board.append('_')
    else:
      board.append(letter)
  board = ' '.join(board)
  print (board)
  return 
  
def swap_letters(randword, guesses, board):
  for letter in randword:
    if letter in guesses:
      board.replace(letter)
  return 
 
def get_guess(guesses):
  guess = str(input('Which letter do you guess? --> '))
  if len(guess) != 1:
    print ('You entered more than one character. Try agian.')
    get_guess(guesses)
  elif guess in guesses:
    print ('You already guessed that letter. Try agian.')
    get_guess(guesses)
  else:  
    guesses.append(guess)
    guesses = ' '.join(guesses)
    print ('Your guesses are: %s ' % (guesses))
    return guess

def check_for_win(randword, guesses):
  right = 0
  for i in randword:
    if i in guesses:
      right += 1
  if right == len(randword):
    return True
  else:
    return False
      
  
def main():
  max_tries = 10
  wordlist = load_words()
  randword = choose_word(wordlist)
  guesses = []
  win = False

  while True:
    print ('You have %d turns left.' % (max_tries))
    board = []
    hide_word(randword, board, guesses)
    guess = str(get_guess(guesses))
    if guess not in randword:
      max_tries = max_tries - 1
    else: 
      pass
    win = check_for_win(randword, guesses)
    if win == True:
      print ('You win!')
      break
    if  max_tries == 0:
      print ('You lost')
      break 
  print ('The word was: ' + randword)
  print ('Game Over!')

if __name__ == '__main__':
  main()
