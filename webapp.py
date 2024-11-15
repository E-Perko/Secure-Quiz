import os
import datetime
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

time1 = 0
correct = []

app = Flask(__name__)

app.secret_key=os.environ["SECRET_KEY"];

@app.route("/")
def render_main():
    return render_template('home.html')
    
@app.route('/startOver')
def startOver():
    session.clear()
    correct.clear()    
    return redirect(url_for('render_main'))
    
    
@app.route('/question1')
def renderQuestion1():
    global time1
    time1 = datetime.datetime.now()
    return render_template('question1.html')

@app.route('/question2',methods=['GET','POST'])
def renderQuestion2():
    session["answer1"]=request.form['answer1']
    global correct
    if session["answer1"]=="4":
        correct.append(1)
        session["answer1"]="CORRECT"
    else:
        correct.append(0)
        session["answer1"]="INCORRECT"
    return render_template('question2.html')

@app.route('/question3',methods=['GET','POST'])
def renderQuestion3():
    session["answer2"]=request.form['answer2']
    global correct
    if session["answer2"]=="3":
        correct.append(1)
        session["answer2"]="CORRECT"
    else:
        correct.append(0)
        session["answer2"]="INCORRECT"
    return render_template('question3.html')
    
@app.route('/question4',methods=['GET','POST'])
def renderQuestion4():
    session["answer3"]=request.form['answer3']
    global correct
    if session["answer3"]=="1":
        correct.append(1)
        session["answer3"]="CORRECT"
    else:
        correct.append(0)
        session["answer3"]="INCORRECT"
    return render_template('question4.html')
    
@app.route('/question5',methods=['GET','POST'])
def renderQuestion5():
    session["answer4"]=request.form['answer4']
    global correct
    if session["answer4"]=="2":
        correct.append(1)
        session["answer4"]="CORRECT"
    else:
        correct.append(0)
        session["answer4"]="INCORRECT"
    return render_template('question5.html')
    
@app.route('/results',methods=['GET','POST'])
def renderResults():
    session["answer5"]=request.form['answer5']
    global correct
    if session["answer5"]=="1":
        correct.append(1)
        session["answer5"]="CORRECT"
    else:
        correct.append(0)
        session["answer5"]="INCORRECT"
    time2 = datetime.datetime.now()
    global time1
    time = time2-time1
    return render_template('results.html', time=time, correct=sum(correct)*20)

def is_localhost():
    root_url = request.url_root
    developer_url = 'http://127.0.0.1:5000/'
    return root_url == developer_url
    
if __name__=="__main__":
    app.run(debug=True)
