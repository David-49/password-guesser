from password import Password
# from flask import Flask, render_template, request

""" app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    words = request.form['mots']
    date = request.form['date']
    characters = request.form['characters']
    leet = request.form['leet']

    wordsList = []
    for word in words.split(','):
            wordsList.append(word.strip())

    password = Password({wordsList, date, characters, leet})
    print(password.concat_combinations());

if __name__ == '__main__':
    app.run(debug=True)

submit() """

words = input("Ajouter une liste de mots :\n")

#date = input("Ajouter une date (YYYY/MM/DD) :\n")

wordsList = []
for word in words.split(','):
        wordsList.append(word.strip())
date = "2023/04/13"
characters = False
leet = False
dateLang = 'FR'

dataForm = {
    'words': wordsList,
    'date': date
}

options = {
    'leet': leet,
    'specialCharacters': characters,
    'dateLang': dateLang
}

password = Password(dataForm, options)
result = password.concat_combinations();

print(result)