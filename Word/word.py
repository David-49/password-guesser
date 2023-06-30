from .wordCapitalize import WordCapitalize
from .wordLowercase import WordLowercase
from .wordUppercase import WordUppercase
from .removeAccent import RemoveAccent
from .wordInterface import WordInterface

class Word(WordInterface):
    _words = []
    _uppercase = []
    _lowercase = []
    _remove_accent = []
    _capitalize = []

    def __init__(self, words):
        self._words += words
        self._uppercase = WordUppercase()
        self._lowercase = WordLowercase()
        self._remove_accent = RemoveAccent()
        self._capitalize = WordCapitalize()
        
    def to_capitalize_without_accent(self, word):
        withoutAccent = self._remove_accent.remove(word)
        if withoutAccent is not None:
            return self._capitalize.to_capitalize(withoutAccent)
        return None

    def to_lowercase_without_accent(self, word):
        withoutAccent = self._remove_accent.remove(word)
        if withoutAccent is not None:
            return withoutAccent.capitalize()
        return None
    
    def to_uppercase_without_accent(self, word):
        withoutAccent = self._remove_accent.remove(word)
        if withoutAccent is not None:
            return self._uppercase._transform(withoutAccent)
        return None
    
    def remove_accent_from_words(self):
        wordsWithoutAccent = []
        for word in self._words:
            wordsWithoutAccent.append(self._remove_accent.remove(word))
        return wordsWithoutAccent

    def words_to_uppercase(self):
        uppercaseWords = []
        for word in self._words:
            uppercaseWords.append(self._uppercase._transform(word))
        return uppercaseWords
    
    def words_to_lowercase(self):
        lowercaseWords = []
        for word in self._words:
            lowercaseWords.append(self._lowercase._transform(word))
        return lowercaseWords

    def capitalize_words(self):
        capitalizeWords = []
        for word in self._words:
            capitalizeWords.append(self._capitalize.to_capitalize(word))
        return capitalizeWords
    
    def capitalize_words_without_accents(self):
        capitalizeWordsWithoutAccents = []
        for word in self._words:
            capitalizeWordsWithoutAccents.append(self.to_capitalize_without_accent(word))
        return capitalizeWordsWithoutAccents
    
    def uppercase_words_without_accents(self):
        uppercaseWordsWithoutAccents = []
        for word in self._words:
            uppercaseWordsWithoutAccents.append(self.to_uppercase_without_accent(word))
        return uppercaseWordsWithoutAccents
    
    def lowercase_words_without_accents(self):
        lowercaseWordsWithoutAccents = []
        for word in self._words:
            lowercaseWordsWithoutAccents.append(self.to_lowercase_without_accent(word))
        return lowercaseWordsWithoutAccents
    
    def concat_methods_results(self):
        possible_combinations = []

        possible_combinations += self.remove_accent_from_words()
        possible_combinations += self.words_to_uppercase()
        possible_combinations += self.words_to_lowercase()
        possible_combinations += self.capitalize_words()
        possible_combinations += self.capitalize_words_without_accents()
        possible_combinations += self.uppercase_words_without_accents()
        possible_combinations += self.lowercase_words_without_accents()

        possible_combinations = list(filter(lambda item: item is not None, possible_combinations))

        return list(dict.fromkeys(possible_combinations))
