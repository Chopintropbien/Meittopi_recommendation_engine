__author__ = 'andrei'

from datetime import datetime

from configs import default_review_pic
from Recommend_engine.middle_ware.class_declarations.RootMethods import *



# Enhancements possibilities:
    # - output the graph interfaces as a separate module
        # This module would take the informations provided by the core
        # object and perform the _init/_create/_update routines
    # - output the image interfaces as a separate module:
        # General search for multiple images that are linked to the given
        # object. Return them as block with identifiers
        # In addition it manages all the routines of image_adding
        # ? None-Single-Multiple fitting to the user connexion?
    # - Remains in the class:
        # * Internals
        # * Render for JSON
        # * Add/delete relations routines (Only for persons and restaurants)
        # * Add/delete like, compliment for Review, Person, Restaurant, List, Event


class Review(object):

    DB_root = Graph_DB.Review

    def __init__(self, uid=None, node_ID=None, Node=None, new=False):
        self.uid = ''
        self.node_ID = ''
        self.node = ''

        self.contents = ''
        self.creation_date = datetime.today()

        if not uid and not node_ID and not Node and not anew:
            warn("Define uid, node_ID or Node or create a new node")

        if Node:
            self.node = Node
            self._init_by_node()

        if node_ID:
            self.node_ID = node_ID
            self._init_by_ID()

        if uid:
            self.uid = uid
            self._init_by_uid()


    def _init_by_node(self):
        if self.node:
            self.node_ID = get_node_ID(self.node)
            self.uid = self.node.uid
            self.contents = self.node.contents
            self.creation_date = self.node.creation_date
        else:
            raise Inst_Init_Exception


    def _init_by_ID(self):
        self.node = self.DB_root.get(self.node_ID)
        self._init_by_node()


    def _init_by_uid(self):
        generator = self.DB_root.index.lookup(uid=self.uid)
        if not generator:
            raise Inst_Init_Exception
        nodes = [node for node in generator]
        if len(nodes) > 1:
            raise Inst_Init_Exception
        else:
            self.node = nodes[0]
            self._init_by_node()


    @classmethod
    def check_uid_availability(cls, new_uid):
        node_generator = cls.DB_root.index.lookup(uid=new_uid)
        if node_generator:
            return False
        return True


    def _create_new(self, uid, contents, user, restaurant):
        self.uid = uid
        self.contents = contents
        if self.check_uid_availability(self.uid):
            self.node = self.DB_root.create(uid=uid, contents=contents)
            self.node_ID = get_node_ID(self.node)
            Graph_DB.wrote_review(user.node, self.node)
            Graph_DB.was_reviewed(restaurant.node, self.node)
            return True
        else:
            print 'attempted to duplicate uid: %s' % uid
            return False


    def _update(self, contents=None, user=None, restaurant=None):
        if contents is not None:
            self.contents = contents
            self.node.contents = contents
        if user is not None:
            edge_generator = self.node.inE('wrote_review')
            for edge in edge_generator:
                Graph_DB.wrote_review.delete(edge.eid)
            Graph_DB.wrote_review(user.node, self.node)
        if restaurant is not None:
            edge_generator = self.node.inE('was_reviewed')
            for edge in edge_generator:
                Graph_DB.was_reviewed.delete(edge.eid)
            Graph_DB.was_reviewed(restaurant.node, self.node)


    def _render_for_json(self):
        return {"uid" : self.uid,
                "contents" : self.contents,
                "pictures" : self._get_pictures(),
                "Node_ID" : self.node_ID}


    def _get_picture_Nodes(self):
        picture_generator = self.node.outV("image")
        if not picture_generator:
            return None
        return [node for node in picture_generator]


    def _get_pictures(self):
        picture_Nodes = self._get_picture_Nodes()
        if picture_Nodes:
            return dict((get_node_ID(node), node.payload) for node in picture_Nodes)
        return [default_review_pic]


    def _add_picture(self, new_pic, primary):
        """
        Replaces an old profile picture by a new picture

        :param new_pic:
        """
        new_pic_Node = Graph_DB.Image.create(im_type='review', primary=primary, payload=new_pic)
        Graph_DB.image.create(self.node, new_pic_Node)


    def _delete_picture(self, pic_node_id):
         Graph_DB.image.delete(pic_node_id)