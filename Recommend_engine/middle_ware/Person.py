__author__ = 'andrei'
from Recommend_engine.neo4j_manager.db_dec import Graph_DB
from Common_tools import *
from datetime import date


class Person(object):

    DB_root = Graph_DB.Profile

    def __init__(self, pseudo = None, node_ID=None, Node=None):
        self.pseudo = ''
        self.node_ID = ''
        self.Node = ''

        self.name = ''
        self.open_ID_Links = ''
        self.joined_on = date.today()
        self.accessed = 0
        self.birthday = date.today()

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
            self.openID_Links = self.Node.openID_Links
            self.joined_on = self.Node.joined_on
            self.accessed = self.Node.accessed
            self.birthday = self.Node.birthday
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
            self.Node_ID = get_node_ID(self.Node)
            self.name = self.Node.name
            self.openID_Links = self.Node.openID_Links
            self.joined_on = self.Node.joined_on
            self.accessed = self.Node.accessed
            self.birthday = self.Node.birthday


    def _init_by_node(self):
        if self.Node:
            self.Node_ID = get_node_ID(self.Node)
            self.pseudo = self.Node.pseudo
            self.name = self.Node.name
            self.openID_Links = self.Node.openID_Links
            self.joined_on = self.Node.joined_on
            self.accessed = self.Node.accessed
            self.birthday = self.Node.birthday
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
        return {"pseudo":self.pseudo,
                "name":self.pseudo,
                "picture":self._get_picture(),
                "Node_ID":self.Node_ID,
                "open_ID_Links":self.Node_ID}


    def _long_render_for_json(self):
        return self._render_for_json().update({
                            "review_list":[],
                            "followers":[],
                            "follows":[] })


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


    def _add_picture(self):
        pass


    def _most_prominent_features(self):
        pass

    def _leadership_potential(self):
        # Attention! this one is specific towards certains persons or certains groups
        pass


    def _list_recommended_restaurants(self):
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

