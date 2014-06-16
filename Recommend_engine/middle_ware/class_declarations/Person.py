__author__ = 'andrei'

from itertools import product
from datetime import date

from configs import default_User_Pic
from Recommend_engine.neo4j_manager.db_dec import Graph_DB
from Recommend_engine.middle_ware.class_declarations import RootMethods as CM
from Recommend_engine.middle_ware.class_declarations import SharedMethods as SM

# TODO: export to the external methods specific adds of reviews / follow / attend relationships
# => Is this true this thing? We would like to route the API specs of something like /Person/<personID>/add_follow/<folloedID>
# => Nope, we are going to operate the info-gets by GETs from adress and info-posts by POSTS to the root address


# Picture co-routines:
#    - get_picture_Node()  # alias for get_picture_Node(1) => not important; in fact used only for the user profile picture
#    - get_picture_Nodes(N) # common one
#    - get_picture()        # used only for the profile actually
#    - get_pictures(N)  # number of desired pictures. returns the number of pictures or => We need to dict-sort by relevance, adding also the uid and the node number
#    - add_picture(self, picture, options)

# should we inline pics? => for users, yes

# In the image module:
#    - get_full_image # currently non-implemented, we will provide interposition later on


# clear cache method? => Nope, the API takes care of it



class Person(object):
    DB_root = Graph_DB.Person

    def _render_for_json(self):
        co_return_dict = {  "pseudo":self.uid,
                            "picture":self.get_pictures(1)}
        co_return_dict.update(self.dictify())
        return co_return_dict


    def _long_render_for_json(self):
        return self._render_for_json().update({
                            "review_list":self._list_reviews(),
                            "followers":self._list_followers(),
                            "follows":self._list_follows() })


    def change_picture(self, new_pic):
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


picture_enabled = [Person]

classlist = [Person]


for cls, methd in product(classlist, CM.attr_map.iteritems()):
    setattr(cls, methd[0], methd[1])


for cls, methd in product(picture_enabled, SM.pic_attrs):
    setattr(cls, methd.__name__, methd)


if __name__ == "__main__":
    # p = Person(anew = {"uid":"andrei", "name":"Andrei Kucharavy", "joined_on":date(2014,05,26), "birthday":date(1989,4,26)})
    # p.save()

    p = Person(uid = 'andrei')
    p.add_picture('test_picture_payload', 'Profile')
    print p.dictify()
    print p._render_for_json()
    # p.delete_node()

    pass