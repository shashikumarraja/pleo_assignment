"""
Entry point of the webapp
"""
from flask import Flask, request, render_template
from utils import format_num

app = Flask(__name__)


@app.route('/')
def render_homepage():
    """
    Default view on page load
    """
    return render_template('home.html')


@app.route('/', methods=['POST'])
def format_money():
    """
    Formats the input number based on a rule
    """
    input_number = request.form['amount']
    result = format_num(input_number, [(',', ' ')])
    return render_template('home.html', value=result)


if __name__ == '__main__':
    app.run(debug=True)
