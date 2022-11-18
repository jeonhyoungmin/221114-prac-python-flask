from flask import Flask, url_for, render_template
from flask import request
import json

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello(name = None):
    return render_template('test.html', name=name)

@app.route('/post', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return 'hello flask'
    elif request.method == 'POST':
        print(request.__dict__)
        return 'hello post'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 8080)