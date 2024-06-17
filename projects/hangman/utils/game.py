import random
import os

class Hangman():
    """
    Class containing the whole hangman game. The start_game() method is called to initialize a game.
    """
    
    def __init__(self) -> None:
        self.possible_words = ['becode', 'learning', 'mathematics', 'sessions']
        self.word_to_find = [x for x in self.possible_words[random.randrange(len(self.possible_words))]]
        self.lives = 5
        self.wrongly_guessed_letters = []
        self.correctly_guessed_letters = ["_" for x in self.word_to_find]
        self.turn_count = 0
        self.error_count = 0
    pass

    def play(self) -> None:
        """
        Initialize a standard game turn.
        """

        suggested_letters = self.correctly_guessed_letters + self.wrongly_guessed_letters
        guess = input("Take your guess : ")
        while len(guess) != 1 or guess.isalpha() == False:
            guess = input("Wrong format, please only select one letter : ")
        while guess in self.wrongly_guessed_letters + self.correctly_guessed_letters:
            guess = input("Letter already selected, please choose another : ")
        if guess in self.word_to_find:
            suggested_letters.append(guess)
            self.correctly_guessed_letters = [x if x in suggested_letters else "_" for x in self.word_to_find]
        else:
            self.wrongly_guessed_letters.append(guess)
            self.error_count += 1
            self.lives -= 1
    pass

    def game_over(self) -> None:
        """
        Prints the end of game message if defeated.
        """
        print("Game over...")
    pass

    def well_played(self) -> None:
        """
        Prints the end of game message if victorious.
        """
        print(f"You found the word: '{''.join(self.word_to_find)}' in {self.turn_count} turns with {self.error_count} errors!")
    pass

    def start_game(self) -> None:
        """
        Main loop of the game
        """
        os.system('cls||clear')
        print(f"{" ".join(self.correctly_guessed_letters)}")
        while True:
            if self.lives == 0:
                self.game_over()
                break
            elif '_' not in self.correctly_guessed_letters:
                self.well_played()
                break
            else:
                self.play()
            self.turn_count += 1
            os.system('cls||clear')
            print(f"{" ".join(self.correctly_guessed_letters)}\nBad letters : {" ".join(self.wrongly_guessed_letters)}\nLives : {self.lives} | Errors : {self.error_count} | Turn : {self.turn_count}")
    pass