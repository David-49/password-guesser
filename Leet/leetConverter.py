class LeetConverter:
    __leet_dict = {
        'a': '4', 'A': '4',
        'b': '8', 'B': '8',
        'e': '3', 'E': '3',
        'g': '6', 'G': '6',
        'i': '1', 'I': '1',
        'l': '1', 'L': '1',
        'o': '0', 'O': '0',
        's': '5', 'S': '5',
        't': '7', 'T': '7',
        'z': '2', 'Z': '2'
    }
    _words = []

    def __init__(self, words):
        self._words = words

    def __convert_to_leet(self, word):
        return ''.join(self.__leet_dict.get(c, c) for c in word)
    
    def convert_words_to_leet(self):
        convertedWords = []
        for word in self._words:
            convertedWords.append(self.__convert_to_leet(word))
        return convertedWords