from .wordTransform import WordTransform

class WordUppercase(WordTransform):

    def _transform(self, word, withoutAccent=None):
        if withoutAccent is None:
            return word.upper()
        return withoutAccent.upper()