import os
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
    return render_template('question1.html')

@app.route('/question2',methods=['GET','POST'])
def renderQuestion2():
    session["answer1"]=request.form['answer1']
    return render_template('question2.html')

@app.route('/question3',methods=['GET','POST'])
def renderQuestion3():
    session["answer2"]=request.form['answer2']
    return render_template('question3.html')
    
@app.route('/question4',methods=['GET','POST'])
def renderQuestion4():
    session["answer3"]=request.form['answer3']
    return render_template('question4.html')
    
@app.route('/question5',methods=['GET','POST'])
def renderQuestion5():
    session["answer4"]=request.form['answer4']
    return render_template('question5.html')
    
@app.route('/results',methods=['GET','POST'])
def renderResults():
    session["answer5"]=request.form['answer5']
    return render_template('results.html')

def is_localhost():
    root_url = request.url_root
    developer_url = 'http://127.0.0.1:5000/'
    return root_url == developer_url
    
if __name__=="__main__":
    app.run(debug=True)
