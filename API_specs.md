Add a restaurant to the database:
	address	:	localhost:5000user
	type	:	POST
	payload	:	{'uid':'mlop','name':'1','opening_date':2014-5-26,'operation_horus':'11-23'}
	response code	:	200 if success, 404 in case of failure
	response example	:	{''}
	response type	:	JSON


Get a full representation of a restaurant information:
	address	:	localhost:5000restaurant
	type	:	GET
	payload	:	{'uid':'mlop','uid':'4','full':'True'}
	response code	:	200 if success, 404 or 412 in case of failure
	response example	:	{'review_list': [], 'picture': [], 'added':'2014-05-26', 'followers': [], 'name': 'the mloppest mlop', 'opening_date': None, 'operation_hours': '11-23', 'pseudo': 'mlop'}
	response type	:	JSON


Add a review to the database:
	address	:	localhost:5000restaurant
	type	:	POST
	payload	:	{'user_uid':'Lauriane', 'restau_uid':'mlop', 'title':'bloppidy mlop is mloppy blop', 'contents':'boppity blop is blopppidiest bop in town'}
	response code	:	200 if success, 404 in case of failure
	response example	:	{''}
	response type	:	JSON


Add a user to the database :
	address	:	localhost:5000user
	type	:	GET
	payload	:	{'uid':'Lauriane','name':'Lauriane Mollier','birthday':'1993-8-4'}
	response code	:	200 if success, 404 or 412 in case of failure
	response example	:	{''}
	response type	:	JSON


Demand if pseudo is available:
	address	:	localhost:5000user/pseudo_available
	type	:	GET
	payload	:	{'uid':'Lauriane'}
	response code	:	200
	response example	:	{'available': true, 'pseudo': 'Lauriane'}
	response type	:	JSON


Get a minimal representation of a user information:
	address	:	localhost:5000user
	type	:	GET
	payload	:	{'uid':'Lauriane','nodeID':'1','full':'False'}
	response code	:	200 if success, 404 or 412 in case of failure
	response example	:	{joined_on': '2014-5-25', 'birthday': '1993-8-4', 'name': 'Lauriane Mollier','pseudo': 'lauriane', 'picture': [{'type': 'other_profile', 'quality': 1.0, 'uid': '8', 'payload': 'test_picture_payload-22'}]}
	response type	:	JSON


Get a minimal representation of a restaurant information:
	address	:	localhost:5000restaurant
	type	:	GET
	payload	:	{'uid':'mlop','uid':'4','full':'False'}
	response code	:	200 if success, 404 or 412 in case of failure
	response example	:	{'picture': [], 'added': '2014-05-26', 'name': 'the mloppest mlop', 'opening_date': None, 'operation_hours': '11-23', 'pseudo': 'mlop'}
	response type	:	JSON


Demand if restaurant name is available:
	address	:	localhost:5000restaurant/name_available
	type	:	GET
	payload	:	{'uid':'andrei'}
	response code	:	200
	response example	:	{'available':true, 'resto_name': 'Chez Jaime - Lausanne'}
	response type	:	JSON


Get a full representation of a user information:
	address	:	localhost:5000user
	type	:	GET
	payload	:	{'uid':'Lauriane','nodeID':'1','full':'True'}
	response code	:	200 if success, 404 or 412 in case of failure
	response example	:	{joined_on': '2014-5-25', 'birthday': '1993-8-4', 'name': 'Lauriane Mollier','pseudo': 'lauriane', 'picture': [{'type': 'other_profile', 'quality': 1.0, 'uid': '8', 'payload': 'test_picture_payload-22'}], 'review_list': [{'picture': [], 'creation_date': u'2014-05-26', 'contents': u'Mloppily mlop blopity blopopblop', 'title': u'the mloppest mlop is mloppily mlop'}], 'follows': [], 'followers': [] }
	response type	:	JSON


