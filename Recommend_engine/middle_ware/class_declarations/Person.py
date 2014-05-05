__author__ = 'andrei'

from Recommend_engine.middle_ware.class_declarations.defaults import default_User_Pic, reserved_user_pseudos
from Recommend_engine.neo4j_manager.db_dec import Graph_DB
from Recommend_engine.middle_ware.Common_tools import *
from datetime import date


class Person(object):

    DB_root = Graph_DB.Person

    def __init__(self, pseudo=None, node_ID=None, Node=None, anew=False):
        self.pseudo = ''
        self.node_ID = ''
        self.node = ''

        self.name = ''
        self.open_ID_Links = ''
        self.joined_on = date.today()
        self.birthday = date.today()

        if not pseudo and not node_ID and not Node and not anew:
            raise Exception("Define pseudo, node_ID or Node")

        if Node:
            self.node = Node
            self._init_by_node()

        if node_ID:
            self.node_ID = node_ID
            self._init_by_ID()

        if pseudo:
            self.pseudo=pseudo
            self._init_by_pseudo()


    def _init_by_ID(self):
        self.node = self.DB_root.get(self.node_ID)
        if self.node:
            self.pseudo = self.node.pseudo
            self.name = self.node.name
            self.open_ID_Links= self.node.openID_Links
            self.joined_on = self.node.joined_on
            self.birthday = self.node.birthday
        else:
            raise Inst_Init_Exception


    def _init_by_pseudo(self):
        generator = self.DB_root.index.lookup(pseudo=self.pseudo)
        if not generator:
            raise Inst_Init_Exception
        nodes = []
        for node in generator:
            nodes.append(node)
        if len(nodes) > 1:
            raise Inst_Init_Exception
        else:
            self.node = nodes[0]
            self.node_ID = get_node_ID(self.node)
            self.name = self.node.name
            self.open_ID_Links = self.node.openID_Links
            self.joined_on = self.node.joined_on
            self.birthday = self.node.birthday


    def _init_by_node(self):
        if self.node:
            self.node_ID = get_node_ID(self.node)
            self.pseudo = self.node.pseudo
            self.name = self.node.name
            self.open_ID_Links = self.node.openID_Links
            self.joined_on = self.node.joined_on
            self.birthday = self.node.birthday
        else:
            raise Inst_Init_Exception

    @classmethod
    def check_pseudo_availability(cls, new_pseudo):
        if new_pseudo in reserved_user_pseudos:
            return False
        node_generator = Graph_DB.Person.index.lookup(pseudo=new_pseudo)
        if node_generator:
            return False
        return True

    def _create_anew(self, name, pseudo, joined_on, birthday):
        self.pseudo = pseudo
        self.name = name
        self.joined_on = joined_on
        self.birthday = birthday
        self.open_ID_Links =''
        if self.check_pseudo_availability(pseudo):
            Graph_DB.Person.create(pseudo=pseudo, name=name, joined_on=joined_on, birthday=birthday)
            return True
        else:
            print 'attempted to duplicate pseudo: %s' % pseudo
            return False


    def _update(self, name=None, joined_on=None, birthday=None):
        pass


    def _render_for_json(self):
        return {"pseudo":self.pseudo,
                "name":self.pseudo,
                "picture":self._get_picture(),
                "Node_ID":self.node_ID,
                "open_ID_Links":self.open_ID_Links}


    def _long_render_for_json(self):
        return self._render_for_json().update({
                            "review_list":self._list_reviews(),
                            "followers":self._list_followers(),
                            "follows":self._list_follows() })


    def _get_picture_Node(self):
        picture_generator = self.node.outV("image")
        if not picture_generator:
            return None
        for node in picture_generator:
            if node.primary and node.type == 'profile':
                return node


    def _get_picture(self):
        picture_Node = self._get_picture_Node()
        if picture_Node:
            return picture_Node
        return default_User_Pic


    def _change_picture(self, new_pic):
        """
        Replaces an old profile picture by a new picture

        :param new_pic:
        """
        old_pic_Node = self._get_picture_Node()
        if old_pic_Node is not None:
            old_pic_Node.payload = new_pic
        else:
            old_pic_Node = Graph_DB.Image.create(im_type='profile', primary='True', payload=new_pic)
            Graph_DB.image.create(self.node, old_pic_Node)


    def _get_feature_matrix(self):
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

    def _list_followers(self):
        pass

    def _list_follows(self):
        pass
