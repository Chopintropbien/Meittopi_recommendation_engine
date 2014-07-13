__author__ = 'andrei'

from flask import Flask, jsonify, url_for,  session, redirect, escape, request
from flask.ext.script import Manager
from Recommend_engine.middle_ware.class_declarations.HigherClasses import Person, Restaurant
from configs import app_base_url


app = Flask(__name__)
manager = Manager(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('user/check_pseudo/<pseudo>')
def pseudo_check(pseudo):
    available = Person.check_uid_availability(pseudo)
    return jsonify({'pseudo':pseudo, 'available': available})


@app.route('restaurant/check_name/<resto_name>')
def resto_name_check(resto_name):
    available = Restaurant.check_uid_availability(resto_name)
    return jsonify({'resto_name':resto_name, 'available': available})


@app.route('restaurant/ ')



@manager.command
def list_routes():
    import urllib
    output = []
    for rule in app.url_map.iter_rules():

        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = tuple(rule.methods)
        url = urllib.unquote(url_for(rule.endpoint, **options)).replace('[','<').replace(']','>')
        output.append((rule.endpoint, methods, url))

    return output


def get_routes():
    with app.test_request_context() as ctx:
        routelist = list_routes()
        return routelist, [app_base_url+route[-1] for route in routelist]


if __name__ == '__main__':
    app.run()
