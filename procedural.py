import time
from datetime import datetime
from unidecode import unidecode
from flask import Flask, render_template, request
from itertools import permutations

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['mots']
    email = request.form['dates']
    return f'Hello, {name}! Your email is {email}.'

if __name__ == '__main__':
    app.run(debug=True)

submit()

words = input("Ajouter une liste de mots :\n")

wordsList = []
for word in words.split(','):
            wordsList.append(word.strip())

#dates = input("Dates :\n")

def convert_month_to_french(date_str, lang_selected):
    french_months = [
        'janvier', 'février', 'mars', 'avril', 'mai', 'juin',
        'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre'
    ]

    english_months = [
        'january', 'february', 'march', 'april', 'may', 'june',
        'jully', 'august', 'september', 'october', 'november', 'december'
    ]
    
    date_obj = datetime.strptime(date_str, "%Y/%m/%d")
    day = date_obj.day
    month = french_months[date_obj.month - 1]
    year = date_obj.year

    return f"{day} {month} {year}"

date = "2023/04/12"
french_date = convert_month_to_french(date)
print(french_date)


def get_year_parts(date_str):
    date_obj = datetime.strptime(date_str, "%Y/%m/%d")
    year = date_obj.year
    last_two_digits = year % 100
    return last_two_digits, year

date = "2023/04/12"
result = get_year_parts(date)
print(result)


def generate_combinations(words):
    all_permutations = permutations(words, 2)
    combined_words = [''.join(p) for p in all_permutations]
    return combined_words

words = ['salut', 'oui', 'non']
combined_words = generate_combinations(words)
print(combined_words)


def word_to_leet(word):
    leet_dict = {
        'a': '4', 'A': '4',
        'b': '8', 'B': '8',
        'e': '3', 'E': '3',
        'g': '6', 'G': '6',
        'i': '1', 'I': '1',
        'l': '1', 'L': '1',
        'o': '0', 'O': '0',
        's': '5', 'S': '5',
        't': '7', 'T': '7',
        'z': '2', 'Z': '2'
    }
    return ''.join(leet_dict.get(c, c) for c in word)

def convert_words_to_leet(words):
     return [word_to_leet(word) for word in words]

words = ["Leet", "Converter", "Python", "Example"]
leet_words = convert_words_to_leet(words)
print(leet_words)


def word_to_uppercase(wordsList):
    uppercase_words = []
    for word in wordsList:
        uppercase_words.append(word.upper())
    return uppercase_words

def word_to_lowercase(wordsList):
    lowercase_words = []
    for word in wordsList:
        lowercase_words.append(word.lower())
    return lowercase_words

def remove_accent_to_words(wordsList):
    words_without_accent = []
    for word in wordsList:
        words_without_accent.append(unidecode(word))
    return words_without_accent

def first_letter_to_uppercase(wordsList):
    first_letter_uppercase = []
    for word in wordsList:
        first_letter_uppercase.append(word[0].upper() + word[1:])
    return first_letter_uppercase

def parse_date_in_words(dates):
    for date in dates:
        print(date.split())

def combine_words():
    wordsUppercase = word_to_uppercase(wordsList)
    wordsLowercase = word_to_lowercase(wordsList)
    firstLetterUppercase = first_letter_to_uppercase(wordsList)
    wordsUppercaseWithoutAccent = remove_accent_to_words(wordsUppercase)
    wordsLowercaseWithoutAccent = remove_accent_to_words(wordsLowercase)
    firstLetterUppercaseWithoutAccent = first_letter_to_uppercase(wordsLowercaseWithoutAccent)

    words_combination = [*wordsList, *wordsUppercase, *wordsLowercase, *wordsUppercaseWithoutAccent, *wordsLowercaseWithoutAccent, *firstLetterUppercaseWithoutAccent, *firstLetterUppercase]

    # remove duplicate from list
    print(list(dict.fromkeys(words_combination)))

    # all_passwords = words_combination
    ##all_passwords_leet = self.convert_words_to_leet(self, words_combination)
    # print(all_passwords)
    ##print(all_passwords_leet)

combine_words()