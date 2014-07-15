__author__ = 'andrei'

from configs import app_home, app_base_url
from collections import OrderedDict


pseudo_available = OrderedDict([
    ("title", "Demand if pseudo is available:"),
    ("address", app_base_url+"user/pseudo_available"),
    ("type", "GET"),
    ("payload", "{'uid':'Lauriane'}"),
    ("response code", "200"),
    ("response example", "{'available': true, 'pseudo': 'Lauriane'}"),
    ("response type", "JSON"),
    ("requires user logged_in", False),
    ])


restaurant_name_available = OrderedDict([
    ("title", "Demand if restaurant name is available:"),
    ("address", app_base_url+"restaurant/name_available"),
    ("type", "GET"),
    ("payload", "{'uid':'andrei'}"),
    ("response code", '200'),
    ("response example", "{'available':true, 'resto_name': 'Chez Jaime - Lausanne'}"),
    ("response type", "JSON"),
    ("requires user logged_in", False),
    ])


get_person = OrderedDict([
    ("title", "Get a minimal representation of a user information:"),
    ("address", app_base_url+"user"),
    ("type", "GET"),
    ("payload", "{'uid':'Lauriane','nodeID':'1','full':'False'}"),
    ("response code", '200 if success, 404 or 412 in case of failure'),
    ("response example", "{joined_on': '2014-5-25', 'birthday': '1993-8-4', 'name': 'Lauriane Mollier','pseudo': 'lauriane', 'picture': [{'type': 'other_profile', 'quality': 1.0, 'uid': '8', 'payload': 'test_picture_payload-22'}]}"),
    ("response type", "JSON"),
    ("requires user logged_in", True),
    ])


get_person_full = OrderedDict([
    ("title", "Get a full representation of a user information:"),
    ("address", app_base_url+"user"),
    ("type", "GET"),
    ("payload", "{'uid':'Lauriane','nodeID':'1','full':'True'}"),
    ("response code", '200 if success, 404 or 412 in case of failure'),
    ("response example", "{joined_on': '2014-5-25', 'birthday': '1993-8-4', 'name': 'Lauriane Mollier','pseudo': 'lauriane', 'picture': [{'type': 'other_profile', 'quality': 1.0, 'uid': '8', 'payload': 'test_picture_payload-22'}], 'review_list': [{'picture': [], 'creation_date': u'2014-05-26', 'contents': u'Mloppily mlop blopity blopopblop', 'title': u'the mloppest mlop is mloppily mlop'}], 'follows': [], 'followers': [] }"),
    ("response type", "JSON"),
    ("requires user logged_in", False),
    ])


get_restaurant = OrderedDict([
    ("title", "Get a minimal representation of a restaurant information:"),
    ("address", app_base_url+"restaurant"),
    ("type", "GET"),
    ("payload", "{'uid':'mlop','uid':'4','full':'False'}"),
    ("response code", '200 if success, 404 or 412 in case of failure'),
    ("response example", "{'picture': [], 'added': '2014-05-26', 'name': 'the mloppest mlop', 'opening_date': None, 'operation_hours': '11-23', 'pseudo': 'mlop'}"),
    ("response type", "JSON"),
    ("requires user logged_in", False),
    ])


get_restaurant_full = OrderedDict([
    ("title", "Get a full representation of a restaurant information:"),
    ("address", app_base_url+"restaurant"),
    ("type", "GET"),
    ("payload", "{'uid':'mlop','uid':'4','full':'True'}"),
    ("response code", '200 if success, 404 or 412 in case of failure'),
    ("response example", "{'review_list': [], 'picture': [], 'added':'2014-05-26', 'followers': [], 'name': 'the mloppest mlop', 'opening_date': None, 'operation_hours': '11-23', 'pseudo': 'mlop'}"),
    ("response type", "JSON"),
    ("requires user logged_in", False),
    ])

post_person = OrderedDict([
    ("title", "Add a user to the database :"),
    ("address", app_base_url+"user"),
    ("type", "GET"),
    ("payload", "{'uid':'Lauriane','name':'Lauriane Mollier','birthday':'1993-8-4'}"),
    ("response code", '200 if success, 404 or 412 in case of failure'),
    ("response example", "{''}"),
    ("response type", "JSON"),
    ("requires user logged_in", True),
    ])


post_restaurant = OrderedDict([
    ("title", "Add a restaurant to the database:"),
    ("address", app_base_url+"user"),
    ("type", "POST"),
    ("payload", "{'uid':'mlop','name':'1','opening_date':2014-5-26,'operation_horus':'11-23'}"),
    ("response code", '200 if success, 404 in case of failure'),
    ("response example", "{''}"),
    ("response type", "JSON"),
    ("requires user logged_in", False),
    ])


post_review = OrderedDict([
    ("title", "Add a review to the database:"),
    ("address", app_base_url+"restaurant"),
    ("type", "POST"),
    ("payload", "{'user_uid':'Lauriane', 'restau_uid':'mlop', 'title':'bloppidy mlop is mloppy blop', 'contents':'boppity blop is blopppidiest bop in town'}"),
    ("response code", '200 if success, 404 in case of failure'),
    ("response example", "{''}"),
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
            if key not in ["title", "requires user logged_in"]:
                collectlist.append('\t'+str(key)+'\t:\t'+str(val))
        collectlist.append('\n\n')
        return '\n'.join(collectlist)

    APIs = get_API_list()
    fle = open(app_home+'/API_specs.md', 'w')
    for API in APIs:
        fle.write(p_format(API[1]))


if __name__ == "__main__":
    generate_API_specs()