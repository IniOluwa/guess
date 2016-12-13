from flask import Flask, render_template

app = Flask(__name__)
questions = ['Are they ninjas?', 'Do they have Dragon Balls?', 'Are they souls?', 'Do they have devil fruits?', 'Are they Mages?']
guesses = ['Naruto', 'One Piece', 'Bleach', 'Fairytail', 'DBS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/question/<int:id>')
def question(id):
    return render_template('question.html', question=questions[id])

@app.route('/guess/<int:id>')
def guess(id):
    return render_template('guess.html', guess=guesses[id])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
