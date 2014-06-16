__author__ = 'andrei'

from warnings import warn

from configs import reserved_uids
from Recommend_engine.neo4j_manager.db_dec import Graph_DB


class Inst_Init_Exception(Exception):
    pass


class DB_Exception(Exception):
    pass


def get_node_ID(Node):
    return str(Node).split('/')[-1][:-1]


#<========= Supporting methods =========>
filter_list = ['bothE','bothV','get', 'get_base_type', 'get_bundle', 'data', 'get_element_key', 'get_element_type',
               'get_index_keys', 'get_index_name', 'get_property_keys', 'get_proxy_class', 'inE', 'inV', 'map','outE',
               'outV', 'save', 'uid', 'element_type', 'eid']


def name_attrs(bulbs_class):
    baseclass = getattr(bulbs_class, 'element_class')
    lst = [elt for elt in dir(baseclass) if elt[:1] != '_' and elt not in filter_list]
    return lst


#<========= Routines that need to be shared by all the mirror classes =========>
def class2dict(self):
    names_list = name_attrs(self.DB_root)
    retdict = {}
    for name in names_list:
        if hasattr(self, name):
            retdict[name] = getattr(self, name)
    return retdict


def dict2class(self, dico):
    names_list = name_attrs(self.DB_root)
    for name, val in dico.iteritems():
        if name in names_list:
            setattr(self, name, val)


def class2node(self):
    names_list = name_attrs(self.DB_root)
    if not self.node:
        warn('Inflation of node from class %s failed. Provided node is empty' % self)
        raise Inst_Init_Exception
    else:
        for name in names_list:
            if hasattr(self, name):
                setattr(self.node, name, getattr(self, name))
        self.node.save()


def node2class(self):
    names_list = name_attrs(self.DB_root)
    if not self.node:
        warn('Inflation of class %s failed: provided node %s is empty' % (self, self.node))
        raise Inst_Init_Exception
    else:
        for name in names_list:
            setattr(self, name, getattr(self.node, name))


def check_class_attrs(self):
    names_list = name_attrs(self.DB_root)
    failed_list = []
    for name in names_list:
        if not hasattr(self, name):
            failed_list.append(name)
    if failed_list:
        warn("Following properties were not properly defined: %s" % failed_list)
        return False
    else:
        return True


def check_uid_availability(cls, uid):
    if uid in reserved_uids:
        return False
    node_generator = cls.DB_root.index.lookup(uid=uid)
    if node_generator:
        return False
    return True


def assign_uid(self, uid):
    if check_uid_availability(type(self), uid):
        self.node = self.DB_root.create(uid=uid)
        self.node_ID = get_node_ID(self.node)
        self.uid = uid
    else:
        warn("Attempted to assign a uid already used")
        raise Inst_Init_Exception


def assign_no_uid(self):
    self.node = self.DB_root.create(uid = "blank")
    self.node_ID = get_node_ID(self.node)
    self.uid = self.node_ID

    self.node.uid = self.node_ID
    self.node.save()


def common_init(self, uid=False, node_ID=False, node=False, anew=False):
    # Class or instance of a class? => instance is easier, because it requires just
    # just a self.call from the

    def _init_by_node():
        if self.node:
            self.node_ID = get_node_ID(self.node)
            self.uid = self.node.uid
            self.load()
        else:
            raise Inst_Init_Exception


    def _init_by_ID():
        self.node = self.DB_root.get(self.node_ID)
        _init_by_node()


    def _init_by_pseudo():
        generator = self.DB_root.index.lookup(uid=self.uid)
        if not generator:
            warn('No nodes were found for uid %s' % self.uid)
            raise Inst_Init_Exception
        nodes = [node for node in generator]
        if len(nodes) > 1:
            warn('Uid %s mapped to several nodes' % self.uid)
            raise Inst_Init_Exception
        else:
            self.node = nodes[0]
            _init_by_node()


    if not any([uid, node_ID, node, anew]):
        warn("Define uid, node_ID, node or define as new object")
        raise Inst_Init_Exception

    if node:
        self.node = node
        _init_by_node()

    if node_ID:
        self.node_ID = node_ID
        _init_by_ID()

    if uid:
        self.uid = uid
        _init_by_pseudo()

    if anew:
        # add a clause if there is no uid: create by node, then use node_Id as the uid
        if 'uid' in anew:
            self.assign_uid(anew['uid'])
        else:
            self.assign_no_uid()
        self.update(anew)


def common_node_delete(self):
    if not self.node:
        warn("No node attached to the mirror object %s" % type(self).__name__)
        raise DB_Exception
    self.DB_root.delete(self.node_ID)
    return True


def better_repr(self):
    return "<%s> %s" % (self.__class__.__name__, tuple((attr_name, getattr(self,attr_name)) for attr_name in name_attrs(self.DB_root)))


#<========= Routines that need to be shared by all the mirror classes =========>
attr_map = {
            "assign_no_uid": assign_no_uid,
            "assign_uid" : assign_uid,
            "dictify" : class2dict,
            "update" : dict2class,
            "save" : class2node,
            "load" : node2class,
            "check" : check_class_attrs,
            "delete_node" : common_node_delete,
            "check_uid_availability" : classmethod(check_uid_availability),
            "__init__" : common_init,
            "__repr__" : better_repr,
            "__str__" : better_repr,
        }


if __name__ == "__main__":
    print name_attrs(Graph_DB.Restaurant)
    print name_attrs(Graph_DB.Person)
    print name_attrs(Graph_DB.Review)
