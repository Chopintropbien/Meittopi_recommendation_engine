__author__ = 'andrei'

from Recommend_engine.neo4j_manager.db_dec import Graph_DB
from RootMethods import attr_map


# TODO: implement segregation of images into the tumbnails and full-sized images


class Image(object):
    DB_root = Graph_DB.Image

    def change_quality(self, newquality):
        node = self.node
        linkgen = node.bothE("image")
        linklist = [link for link in linkgen]
        if len(linklist) > 1:
            raise Exception
        else:
            linklist[0].quality = newquality
            linklist[0].save()
            return True

    def change_type(self, newType):
        self.node.im_type = newType
        self.node.save()

    def change_payload(self, newPayload):
        self.node.payload = newPayload
        self.node.save()

for methd in attr_map.iteritems():
    setattr(Image, methd[0], methd[1])