__author__ = 'andrei'

from Recommend_engine.middle_ware.class_declarations.defaults import reserved_user_pseudos
from Recommend_engine.neo4j_manager.db_dec import Graph_DB
from warnings import warn


class Inst_Init_Exception(Exception):
    pass


class DB_Push_Exception(Exception):
    pass


def get_node_ID(Node):
    return str(Node).split('/')[-1][:-1]


# How can I make this part more testable?
# adding more separation won't work well, because the purpouse is to be
# a thin overlay over bulbs with DLL from JSON.

# Alternatively, we could define a superclass and use it's instaces to costumize the
# metaclasses

# example of a dictionary from which the opening hours inflate
# => how to manage time => UTC?
# => datelist as pythonic Dates? As a list of common closing days + costum vacations?
# =>

# Common DDT base:
    # Creation/destruction/modification by uid/node_id/node object
    # Use metaprogrqmming to get additional properties / inject functions?
    # verification of uid availability


Exdict = {"Weekly_schedule":{"M":('oh','clh','evoh', 'evcloh'),
                             "Tu":('oh','clh','evoh', 'evcloh'),
                             "W":('oh','clh','evoh', 'evcloh'),
                             "Th":('oh','clh','evoh', 'evcloh'),
                             "F":('oh','clh','evoh', 'evcloh'),
                             "S":('oh','clh','evoh', 'evcloh'),
                             "Sun":('oh','clh','evoh', 'evcloh')},
          "Vacations":['datelist']}


filter_list = ['bothE','bothV','get', 'get_base_type', 'get_bundle', 'data', 'get_element_key', 'get_element_type',
               'get_index_keys', 'get_index_name', 'get_property_keys', 'get_proxy_class', 'inE', 'inV', 'map','outE',
               'outV', 'save', 'UID']


def name_attrs(bulbs_class):
    baseclass = getattr(bulbs_class, 'element_class')
    lst = [elt for elt in dir(baseclass) if elt[:1] != '_' and elt not in filter_list]
    return lst


def node2class(bulbs_mirror_class, node):
    names_list = name_attrs(bulbs_mirror_class.DB_root)
    if not node:
        warn('Inflation of class %s failed: provided node %s is empty' % (bulbs_mirror_class, node))
        raise Inst_Init_Exception
    else:
        for name in names_list:
            setattr(bulbs_mirror_class, name, getattr(node, name))
        return bulbs_mirror_class

#<========= Routines that need to be shared by all the mirror classes =========>


def class2dict(bulbs_mirror_class):
    names_list = name_attrs(bulbs_mirror_class.DB_root)
    retdict = {}
    for name in names_list:
        retdict[name] = getattr(bulbs_mirror_class, name)
    return retdict

def dict2class(bulbs_mirror_class, dict): # creates a class from a dict
    names_list = name_attrs(bulbs_mirror_class.DB_root)
    for name in names_list:
        setattr(bulbs_mirror_class, name, dict[name])
    return bulbs_mirror_class


def class2node(bulbs_mirror_class, node):
    names_list = name_attrs(bulbs_mirror_class.DB_root)
    if not node:
        warn('Inflation of node %s failed from class %s: provided node is empty' % (node, bulbs_mirror_class))
        raise Inst_Init_Exception
    else:
        for name in names_list:
            setattr(node, name, getattr(bulbs_mirror_class, name))
        return bulbs_mirror_class


def check_class_attrs(bulbs_mirror_class):
    names_list = name_attrs(bulbs_mirror_class.DB_root)
    failed_list = []
    for name in names_list:
        if not hasattr(bulbs_mirror_class,name):
            failed_list.append(name)
    if failed_list:
        warn("Following properties were not properly defined: %s" % failed_list)
        return False
    else:
        return True


def check_uid_availability(klass, new_pseudo):
        if new_pseudo in reserved_user_pseudos:
            return False
        node_generator = klass.DB_root.index.lookup(pseudo=new_pseudo)
        if node_generator:
            return False
        return True


# <========= Needs to be called from inside the class for self-replacement =========>

def DDL_base(bulbs_mirror_class, uid, node_ID, node, anew):
    # Class or instance of a class? => instance is easier, because it requires just
    # just a self.call from the

    def _init_by_node():
        if bulbs_mirror_class.node:
            bulbs_mirror_class.node_ID = get_node_ID(bulbs_mirror_class.node)
            bulbs_mirror_class.uid= bulbs_mirror_class.node.UID
            node2class(bulbs_mirror_class, bulbs_mirror_class.node)
        else:
            raise Inst_Init_Exception


    def _init_by_ID():
        bulbs_mirror_class.node = bulbs_mirror_class.DB_root.get(bulbs_mirror_class.node_ID)
        _init_by_node()


    def _init_by_pseudo():
        generator = bulbs_mirror_class.DB_root.index.lookup(UID=bulbs_mirror_class.uid)
        if not generator:
            raise Inst_Init_Exception
        nodes = [node for node in generator]
        if len(nodes) > 1:
            raise Inst_Init_Exception
        else:
            bulbs_mirror_class.node = nodes[0]
            _init_by_node()

    if not any([uid, node_ID, node, anew]):
        warn("Define uid, node_ID, node or define as new object")
        raise Inst_Init_Exception

    if node:
        bulbs_mirror_class.node = node
        bulbs_mirror_class = _init_by_node()

    if node_ID:
        bulbs_mirror_class.node_ID = node_ID
        bulbs_mirror_class = _init_by_ID()

    if uid:
        bulbs_mirror_class.pseudo = uid
        bulbs_mirror_class = _init_by_pseudo()

    if anew:
        bulbs_mirror_class.anew = True

    return bulbs_mirror_class


class Restau(object):
    DB_root = Graph_DB.Restaurant

    def __init__(self, uid=False, node_ID=False, node=False, anew=False):
        self = DDL_base(self, uid, node_ID, node, anew)
        print self.anew


if __name__ == "__main__":
    print name_attrs(Graph_DB.Restaurant)
    print name_attrs(Graph_DB.Person)
    print name_attrs(Graph_DB.Review)
    Restau(anew = True)
