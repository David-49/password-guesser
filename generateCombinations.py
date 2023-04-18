from itertools import permutations

class GenerateCombinations:
    _words = []

    def __init__(self, words):
        self._words = words

    def generate_combinations(self):
        all_permutations = permutations(self._words, 2)
        combined_words = [''.join(p) for p in all_permutations]
        return combined_words