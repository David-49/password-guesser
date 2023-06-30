from .wordTransform import WordTransform

class WordLowercase(WordTransform):

    def _transform(self, word, withoutAccent=None):
        if withoutAccent is None:
            return word.lower()
        return withoutAccent.lower()