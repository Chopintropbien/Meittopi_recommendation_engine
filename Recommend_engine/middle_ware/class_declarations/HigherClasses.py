__author__ = 'andrei'

from itertools import product
from datetime import date

from configs import default_User_Pic
from Recommend_engine.neo4j_manager.db_dec import Graph_DB
from Recommend_engine.middle_ware.class_declarations import RootMethods as CM
from Recommend_engine.middle_ware.class_declarations import SharedMethods as SM
from Recommend_engine.middle_ware.class_declarations.Image import Image

# TODO: export to the external methods specific adds of reviews / follow / attend relationships
# => Is this true this thing? We would like to route the API specs of something like /Person/<personID>/add_follow/<folloedID>
# => Nope, we are going to operate the info-gets by GETs from adress and info-posts by POSTS to the root address

# In the image module:
#    - get_full_image # currently non-implemented, we will provide interposition later on


# clear cache method? => Nope, the API takes care of it

def easy_render(node_generator, target_class):
    if node_generator:
        return [target_class(node=_node)._render_for_json() for _node in node_generator]
    else:
        return []


class Review(object):
    DB_root = Graph_DB.Review

    def _render_for_json(self, PicNum = 3):
        co_return_dict = { "picture":self.get_pictures(PicNum)}
        co_return_dict.update(self.dictify())
        return co_return_dict


    def _full_render_for_json(self, PicNum=3):
        return self._render_for_json(PicNum).update({
                            "issuer":self._get_issuer(),
                            "object":self._get_object()})

    # Combined injection from now on to avoid using Person and Restaurant before they are defined ?
    # => Ok, it works for now (not yet called)

    def _get_issuer(self):
        writergen = self.node.outV("wrote_review")
        writerlist = [writer for writer in writergen]
        if len(writerlist) != 1:
            raise Exception
        return Person(node=writerlist[0])._render_for_json()


    def _get_object(self):
        restaugen = self.node.outV("was_reviewed")
        restaulist = [writer for writer in restaugen]
        if len(restaulist) != 1:
            raise Exception
        return Restaurant(node = restaulist[0])._render_for_json()



class Person(object):
    DB_root = Graph_DB.Person

    def _render_for_json(self):
        co_return_dict = {  "pseudo":self.uid,
                            "picture":self.get_pictures(1)}
        co_return_dict.update(self.dictify())
        return co_return_dict


    def _full_render_for_json(self):
        return self._render_for_json().update({
                            "review_list":self._list_reviews(),
                            "followers":self._list_followers(),
                            "follows":self._list_follows() })

    # Not tested Yet
    def _add_review(self, payload, RestaurantUid):
        rev = Review(anew=payload)
        rev.save()
        restoNode = Restaurant(uid=RestaurantUid).node
        Graph_DB.wrote_review.create(self.node, rev.node)
        Graph_DB.was_reviewed.create(rev.node, restoNode)


    # Not tested Yet
    def _list_reviews(self):
        review_node_generator = self.node.outV("wrote_review")
        easy_render(review_node_generator, Review)

    # Not tested Yet
    def _make_follow(self, pseudo_to_follow):
        Graph_DB.follows.create(self.node, Person(uid=pseudo_to_follow).node)

    # Not tested Yet
    def _list_followers(self):
        follower_node_generator = self.node.inV("follows")
        easy_render(follower_node_generator, Person)

    # Not tested Yet
    def _list_follows(self):
        # what do we do if it follows a Restaurant?
        follows_node_generator = self.node.outV("follows")
        easy_render(follows_node_generator, Person)


    # <====== Is here for future implementation ======>

    def _get_feature_matrix(self):
        raise NotImplementedError


    def _list_recommended_restaurants(self):
        raise NotImplementedError


    def _list_Compliments_from(self):
        raise NotImplementedError

    def _list_Compliments_to(self, unread=True):
        raise NotImplementedError

    def _add_Compliment(self, compliment_body, compliment_destination_UID):
        raise NotImplementedError

    def _list_created_events(self):
        raise NotImplementedError

    def _list_attended_events(self):
        raise NotImplementedError

    def _add_to_event(self, event_UID):
        raise NotImplementedError




class Restaurant(object):
    DB_root = Graph_DB.Restaurant

    def _render_for_json(self):
        co_return_dict = {  "pseudo":self.uid,
                            "picture":self.get_pictures(1)}
        co_return_dict.update(self.dictify())
        return co_return_dict


    def _full_render_for_json(self):
        return self._render_for_json().update({
                            "review_list":self._list_reviews(),
                            "followers":self._list_followers()})


    # Not tested Yet
    def _list_reviews(self):
        review_node_generator = self.node.outV("wrote_review")
        easy_render(review_node_generator, Review)

    # To be implemented in the future: we need to redefine Persons as able to follow an existing Restaurant or Person
    def _list_followers(self):
        return []



picture_enabled = [Person, Restaurant, Review]

classlist = [Person, Restaurant, Review]


for cls, methd in product(classlist, CM.attr_map.iteritems()):
    setattr(cls, methd[0], methd[1])


for cls, methd in product(picture_enabled, SM.pic_attrs):
    setattr(cls, methd.__name__, methd)


if __name__ == "__main__":
    # p = Person(anew = {"uid":"andrei", "name":"Andrei Kucharavy", "joined_on":date(2014,05,26).isoformat(), "birthday":date(1989,4,26)})
    # p.save()

    p = Person(uid = 'andrei')

    print p.dictify()
    print p._render_for_json()
    print p.get_picture_nodes()
    p.change_picture('test_picture_payload-22', 'Profile')
    subnode = p.get_picture_nodes()[0][1][1]
    im = Image(node = subnode)
    im.change_quality(1.0)
    im.change_type("other_profile")
    print p._render_for_json()
    # p.delete_node()

    pass