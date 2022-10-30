from unidecode import unidecode
from password import Password

class Word(Password):
    _passwords = []

    _leet_dictionnaries = {
        "a": "4",
        "e": "3",
        "b": "8",
        "z": "2",
        "t": "7",
        "o": "0",
        "g": "6",
        "l": "1",
        "i": "1",
        "s": "5"
    }

    def remove_accent(self):
        if unidecode(self._word)!= self._word:
            return unidecode(self._word)
        return None
    
    def to_uppercase(self, withoutAccent=None):
        if withoutAccent is None:
            return self._word.upper()
        return withoutAccent.upper()

    def to_lowercase(self, withoutAccent=None):
        if withoutAccent is None:
            return self._word.lower()
        return withoutAccent.lower()

    def to_capitalize(self, withoutAccent=None):
        if withoutAccent is None:
            return self._word.capitalize()
        return withoutAccent.capitalize()

    #concats
    
    def to_capitalize_without_accent(self):
        withoutAccent = self.remove_accent()
        if withoutAccent is not None:
            return withoutAccent.capitalize()
        return None

    def to_lowercase_without_accent(self):
        withoutAccent = self.remove_accent()
        if withoutAccent is not None:
            return self.to_lowercase(withoutAccent)
        return None
    
    def to_uppercase_without_accent(self):
        withoutAccent = self.remove_accent()
        if withoutAccent is not None:
            return self.to_uppercase(withoutAccent)
        return None

    # def convert_words_to_leet(self, words):
    #     words_in_leet = []
    #     for word in words:
    #         characters_in_leet = []
    #         for char in word:
    #             print(self.leet_dictionnaries[char])
    #             characters_in_leet.append(self.leet_dictionnaries[char.lower()])
    #         words_in_leet.append("".join(characters_in_leet))
    #     return words_in_leet

    def concat_passwords(self):
        self._passwords.append(self.remove_accent())
        self._passwords.append(self.to_uppercase())
        self._passwords.append(self.to_lowercase())
        self._passwords.append(self.to_capitalize())
        self._passwords.append(self.to_capitalize_without_accent())
        self._passwords.append(self.to_uppercase_without_accent())
        self._passwords.append(self.to_lowercase_without_accent())
        print(self._passwords)