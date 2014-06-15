__author__ = 'andrei'

from copy import deepcopy
import json

# example of a dictionary from which the opening hours inflate
# => how to manage time => UTC?
# => datelist as pythonic Dates? As a list of common closing days + costum vacations?


# mo-mc and evo-evc are replaced by - if the restaurant is closed during those hours.

Exdict = {"Weekly_schedule":{"Mon" : ('mo','mc','evo', 'evc'),
                             "Tue" : ('mo','mc','evo', 'evc'),
                             "Wed" : ('mo','mc','evo', 'evc'),
                             "Thu" : ('mo','mc','evo', 'evc'),
                             "Fri" : ('mo','mc','evo', 'evc'),
                             "Sat" : ('mo','mc','evo', 'evc'),
                             "Sun" : ('mo','mc','evo', 'evc')},
          "Vacations":['datelist']}


class DaytimeWrapper(object):

    def __init__(self):
        self.payload = deepcopy(Exdict)

    def class2JSON(self):
        return json.dumps(self.payload)

    def JSON2class(self, JSON):
        self.payload = json.loads(self.payload)