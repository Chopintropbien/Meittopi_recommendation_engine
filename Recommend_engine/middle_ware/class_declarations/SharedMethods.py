__author__ = 'andrei'

from Image import Image
from Recommend_engine.neo4j_manager.db_dec import Graph_DB
from RootMethods import get_node_ID


# we should exteriorize the get_rel_nodes and _add_relnode to get a family of methods able to retrieve according to a normal set and then costumize
# only the filters on which we get the relations and the unpacking method.


def get_picture_nodes(self, N=-1):
    picture_pre_generator = self.node.outE("image")
    if not picture_pre_generator:
        return None
    else:
        dico ={}
        for edge in picture_pre_generator:
            dico[get_node_ID(edge.outV())] = (edge.quality, edge.inV())
        diclist = sorted(dico.iteritems(), key=lambda x: x[1][0], reverse=True)
        if N > 0 :
            return diclist[:N]
        else:
            return diclist


def get_pictures(self, N):
    picture_dict = self.get_picture_nodes(N)
    if picture_dict is None:
        return []
    else:
        return [{"uid":key, "payload":valpack[1].payload, "quality":valpack[0], "type":valpack[1].im_type} for key, valpack in picture_dict]


def add_picture(self, picture, im_type = 'None'):
    img = Image(anew = {'payload':picture, 'im_type':im_type})
    img.save()
    Graph_DB.image.create(self.node, img.node, quality=0)
    return True


def change_picture(self, new_pic, im_type = 'None'):
        """
        Replaces an old profile picture by a new picture

        :param new_pic:
        """
        old_pic_Node = self.get_picture_nodes()
        if old_pic_Node is None:
            old_pic_Node = Graph_DB.Image.create(im_type=im_type, payload=new_pic)
            Graph_DB.image.create(self.node, old_pic_Node)
            return True

        if len(old_pic_Node) > 1:
            raise Exception

        node = old_pic_Node[0][1][1]
        node.payload = new_pic
        node.save()

        return True

# Chained delete / anonimization?

pic_attrs = [get_picture_nodes, get_pictures, add_picture, change_picture]


