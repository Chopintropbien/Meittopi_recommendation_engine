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
    uid = String()
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

# this thing is in fact an onthology of locations
class Location(CostumNode):
    element_type = "Location"
    Name_of_location = String()
    Address = String()
    Coordinates = String()
    Approx_radius = Float()


# We don't need additional verification => We are going to make it universal method
class Image(CostumNode):
    element_type = "Image"
    im_type = String()         # Profile, together_picture, picture_at, picture_of
    pimary = Bool()
    payload = String()


# Used to store time and perform coputations for
# repetitive events, such as opening hours,
# repetitive events occurences and human-readable transcriptions
class Time_Object(CostumNode):
    element_type = "Time_Object"
    time_type = String()    # opening hours, time of event, time of repetitive event

# < ================================ >

class distance(CostumLink):
    label = "distance"
    distance = Float()


class image(CostumLink):  # always described object to image
    label = "image"
    quality = Float()

# What do we use this for? => Delete
class has_access_to(CostumLink):
    label = "has_access_to"
    hard = Bool()
    requires_external_auth = Bool()


# We would need to run a re-hash over this all module each time
# to check that those were not changed without the authorisation
class has_admin_rights_over(CostumLink):
    label = "has_admin_rights_over"
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

class takes_place_on(CostumLink):
    label = "takes_place_on"

class open_on(CostumLink):
    label = "open on"

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