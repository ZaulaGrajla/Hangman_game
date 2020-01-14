from chances import ChancesError
from hangman import Hangman


class HangmanGame:
    def __init__(self):
        self.hangman = Hangman()

    def play(self):
        while True:
            print(f'Chances left: {self.hangman.get_chances()}')
            print(self.hangman.get_word_to_guess())
            letter = input('Give a letter or word: ')
            if self.hangman.is_it_word_to_find(letter):
                self.win()
                break
            try:
                self.hangman.guess_letter(letter)
            except ChancesError:
                self.lose()
                break
            if self.hangman.are_all_letters_found():
                self.win()
                break

    def lose(self):
        print('\nLoser!!!!')
        self.print_word_to_find()

    def win(self):
        print('\nCongrats!!!')
        self.print_word_to_find()

    def print_word_to_find(self):
        print(f'A word to find: {self.hangman.get_word_to_find()}')


def main_game():
    game = HangmanGame()
    while True:
        game = HangmanGame()
        game.play()

        answer = input('Do you want to play again [y/n]: ')
        if answer == 'n':
            break


if __name__ == '__main__':
    main_game()
