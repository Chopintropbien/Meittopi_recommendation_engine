__author__ = 'andrei'

from Recommend_engine.neo4j_manager.db_dec import Graph_DB
from Common_tools import *
from Profile import Profile

class Person(object):

    DB_root = Graph_DB.Person

    def __init__(self, pseudo = None, node_ID=None, Node=None):
        self.pseudo = ''
        self.name = ''
        self.node_ID = ''
        self.Node = ''

        if not pseudo and not node_ID and not Node:
            raise Exception("Define pseudo, node_ID or Node")

        if Node:
            self.Node = Node
            self._init_by_node()

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

    def _init_by_node(self):
        if self.Node:
            self.pseudo = self.Node.pseudo
            self.name = self.Node.name
            self.Node_ID = get_node_ID(self.Node)
        else:
            raise Inst_Init_Exception

    def _push_to_DB(self):
        # check if we are updating
        if self.Node:
            pass
        # check if a name collision already exists
        if self.DB_root.index.lookup(pseudo=self.pseudo):
            pass
        # if we are creating a new node with a new UID
        pass


    def _render_for_json(self):
        return {"pseudo":self.pseudo, "name":self.pseudo, "picture":self._get_picture(), "Node_ID":self.Node_ID}


    def _get_picture_Node(self):
        picture_generator = self.Node.outV("image")
        if not picture_generator:
            return None
        for node in picture_generator:
            if node.primary and node.type == 'profile':
                return node


    def _get_picture(self):
        picture_Node = self._get_picture_Node()
        if picture_Node:
            return picture_Node
        return ''  # default_picture?


    def _get_profile(self):
        Profile_Gen = self.Node.outV("profile")
        if not Profile_Gen:
            return None # manage unregistered user
        for profile in Profile_Gen:
            return Profile._init_by_node(profile)


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

