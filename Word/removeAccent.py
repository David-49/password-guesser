from unidecode import unidecode

class RemoveAccent:

    def remove(self, word):
        if unidecode(word)!= word:
            return unidecode(word)