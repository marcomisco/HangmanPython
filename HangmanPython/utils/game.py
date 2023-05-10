from typing import List, Union
import random

# create a class with attributes
class Hangman:
    def __init__(self):
        self.possible_words:List[str]= ['becode', 'learning', 'mathematics', 'sessions']
        self.word_to_find = list(random.choice(self.possible_words))
        self.lives = 5
        self.correctly_guessed_letters = ['_'] * len(self.word_to_find)
        self.wrongly_guessed_letters:List[str]= []
        self.turn_count = 0
        self.error_count = 0


    def start_game(self):
        while not self.game_over():
            print(' '.join(self.correctly_guessed_letters))
            print("Lives left:", self.lives)
            print("Wrong guesses:", ' '.join(self.wrongly_guessed_letters))
            self.play()

    def play(self):
        letter = input("Enter a letter: ").lower()
        if len(letter) != 1 or not letter.isalpha():
            print("Please enter a single letter.")
            return
        self.turn_count += 1
        if letter in self.word_to_find:
            for i in range(len(self.word_to_find)):
                if self.word_to_find[i] == letter:
                    self.correctly_guessed_letters[i] = letter
        else:
            self.wrongly_guessed_letters.append(letter)
            self.error_count += 1
            self.lives -= 1

    def game_over(self):
        if self.lives == 0:
            print("Game over! The word was:", ''.join(self.word_to_find))
            return True
        if '_' not in self.correctly_guessed_letters:
            print("Congratulations! You won in", self.turn_count, "turns with", self.error_count, "errors!")
            return True
        return False



if __name__ == '__main__':
    game = Hangman()
    game.start_game()

 