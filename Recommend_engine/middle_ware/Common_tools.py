__author__ = 'andrei'


class Inst_Init_Exception(Exception):
    pass


class DB_Push_Exception(Exception):
    pass


class UID_overload_Exception(Exception):
    pass


def get_node_ID(Node):
    return str(Node).split('/')[-1][:-1]

# example of a dictionary from which the opening hours inflate
# => how to manage time => UTC?
# => datelist as pythonic Dates? As a list of common closing days + costum vacations?
# =>
Exdict = {"Weekly_schedule":{"M":('oh','clh','evoh', 'evcloh'),
                             "Tu":('oh','clh','evoh', 'evcloh'),
                             "W":('oh','clh','evoh', 'evcloh'),
                             "Th":('oh','clh','evoh', 'evcloh'),
                             "F":('oh','clh','evoh', 'evcloh'),
                             "S":('oh','clh','evoh', 'evcloh'),
                             "Sun":('oh','clh','evoh', 'evcloh')},
          "Vacations":['datelist']}