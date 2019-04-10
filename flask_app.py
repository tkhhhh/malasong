from flask import Flask
from flask import render_template,jsonify,request
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def mydict():
    return render_template('5.html')

if __name__ == '__main__':
    app.run()
