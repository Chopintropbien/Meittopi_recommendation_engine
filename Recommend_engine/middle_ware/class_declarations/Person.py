__author__ = 'andrei'

from itertools import product

from configs import default_User_Pic
from Recommend_engine.neo4j_manager.db_dec import Graph_DB
from Recommend_engine.middle_ware.class_declarations import RootMethods as CT


# TODO: export to the external methods specific adds of reviews / follow / attend relationships
# => Is this true this thing? We would like to route the API specs of something like /Person/<personID>/add_follow/<folloedID>
# => Nope, we are going to operate the info-gets by GETs from adress and info-posts by POSTS to the root address


class Person(object):
    DB_root = Graph_DB.Person

    @classmethod
    def check_uid_availability(cls, uid):
        return CT.check_uid_availability(cls, uid)

    def _render_for_json(self):
        return {"pseudo":self.pseudo,
                "name":self.name,
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
            return picture_Node.payload
        return default_User_Pic


    def _change_picture(self, new_pic):
        """
        Replaces an old profile picture by a new picture

        :param new_pic:
        """
        old_pic_Node = self._get_picture_Node()
        if old_pic_Node is not None:
            old_pic_Node.payload = new_pic
        # TODO: this might need to be moved to a separate, "Image" module
        else:
            old_pic_Node = Graph_DB.Image.create(im_type='profile', primary='True', payload=new_pic)
            Graph_DB.image.create(self.node, old_pic_Node)


    def _delete_from_database(self):
        pass

    def _get_feature_matrix(self):
        pass

    def _list_recommended_restaurants(self):
        pass


    def _list_reviews(self):
        review_node_generator = self.node.outV("wrote_review")
        review_list = []
        for review_node in review_node_generator:
            review_list.append(review_node._render_to_json())


    def _add_review(self, review_body, Restaurant):
        pass

    def _list_Compliments_from(self):
        pass

    def _list_Compliments_to(self, unread=True):
        pass

    def _add_Compliment(self, compliment_body, compliment_destination_UID):
        pass

    def _list_created_events(self):
        pass

    def _list_attended_events(self):
        pass

    def _add_to_event(self, event_UID):
        pass

    def _list_followers(self):
        pass

    def _list_follows(self):
        pass

    def _make_follow(self, pseudo_to_follow):
        pass


classlist = [Person]


for cls, methd in product(classlist, CT.attr_map.iteritems()):
    setattr(cls,methd[0], methd[1])


if __name__ == "__main__":
    p = Person(anew = {"uid":"andrei2", "Name":"Andrei Kucharavy", "joined_on":"0", "birthday":"-25"})
    print p.save()

    # ca a avale, mais sans forcement marcher pour autant.