from random import randint
import os

class Words:

    def __init__(self, name_of_file='words_from_file/words.txt'):
        self.file = self.get_path()

    def get_path(self):
        print(os.path.dirname(__file__))
        print(os.path.abspath(os.path.dirname(__file__)))
        return os.path.abspath(os.path.dirname(__file__))

    def get_word(self):
        lines = 0
        with open(f'{self.get_path()}/words.txt', 'r') as plik:
            while plik.readline():
                lines += 1
        word = None
        random_line = randint(1, lines)
        lines = 0
        with open(f'{self.get_path()}/words.txt') as file:
            for i in range(random_line):
                word = file.readline().strip()
            print(word, len(word))
        return word


def get_word_from_file():
    lines = 0
    directory = os.path.abspath(os.path.dirname(__file__))
    with open(f'{directory}/words.txt') as file:
        while file.readline():
            lines += 1
        print(lines)
        file.seek(0)
        random_line = randint(1, lines)
        print(random_line)
        our_word = None
        line_read = 0
        while line_read < random_line:
            line_read += 1
            our_word = file.readline().strip()
        print(our_word)
        
if __name__ == '__main__':
    word = Words()
    print(word.get_word())
