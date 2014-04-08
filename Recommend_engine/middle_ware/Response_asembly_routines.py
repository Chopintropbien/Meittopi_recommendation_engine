__author__ = 'andrei'

from Recommend_engine.neo4j_manager.db_dec import Graph_DB


class Inst_Init_Exception(Exception):
    pass


class DB_Push_Exception(Exception):
    pass


class UID_overload_Exception(Exception):
    pass


def get_node_ID(Node):
    return str(Node).split('/')[-1][:-1]


class Person(object):

    DB_root = Graph_DB.Person

    def __init__(self, pseudo = None, node_ID=None):
        self.pseudo = ''
        self.name = ''
        self.node_ID = ''
        self.Node = ''

        if not pseudo and not node_ID:
            raise Exception("Define pseudo or node_ID")

        if node_ID:
            self.node_ID = node_ID
            self._init_by_ID()

        if pseudo:
            self.pseudo=pseudo
            self._init_by_pseudo()


    def _init_by_ID(self):
        self.Node = self.DB_root.get(self.node_ID)
        if self.Node:
            self.pseudo = self.Node.pseudo
            self.name = self.Node.name
        else:
            raise Inst_Init_Exception


    def _init_by_pseudo(self):
        generator = self.DB_root.index.lookup(pseudo=self.pseudo)
        if not generator:
            raise Inst_Init_Exception
        nodes = []
        for node in generator:
            nodes.append(node)
        if len(nodes)>1:
            raise Inst_Init_Exception
        else:
            self.Node = nodes[0]
            self.name = self.Node.name
            self.Node_ID = get_node_ID(self.Node)


    def _push_to_DB(self):
        # check if we are updating
        if self.Node:
            pass
        # check if a name collision already exists
        if self.DB_root.index.lookup(pseudo=self.pseudo):
            pass
        # if we are creating a new node with a new UID



    def _get_picture(self):
        pass


    def _get_profile(self):
        pass


    def _list_reviews(self):
        pass


    def _list_Compliments_from(self):
        pass


    def _list_Compliments_to(self, unread=True):
        pass


    def _list_created_events(self):
        pass


    def _list_attended_events(self):
        pass