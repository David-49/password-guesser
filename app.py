from unidecode import unidecode


class App:
    words = []
    dates = []
    special_characters = False
    leet = False

    leet_dictionnaries = {
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

    def __init__(self, words):
        for word in words.split(','):
            self.words.append(word.strip())
    
    def word_to_uppercase(self):
        uppercase_words = []
        for word in self.words:
            uppercase_words.append(word.upper())
        return uppercase_words

    def word_to_lowercase(self):
        lowercase_words = []
        for word in self.words:
            lowercase_words.append(word.lower())
        return lowercase_words

    # def word_to_lowercase_without_accent(self):
    #     lowercase_words = []
    #     lowercase_words_without_accent = self.remove_accent_to_words(self.words)
        
    #     for word in self.words:
    #         lowercase_words.append(word.lower())
    #     return lowercase_words

    def first_letter_to_uppercase(self):
        first_letter_uppercase = []
        for word in self.words:
            first_letter_uppercase.append(word[0].upper() + word[1:])
        return first_letter_uppercase

    def remove_accent_to_words(self):
        words_without_accent = []
        for word in self.words:
            words_without_accent.append(unidecode(word))
        return words_without_accent

    def convert_words_to_leet(self, words):
        words_in_leet = []
        for word in words:
            characters_in_leet = []
            for char in word:
                print(self.leet_dictionnaries[char])
                characters_in_leet.append(self.leet_dictionnaries[char.lower()])
            words_in_leet.append("".join(characters_in_leet))
        return words_in_leet

    




    def combine_words(self):
        words_combination = self.word_to_uppercase() + self.word_to_lowercase() + self.first_letter_to_uppercase() + self.remove_accent_to_words()
        all_passwords = words_combination
        ##all_passwords_leet = self.convert_words_to_leet(self, words_combination)
        print(all_passwords)
        ##print(all_passwords_leet)

