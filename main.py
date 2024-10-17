# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


import io
from pprint import pprint

class WordsFinder:
    def __init__(self, *args):
        self.file_names = args

    def get_all_words(self):
        all_words = {}

        for name in self.file_names:
            word = self._read_words(name)
            all_words[name] = word
        return all_words

    def _read_words(self, file_name):
        with open(file_name, 'r', encoding='utf-8') as file:
            text = file.read().lower()

            symbols_to_remove = ',!?.:-'

            for symbol in symbols_to_remove:
                text = text.replace(symbol, " ")
                words = text.split()
            return words

    def find(self, word):
        word_acc = {}

        for file_name, words in self.get_all_words().items():
            if word.lower() in words:
                position = words.index(word.lower()) + 1  # Позиция с 1
                word_acc[file_name] = position

        return word_acc

    def count(self, word):
        result = {}
        for name, words in self.get_all_words().items():
            count = words.count(word.lower())
            if count > 0:
                result[name] = count

        return result

finder1 = WordsFinder('test1_file.txt')
print(finder1.get_all_words())
print(finder1.find('Child'))
print(finder1.count('Child'))


finder2 = WordsFinder('test2_file.txt')  # , 'test1_file.txt', 'test3_file.txt'
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

finder3 = WordsFinder('test3_file.txt')
print(finder3.get_all_words())
print(finder3.find('captain'))
print(finder3.count('captain'))