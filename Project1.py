from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def calculate():
    if request.method == 'GET':
        return render_template('calculate.html')
    else:
        maths = float(request.form['maths'])
        chemistry = float(request.form['chemistry'])
        physics = float(request.form['physics'])
        computer_science = float(request.form['computer_science'])
        hindi = float(request.form['hindi'])

        average_marks = (maths + chemistry + physics + computer_science + hindi) / 5

        result = ""
        if average_marks >= 50:
            result = "success"
        else:
            result = "fail"

        return redirect(url_for(result, score=average_marks))

@app.route('/welcome')
def welcome():
    return "Welcome to the Flask Tutorials"

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    return "The person is passed, and the score is " + str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "The person has failed, and the score is " + str(score)

if __name__ == '__main__':
    app.run(debug=True)