import random
from words import words
import string

def get_valid_word(words):
    word = " " 
    while "-" in word or " " in word:
        word = random.choice(words) # randomly choose an item from the list
    
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # letters the user has guessed!

    lives = 7 # number of guesses
    index_value = lives

    while len(word_letters) > 0 and lives > 0:
        if(lives-index_value) != 0: # don't require this print statement for first entry
            print("\nYou have already utilized: ", " ".join(used_letters))

        word_list = [character if character in used_letters else "-" for character in word]

        print("\nWord: ", " ".join(word_list))

        lives -= 1        

        captured_letters = input("Guess a letter: ").upper()
        if captured_letters in alphabet - used_letters:
            used_letters.add(captured_letters)
            if captured_letters in word_letters:
                word_letters.remove(captured_letters)

        elif captured_letters in used_letters:
            print("\nLetter has already been utilized!")

        else:
            print("\nInvalid Character!")
    
    return word, lives

output = hangman()
if output[1] == 0:
    print(f"\nSorry you ran out of lives... the world was {output[0]}!\n")

else:
    print(f"\nCongrats you got the word: {output[0]}!\n")