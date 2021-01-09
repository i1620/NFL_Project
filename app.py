<<<<<<< HEAD
from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
@app.route('/<html>')
def home(html="index.html"):
    return render_template(html)



port = int(os.environ.get('PORT', 5000))

if __name__ == '__main__':
    app.run(debug=True, port=port)
    app.run(host="0.0.0.0")  # allows access from any computer
=======
from flask import Flask,render_template,request
 
app = Flask(__name__)
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/teamPlays.html')
def teamPlays():
    return render_template('teamPlays.html')


@app.route('/form')
def form():
    return render_template('form.html')
 
@app.route('/data', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form = request.form
     
        return render_template('data.html',form = form)
 
 
app.run(host='localhost', port=5000)
>>>>>>> d5c86d240252237bd1dd6f494225845695200809
