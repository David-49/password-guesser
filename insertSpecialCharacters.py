from itertools import product, combinations

class InsertSpecialCharacters:
    special_chars = ['.', '$', '?', '!', '*']
    _words = []

    def __init__(self, words):
        self._words = words

    def insert_special_chars(self):
        combined_words = []

        for word_pair in product(self._words, repeat=2):
            for special_char in InsertSpecialCharacters.special_chars:
                combined_word = f"{word_pair[0]}{special_char}{word_pair[1]}"
                combined_words.append(combined_word)
    
        return combined_words
        