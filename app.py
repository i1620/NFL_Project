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
