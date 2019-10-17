from random import randint
import os


# wczytać zawartość pliku (może do listy?)
# wylosować słowo z listy albo innej takiej
# zwrócić wylosowane słowo
# co to znaczy parsować

class Words:

    def __init__(self, name_of_file='words_from_file/words.txt'):
        # def __init__(self, name_of_file='words_from_file/words.txt'):
        # def __init__(self, name_of_file='words.txt'):
        self.file = self.get_path()

    def get_path(self):
        print(os.path.dirname(__file__))
        print(os.path.abspath(os.path.dirname(__file__)))
        return os.path.abspath(os.path.dirname(__file__))

    def get_word(self):
        lines = 0
        with open(f'{self.get_path()}/words.txt', 'r') as plik:
            # self.list_of_words = plik.read().split('\n')
            while plik.readline():
                lines += 1

        # random_line = lines  # randint(0,lines-1)
        # print(random_line is lines)
        # print(lines, random_line)
        word = None
        random_line = randint(1, lines)
        lines = 0
        # print(random_line is lines)
        with open(f'{self.get_path()}/words.txt') as file:
            for i in range(random_line):
                # while file.readline() and random_line > lines:
                #     lines += 1
                word = file.readline().strip()  # co to?usuwa ostatni nieprintowalny znak, usuwa białe znaki na początku i na końcu

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
            # print(our_word)
        print(our_word)


# def get_word(self) -> str:
#     index = randint(0, len(self.list_of_words) - 1)
#     return self.list_of_words[index]


# dupa = Words()
# print(dupa.get_word())

if __name__ == '__main__':
    word = Words()
    print(word.get_word())

# get_word_from_file()
