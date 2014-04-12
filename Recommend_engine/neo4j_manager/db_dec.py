__author__ = 'andrei'

from bulbs.neo4jserver import Graph as Neo4jGraph, Config
import type_dec as DDT

neo4j_url = 'http://localhost:7474'
neo4j_server_local = Config(neo4j_url+ '/db/data/')

# noinspection PyTypeChecker
class Graph(Neo4jGraph):
    '''
    The interface with the neo4j graph database
    '''

    def __init__(self, config=neo4j_server_local):
        super(Graph, self).__init__(config)

        # Objects

        self.Restaurant = self.build_proxy(DDT.Restaurant)
        self.Person = self.build_proxy(DDT.Person)
        self.Profile = self.build_proxy(DDT.Profile)
        self.Review = self.build_proxy(DDT.Review)
        self.Compliment = self.build_proxy(DDT.Compliment)
        self.Event = self.build_proxy(DDT.Event)
        self.Location = self.build_proxy(DDT.Location)
        self.Image = self.build_proxy(DDT.Image)

        # Relations

        self.distance = self.build_proxy(DDT.distance)
        self.image = self.build_proxy(DDT.image)
        self.has_access_to = self.build_proxy(DDT.has_access_to)
        self.liked = self.build_proxy(DDT.liked)
        self.complimented = self.build_proxy(DDT.complimented)
        self.wrote_review = self.build_proxy(DDT.wrote_review)
        self.was_reviewed = self.build_proxy(DDT.was_reviewed)
        self.takes_place_at = self.build_proxy(DDT.takes_place_at)
        self.located_at = self.build_proxy(DDT.located_at)
        self.belongs_to_list = self.build_proxy(DDT.belongs_to_list)
        self.follows = self.build_proxy(DDT.follows)
        self.created_event = self.build_proxy(DDT.created_event)
        self.attends_event = self.build_proxy(DDT.attends_event)
        self.owns_list = self.build_proxy(DDT.owns_list)


# create the graph
Graph_DB = Graph()