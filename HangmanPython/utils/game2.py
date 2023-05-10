import random
from typing import List, Union

        # This line defines the __init__ method. The first argument, self, refers to the object being created.
class Hangman:
    def __init__(self):
        # These strings represent the words that can be chosen as the word to find in the game.
        self.possible_words:List[str]= ['becode', 'learning', 'mathematics', 'sessions'] 
        # converted into a list of characters using the list function. 
        self.word_to_find = list(random.choice(self.possible_words))
        self.lives = 5
        self.correctly_guessed_letters = ['_'] * len(self.word_to_find)
        self.wrongly_guessed_letters:List[str]= []
        self.turn_count = 0
        self.error_count = 0


    def start_game(self):
        while True:
            self.play()
            print(f"{' '.join(self.correctly_guessed_letters)}")
            print(f"Wrong guesses: {', '.join(self.wrongly_guessed_letters)}")
            print(f"Lives: {self.lives}")
            print(f"Turns: {self.turn_count}")
            print(f"Errors: {self.error_count}")
            if '_' not in self.correctly_guessed_letters:
                self.well_played()
                break
            if self.lives == 0:
                self.game_over()
                break


    def play(self):
        letter = input("Enter a letter: ").lower()
        if len(letter) != 1 or not letter.isalpha():
            print("Please enter a single letter.")
            return
        self.turn_count += 1
        if letter in self.word_to_find:
            for i, char in enumerate(self.word_to_find):
                if char == letter:
                    self.correctly_guessed_letters[i] = letter
        else:
            self.wrongly_guessed_letters.append(letter)
            self.error_count += 1
            self.lives -= 1
            
    def game_over(self):
        print("Game over...")

    def well_played(self):
        print(f"You found the word: {''.join(self.word_to_find)} in {self.turn_count} turns with {self.error_count} errors!")
        


# game = Hangman()
# game.start_game()
 