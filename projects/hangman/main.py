from utils.game import Hangman
from utils.file_utils import read_file

game = Hangman(read_file('words.txt'))
game.start_game()