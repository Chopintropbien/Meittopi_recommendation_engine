__author__ = 'andrei'


from bulbs.model import Node, Relationship
from bulbs.property import String, Integer, Float, Bool, DateTime, Date


class CostumNode(Node):
    element_type = "CostumNode"
    ID = String(nullable=False)
    displayName = String()


class CostumLink(Relationship):
    label = "CostumLink"

# < ================================ >

class Restaurant(CostumNode):
    element_type = "Restaurant"
    UID = String()
    name = String()
    opened = Date()
    added = Date()
    operation_hours = String()# really?


class Person(CostumNode):
    element_type = "Person"
    pseudo = String()
    name = String()
    open_ID_Links = String()
    joined_on = Date()
    birthday = Date()

class Review(CostumNode):
    element_type = "Review"
    creation_date = DateTime()
    contents = String()


class Compliment(CostumNode):
    element_type = "Compliment"
    issued_on = DateTime()
    unread = Bool()


class Event(CostumNode):
    element_type = "Event"
    Name = String()
    description = String()
    personal_message = String()


class List(CostumNode):
    element_type = "List"
    name = String()
    private = String()


class Location(CostumNode):
    element_type = "Location"
    Name_of_location = String()
    Address = String()
    Coordinates = String()
    Approx_radius = Float()


class Image(CostumNode):
    element_type = "Image"
    im_type = String()         # Profile, together_picture, picture_at, picture_of
    pimary = Bool()
    payload = String()

# < ================================ >

class distance(CostumLink):
    label = "distance"
    walkable = Bool()
    bikeable = Bool()
    driveable = Bool()
    distance = Float()


class image(CostumLink):  # always described object to image
    label = "image"
    quality = Float()


class has_access_to(CostumLink):
    label = "has_access_to"
    hard = Bool()
    requires_external_auth = Bool()


class liked(CostumLink):
    label = "liked"


class complimented(CostumLink):
    label = "complimented"


class wrote_review(CostumLink):
    label = "wrote_review"


class was_reviewed(CostumLink):
    label = "was_reviewed"


class takes_place_at(CostumLink):
    label = "takes_place_at"


class located_at(CostumLink):
    label = "located_at"


class belongs_to_list(CostumLink):
    label = "belongs_to_list"


class follows(CostumLink):
    label = "follows"


class created_event(CostumLink):
    label = "created_event"


class attends_event(CostumLink):
    label = "attend_event"


class owns_list(CostumLink):
    label = "owns_list"


class in_a(CostumLink): # used for location ontologies
    label = "is_a"