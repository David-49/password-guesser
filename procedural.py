import time
from unidecode import unidecode
from flask import Flask, render_template, request

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

    
    print(list(dict.fromkeys(words_combination)))

    # all_passwords = words_combination
    ##all_passwords_leet = self.convert_words_to_leet(self, words_combination)
    # print(all_passwords)
    ##print(all_passwords_leet)

combine_words()