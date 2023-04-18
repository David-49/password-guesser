from unidecode import unidecode

class Word:
    _words = []

    def __init__(self, words):
        self._words += words

    def remove_accent(self, word):
        if unidecode(word)!= word:
            return unidecode(word)
    
    def to_uppercase(self, word, withoutAccent=None):
        if withoutAccent is None:
            return word.upper()
        return withoutAccent.upper()

    def to_lowercase(self, word, withoutAccent=None):
        if withoutAccent is None:
            return word.lower()
        return withoutAccent.lower()

    def to_capitalize(self, word, withoutAccent=None):
        if withoutAccent is None:
            return word.capitalize()
        return withoutAccent.capitalize()

    def to_capitalize_without_accent(self, word):
        withoutAccent = self.remove_accent(word)
        if withoutAccent is not None:
            return withoutAccent.capitalize()
        return None

    def to_lowercase_without_accent(self, word):
        withoutAccent = self.remove_accent(word)
        if withoutAccent is not None:
            return self.to_lowercase(withoutAccent)
        return None
    
    def to_uppercase_without_accent(self, word):
        withoutAccent = self.remove_accent(word)
        if withoutAccent is not None:
            return self.to_uppercase(withoutAccent)
        return None
    
    def remove_accent_from_words(self):
        wordsWithoutAccent = []
        for word in self._words:
            wordsWithoutAccent.append(self.remove_accent(word))
        return wordsWithoutAccent

    def words_to_uppercase(self):
        uppercaseWords = []
        for word in self._words:
            uppercaseWords.append(self.to_uppercase(word))
        return uppercaseWords
    
    def words_to_lowercase(self):
        lowercaseWords = []
        for word in self._words:
            lowercaseWords.append(self.to_lowercase(word))
        return lowercaseWords

    def capitalize_words(self):
        capitalizeWords = []
        for word in self._words:
            capitalizeWords.append(self.to_capitalize(word))
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
        _possible_combinations = []
        _possible_combinations += self.remove_accent_from_words()
        _possible_combinations += self.words_to_uppercase()
        _possible_combinations += self.words_to_lowercase()
        _possible_combinations += self.capitalize_words()
        _possible_combinations += self.capitalize_words_without_accents()
        _possible_combinations += self.uppercase_words_without_accents()
        _possible_combinations += self.lowercase_words_without_accents()

        _possible_combinations = list(filter(lambda item: item is not None, _possible_combinations))

        return list(dict.fromkeys(_possible_combinations))
