from typing import List

def get_word() -> str:
    return input("Please enter a word to be guessed : ")

def get_lives() -> int:
    return int(input("Please enter a number of lives : "))

def get_guess(suggested_letters : List[str]) -> str:
    guess = input("Take your guess : ")
    while len(guess) != 1 or guess.isalpha() == False:
        guess = input("Wrong format, please only select one letter : ")
    while guess in suggested_letters:
        guess = input("Letter already selected, please choose another : ")
    return guess

def assess_guess(secret_word : str, guessed_letter : str, lives_left : int) -> int:
    if guessed_letter in secret_word:
        print("Correct guess!")
        return lives_left
    else:
        print("Incorrect guess :'(")
        return lives_left - 1

def display_word(secret_word : str, suggested_letters : List[str]) -> bool:
    word_holes = [x if x in suggested_letters else "_" for x in secret_word]
    print(' '.join(word_holes))
    if "_" in word_holes:
        return False
    else:
        return True
    
def main():
    secret_word = get_word()
    lives = get_lives()
    suggested_letters = []
    player_win = False

    display_word(secret_word, suggested_letters)

    while lives > 0 and not player_win:
        print(f'You still have {lives} lives')
        guess = get_guess(suggested_letters)
        suggested_letters.append(guess)
        lives = assess_guess(secret_word, guess, lives)
        player_win = display_word(secret_word, suggested_letters)

if __name__ == '__main__':
    main()