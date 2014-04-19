__author__ = 'andrei'

import hashlib
from Recommend_engine.neo4j_manager.db_dec import Graph_DB
from Common_tools import *
from datetime import date

class Restaurant(object):

    DB_root = Graph_DB.Profile

    def __init__(self, UID = None, node_ID=None, Node=None, payload=None):
        self.UID = ''
        self.node_ID = ''
        self.Node = ''

        self.name = ''
        self.opened = date.today()
        self.added = date.today()

        if not UID and not node_ID and not Node and not payload:
            raise Exception("Define pseudo, node_ID or Node")

        if Node:
            self.Node = Node
            self._init_by_node()

        if node_ID:
            self.node_ID = node_ID
            self._init_by_ID()

        if UID:
            self.UID=UID
            self._init_by_UID()

        if payload:
            self._init_by_payload(payload)


    def _init_by_payload(self, payload):



    def _init_by_ID(self):
        self.Node = self.DB_root.get(self.node_ID)
        if self.Node:
            self.UID = self.Node.UID
            self.name = self.Node.name
            self.opened = self.Node.opened
            self.added = self.Node.added
        else:
            raise Inst_Init_Exception


    def _init_by_UID(self):
        generator = self.DB_root.index.lookup(pseudo=self.UID)
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
            self.opened = self.Node.opened
            self.added = self.Node.added


    def _init_by_node(self):
        if self.Node:
            self.Node_ID = get_node_ID(self.Node)
            self.UID = self.Node.UID
            self.name = self.Node.name
            self.opened = self.Node.opened
            self.added = self.Node.added
        else:
            raise Inst_Init_Exception


    def _push_to_DB(self):
        # check if we are updating
        if self.Node:
            pass
        # check if a name collision already exists
        if self.DB_root.index.lookup(UID=self.UID):
            pass
        # if we are creating a new node with a new UID
        pass


    def _render_for_json(self):
        return {"UID":self.UID,
                "name":self.UID,
                "picture":self._get_picture(),
                "Node_ID":self.Node_ID,
                "Address":self._get_position()
                }


    def _long_render_for_json(self):
        return self._render_for_json().update({
                            "review_list":[],
                            "followers":[],
                            "events":[],
                            })


    def _get_picture_Node(self):
        picture_generator = self.Node.outV("image")
        if not picture_generator:
            return None
        for node in picture_generator:
            if node.primary:
                return node


    def _get_picture(self):
        picture_Node = self._get_picture_Node()
        if picture_Node:
            return picture_Node
        return ''  # default_picture?


    def _get_all_picture_Nodes(self):
        picture_generator = self.Node.outV("image")
        if not picture_generator:
            return None
        Node_Accumulator = []
        for node in picture_generator:
            Node_Accumulator.append(node)
        return Node_Accumulator


    def _add_picture(self, new_picture, type, primary):
        # TODO: improve to take in account not only the hexdigest, but all in all
            # visual picture similarity (for instance Daisy evaluation)
        new_hash = hashlib.md5(new_picture).hexdigest()
        existing_hashes = [hashlib.md5(node.payload).hexdigest() for node in self._get_all_picture_Nodes()]
        if new_hash in existing_hashes:
            if new_picture in [node.payload for node in self._get_all_picture_Nodes()]:
                return False
        image_node = Graph_DB.Image.create(type = type,
                                     primary = primary,
                                     payload = new_picture)
        Graph_DB.image.create(self.Node, image_node)
        return True


    def _get_opening_hours(self):
        # uses a jsonified function of opening hours to unfold it into the
            # opening and closing hours
        pass


    def _modify_opening_hours(self):
        pass


    def _modify_opening_hours_special_days(self):
        pass


    def _check_if_opened(self, time):
        pass





    def _most_prominent_features(self):
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


def generate_from_location(Location_Node, type_of_moving):
    pass