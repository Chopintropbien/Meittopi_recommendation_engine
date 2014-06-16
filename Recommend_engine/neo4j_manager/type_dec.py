__author__ = 'andrei'


from bulbs.model import Node, Relationship
from bulbs.property import String, Integer, Float, Bool, DateTime, Date


class CostumNode(Node):
    element_type = "CostumNode"
    uid = String(nullable=False)
    active = Bool()  # is used to store the infpormation about user/restaurant deletion. inactive are not shown, but used for computation


class CostumLink(Relationship):
    label = "CostumLink"

# < ================================ >

class Restaurant(CostumNode):
    element_type = "Restaurant"
    name = String()
    opening_date = Date()
    added = Date()
    operation_hours = String() # really?


class Person(CostumNode):
    element_type = "Person"
    name = String()
    joined_on = Date()
    birthday = Date()


class Review(CostumNode):
    element_type = "Review"
    creation_date = DateTime()
    contents = String()


class Compliment(CostumNode):
    element_type = "Compliment"
    contents = String()
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


# We don't need additional verification => We are going to make it universal method
class Image(CostumNode):
    element_type = "Image"
    payload = String()
    im_type = String()         # Profile
    # thumbnail = Bool()  # curretly off
    # pimary = Bool()


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


class attends_event(CostumLink):
    label = "attend_event"


class administrates(CostumLink):
    label = "administrates"


class in_a(CostumLink):  # used for location ontologies
    label = "is_a"

class full_image(CostumLink):  # used for storing a full-blown image from a preview
    label = "full_image"