__author__ = 'andrei'

from flask import Flask, jsonify
from Recommend_engine.middle_ware.class_declarations.Person import Person

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/pseudo_check/<pseudo>')
def pseudo_check(pseudo):
    available = Person.check_pseudo_availability(pseudo)
    return jsonify({'pseudo':pseudo, 'available': available})

if __name__ == '__main__':
    app.run()
