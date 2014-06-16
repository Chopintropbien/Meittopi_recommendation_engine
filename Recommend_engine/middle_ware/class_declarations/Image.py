__author__ = 'andrei'

from Recommend_engine.neo4j_manager.db_dec import Graph_DB
from RootMethods import attr_map


class Image(object):
    DB_root = Graph_DB.Image

for methd in attr_map.iteritems():
    setattr(Image, methd[0], methd[1])