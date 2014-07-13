__author__ = 'andrei'

from configs import app_home, app_base_url
from collections import OrderedDict


pseudo_available = OrderedDict([
    ("title", "Demand if pseudo is available:"),
    ("address", app_base_url+"user/check_pseudo/<pseudo>"),
    ("type", "GET"),
    ("response example", "{'available': true, 'pseudo': 'andrei'}"),
    ("response type", "JSON"),
    ("requires user logged_in", False),
    ])


restaurant_name_available = OrderedDict([
    ("title", "Demand if restaurant name is available:"),
    ("address", app_base_url+"restaurant/check_name/<resto_name>"),
    ("type", "GET"),
    ("response example", "{'available':true, 'resto_name': 'Chez Jaime - Lausanne'}"),
    ("response type", "JSON"),
    ("requires user logged_in", False),
    ])


def get_API_list():
    return [item for item in globals().items() if item[0][:2] != '__' and not item[0] in ['generate_API_specs',
                                                                                          'OrderedDict', 'app_home',
                                                                                          'get_API_list', "app_base_url"]]


def generate_API_specs():

    def p_format(API_spec_dict):
        print API_spec_dict
        collectlist = []
        collectlist.append(API_spec_dict["title"])
        for key, val in API_spec_dict.iteritems():
            if key!="title":
                collectlist.append('\t'+str(key)+'\t:\t'+str(val))
        collectlist.append('\n')
        return '\n'.join(collectlist)

    APIs = get_API_list()
    fle = open(app_home+'/API_specs.md', 'w')
    for API in APIs:
        fle.write(p_format(API[1]))


if __name__ == "__main__":
    generate_API_specs()