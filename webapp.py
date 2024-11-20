import os
import time
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

app.secret_key=os.environ["SECRET_KEY"];

@app.route("/")
def render_main():
    return render_template('home.html')
    
@app.route('/startOver')
def startOver():
    session.clear()    
    return redirect(url_for('render_main'))
    
@app.route('/question1')
def renderQuestion1():
    timeelapsed=0
    session["time1"] = time.time()
    return render_template('question1.html')

@app.route('/question2',methods=['GET','POST'])
def renderQuestion2():
    if not "answer1" in session:
        session["answer1"]=request.form['answer1']
    return render_template('question2.html')

@app.route('/question3',methods=['GET','POST'])
def renderQuestion3():
    if not "answer2" in session:
        session["answer2"]=request.form['answer2']
    return render_template('question3.html')
    
@app.route('/question4',methods=['GET','POST'])
def renderQuestion4():
    if not "answer3" in session:
        session["answer3"]=request.form['answer3']
    return render_template('question4.html')
    
@app.route('/question5',methods=['GET','POST'])
def renderQuestion5():
    if not "answer4" in session:
        session["answer4"]=request.form['answer4']
    return render_template('question5.html')
    
@app.route('/results',methods=['GET','POST'])
def renderResults():
    if not "answer5" in session:
        session["answer5"]=request.form['answer5']
    correct=0
    if session["answer1"]=="4":
        correct=correct+1
        session["answer1"]="CORRECT"
    else:
        session["answer1"]="INCORRECT"
        
    if session["answer2"]=="3":
        correct=correct+1
        session["answer2"]="CORRECT"
    else:
        session["answer2"]="INCORRECT"
        
    if session["answer3"]=="1":
        correct=correct+1
        session["answer3"]="CORRECT"
    else:
        session["answer3"]="INCORRECT"
        
    if session["answer4"]=="2":
        correct=correct+1
        session["answer4"]="CORRECT"
    else:
        session["answer4"]="INCORRECT"
        
    if session["answer5"]=="1":
        correct=correct+1
        session["answer5"]="CORRECT"
    else:
        session["answer5"]="INCORRECT"
        
    session["time2"] = time.time()
    timediff = session["time2"]-session["time1"]
    return render_template('results.html', time=timediff, correct=correct*20)

def is_localhost():
    root_url = request.url_root
    developer_url = 'http://127.0.0.1:5000/'
    return root_url == developer_url
    
if __name__=="__main__":
    app.run(debug=True)
