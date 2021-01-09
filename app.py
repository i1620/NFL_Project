from flask import Flask, render_template,request
import os

app = Flask(__name__)

@app.route('/')
@app.route('/<html>')
def home(html="index.html"):
    return render_template(html)

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

port = int(os.environ.get('PORT', 5000))

if __name__ == '__main__':
    app.run(debug=True, port=port)
    app.run(host="0.0.0.0")  # allows access from any computer