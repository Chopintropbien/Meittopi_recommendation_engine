__author__ = 'andrei'


from flask import Flask
from flask.ext.restful import Api, Resource, reqparse, abort
from Recommend_engine.middle_ware.class_declarations.HigherClasses import Person, Restaurant, Review
from Recommend_engine.middle_ware.class_declarations.RootMethods import Inst_Init_Exception
from configs import app_base_url

# add error logging

# Create get/post/delete methods in the classes and try to see if they can be exposed easily
# without re-implementing the interface again in the App part

ers = {
    'Inst_Init_Exception': {
        'message': "Instance initiation failure. Mostly caused by supplying non-existent uid/NodeID",
        'status': 409,
    },
}

app = Flask(__name__)
api = Api(app)

# Add the post and find a way to manage the error codes gracefully without the try/catch wrap

def fail_gracefully():
    abort(404, message="Required arguments were not found. please, see the API specs")

def fail_gracefully2():
    abort(410, message="Ressource doesn't exist")


get_parser = reqparse.RequestParser()
get_parser.add_argument('uid', type=str)
get_parser.add_argument('nodeID', type=str)
get_parser.add_argument('full', type=bool)


post_person_parser = reqparse.RequestParser()
post_person_parser.add_argument('uid',type=str)
post_person_parser.add_argument('name',type=str)
post_person_parser.add_argument('birthday',type=str)


post_restau_parser = reqparse.RequestParser()
post_restau_parser.add_argument('uid',type=str)
post_restau_parser.add_argument('name',type=str)
post_restau_parser.add_argument('opening_date',type=str)
post_restau_parser.add_argument('operation_hours',type=str)


post_review_parser = reqparse.RequestParser()
post_review_parser.add_argument("person_uid",type=str)
post_review_parser.add_argument("restau_uid",type=str)
post_review_parser.add_argument("title",type=str)
post_review_parser.add_argument("contents",type=str)


# picture-adding modules????
# add full_ request management?

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


class FrontPerson(Resource):

    def get(self):
        args = get_parser.parse_args()
        print args
        if args["uid"] is not None:
            try:
                person = Person(uid=args["uid"])
            except Inst_Init_Exception:
                fail_gracefully2()
        if args["nodeID"] is not None:
            try:
                person = Person(nodeID=args["nodeID"])
            except Inst_Init_Exception:
                    fail_gracefully2()
        if args["uid"] is not None or args["nodeID"] is not None:
            if args["full"]:
                return person._full_render_for_json()
            else:
                return person._render_for_json()
        else:
            fail_gracefully()


    def post(self):
        args = post_person_parser.parse_args()
        try:
            p = Person(anew=args)
            p.save()
        except Inst_Init_Exception:
            fail_gracefully2()
        return '', 200

class FrontRestaurant(Resource):

    def get(self):
        args = get_parser.parse_args()
        print args
        if args["uid"] is not None:
            try:
                restau = Restaurant(uid=args["uid"])
            except Inst_Init_Exception:
                fail_gracefully2()
        if args["nodeID"] is not None:
            try:
                restau = Restaurant(nodeID=args["nodeID"])
            except Inst_Init_Exception:
                    fail_gracefully2()
        if args["uid"] is not None or args["nodeID"] is not None:
            if args["full"]:
                return restau._full_render_for_json()
            else:
                return restau._render_for_json()
        else:
            fail_gracefully()


    def post(self):
        args = post_restau_parser.parse_args()
        try:
            p = Restaurant(anew=args)
            p.save()
        except Inst_Init_Exception:
            fail_gracefully2()
        return '', 200


class FrontReview(Resource):

    def get(self):
        args = get_parser.parse_args()
        print args
        if args["uid"] is not None:
            try:
                review = Review(uid=args["uid"])
            except Inst_Init_Exception:
                fail_gracefully2()
        if args["nodeID"] is not None:
            try:
                review = Review(nodeID=args["nodeID"])
            except Inst_Init_Exception:
                    fail_gracefully2()
        if args["uid"] is not None or args["nodeID"] is not None:
            if args["full"]:
                return review._full_render_for_json()
            else:
                return review._render_for_json()
        else:
            fail_gracefully()


    def post(self):
        args = post_review_parser.parse_args()
        if not None in args.values():
            try:
                p = Person(uid=args["person_uid"])
                p._add_review({"title":args["title"],"contents":args["contents"]},args["restaurant_uid"])

            except Inst_Init_Exception:
                fail_gracefully2()
            return '', 200
        else:
            fail_gracefully()


api.add_resource(HelloWorld, '/')
api.add_resource(FrontPerson, '/person')
api.add_resource(FrontRestaurant, '/restaurant')
api.add_resource(FrontReview, '/review')


if __name__ == '__main__':
    app.run(debug=True)