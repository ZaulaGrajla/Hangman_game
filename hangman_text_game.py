from chances import ChancesError
from hangman import Hangman


class HangmanGame:
    def __init__(self):
        self.hangman = Hangman()

    def play(self):
        while True:
            print(f'Pozostała liczba szans: {self.hangman.get_chances()}')
            print(self.hangman.get_word_to_guess())
            letter = input('Podaj literę lub słowo: ')
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
        print('\nSłabiaku!!!!')
        self.print_word_to_find()

    def win(self):
        print('\nGratulacje!!!')
        self.print_word_to_find()

    def print_word_to_find(self):
        print(f'Szukane słowo to: {self.hangman.get_word_to_find()}')


# poczytaj o __main

def main_game():
    game = HangmanGame()
    while True:
        game = HangmanGame()
        game.play()

        answer = input('Chcesz zagrać ponownie? [t/n]: ')
        if answer == 'n':
            break


if __name__ == '__main__':
    main_game()
