from flask import Flask, render_template, request
from random import shuffle
from csv import DictReader

app = Flask(__name__)

with open("questions.csv", "r", encoding='cp1252') as file:
    csv_reader = DictReader(file)
    questions = list(csv_reader)


@app.route('/', methods=['GET', 'POST'])
def show_question():
    index = 0
    l = len(questions)
    if request.method == 'GET':
        shuffle(questions)
        question = questions[index]
        return render_template('question.html', question=question["question"], index=index)
    else:
        index = int(request.form["index"])
        question = questions[index]
        guess = request.form["guess"].lower()
        answer = question["answer"].lower()
        detailed = ''
        if guess == answer:
            detailed = question["detailed"]
        elif guess == '':
            if index < l-1:
                index += 1
            else:
                detailed = "THATS ALL FOLKS"
            question = questions[index]
        else:
            detailed = "GIT GUD"
        return render_template('question.html', question=question["question"], index=index, detailed=detailed)


app.run(host='127.0.0.1', port=50000)
