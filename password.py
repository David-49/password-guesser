from word import Word

class Password:
   _word = ""
   _special_characters = False
   _leet = False

   def __init__(self, word):
      self._word = word 