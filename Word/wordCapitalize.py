class WordCapitalize:

    def to_capitalize(self, word, withoutAccent=None):
        if withoutAccent is None:
            return word.capitalize()
        return withoutAccent.capitalize()