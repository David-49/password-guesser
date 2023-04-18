from Dates.dateConfiguration import Date
from Leet.leetConverter import LeetConverter
from generateCombinations import GenerateCombinations
from insertSpecialCharacters import InsertSpecialCharacters
from word import Word

class Password:
   possible_combinations = []
   _words: list = []
   _date: str = ""
   special_characters: bool = False
   _leet: bool = False
   _date_lang: str = "FR"

   def __init__(self, dataForm, options):
      self._words = dataForm['words']
      self._date = dataForm['date']
      self.special_characters = options['specialCharacters']
      self._leet = options['leet']
      self._date_lang = options['dateLang']

   def concat_combinations(self):
      self.possible_combinations += self._words

      date_object = Date(self._date, self._date_lang)
      self.possible_combinations += date_object.convert_date_to_human_language()
      self.possible_combinations += date_object.get_year_parts()

      word_object = Word(self._words)
      self.possible_combinations += word_object.concat_methods_results()
          
      if self._leet:
         leet_converter_object = LeetConverter(self.possible_combinations)
         self.possible_combinations += leet_converter_object.convert_words_to_leet()

      if self.special_characters:
         insert_special_chars_object = InsertSpecialCharacters(self.possible_combinations)
         self.possible_combinations += insert_special_chars_object.insert_special_chars()

      generat_combinations_object = GenerateCombinations(self.possible_combinations)
      self.possible_combinations += generat_combinations_object.generate_combinations()

      return list(dict.fromkeys(self.possible_combinations))
