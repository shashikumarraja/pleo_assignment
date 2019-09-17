"""
Entry point of the webapp
"""
import logging
from flask import Flask, request, render_template, jsonify
from src.utils import format_num

app = Flask(__name__)
logger = app.logger

@app.route('/')
def render_homepage():
    """
    Default view on page load
    """
    return render_template('home.html')

@app.errorhandler(ValueError)
def handle_custom_exception(error, message):
    '''Return a custom message and 400 status code'''
    return jsonify({'message': message}), 400

@app.route('/format_money')
def format_money():
    """
    Formats the input number based on a rule
    """
    argument = request.args.get('number', '')
    try:
        input_number = float(argument)
    except ValueError as error:
        logger.error(error)
        return handle_custom_exception(error, 'Please enter a valid number')
    result = format_num(input_number, [(',', ' ')])
    logger.info('result: %s' % result)
    return jsonify({"original_number":input_number, "formatted_number": result})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
