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
	response example : {'review_list': [], 
				'picture': [],
				'added':'2014-05-26',
				'followers': [],
				'name': 'the mloppest mlop',
				'opening_date': None,
				'operation_hours': '11-23',
				'pseudo': 'mlop'}
				
	response type	:	JSON
	
	- est ce que dans added tu peux aussi metre les heures et les minutes? 
	- j'aimerais que tu me refournisse l'uid du restau
	- c'est quoi la liste des folowers? c'est les personnes qui aime? 
	- le prix du restau
	- le nombre d'avis qu'il a recu
	- la liste des cathegorie auquel il appartient
	- (pour plus tart) la liste des evenement qu'il prospose
	- qu'est ce qu'il y a dans revu list? que les revues? peut etre que c'est ecrit plus bas je verrais

Add a review to the database:
	address	:	localhost:5000restaurant
	type	:	POST
	payload	:	{'user_uid':'Lauriane', 
			'restau_uid':'mlop',
			'title':'bloppidy mlop is mloppy blop',
			'contents':'boppity blop is blopppidiest bop in town'}
	response code	:	200 if success, 404 in case of failure
	response example	:	{''}
	response type	:	JSON
	
	- il faudra bien que tu enregistre l'haure à la quel il a  été poster
	- il faut que je te passe la note qu'il a mis


Add a user to the database :
	address	:	localhost:5000user
	type	:	GET
	payload	:	{'uid':'Lauriane',
			'name':'Lauriane Mollier',
			'birthday':'1993-8-4'}
	response code	:	200 if success, 404 or 412 in case of failure
	response example	:	{''}
	response type	:	JSON

	- ne n'est pas moi de te donner l'id
	- email
	- si c'est une fille ou un garcon
	- nom de passe

Demand if pseudo is available:
	address	:	localhost:5000user/pseudo_available
	type	:	GET
	payload	:	{'uid':'Lauriane'}
	response code	:	200
	response example	:	{'available': true, 'pseudo': 'Lauriane'}
	response type	:	JSON

	- pas besoin du speudo, d'il se fait avec l'adresse email. 
	- mais meme requete

Get a minimal representation of a user information:
	address	:	localhost:5000user
	type	:	GET
	payload	:	{'uid':'Lauriane',
			'nodeID':'1',
			'full':'False'}
		
	response code	:	200 if success, 404 or 412 in case of failure
	response example : {joined_on': '2014-5-25',
				'birthday': '1993-8-4',
				'name': 'Lauriane Mollier',
				'pseudo': 'lauriane',
				'picture': [{'type': 'other_profile', 'quality': 1.0, 'uid': '8', 'payload': 'test_picture_payload-22'}]}
	response type	:	JSON
	
	- pas de speudo 
	- la ville ou il habite

	

Get a minimal representation of a restaurant information:
	address	:	localhost:5000restaurant
	type	:	GET
	payload	:	{'uid':'mlop','uid':'4','full':'False'}
	response code	:	200 if success, 404 or 412 in case of failure
	response example : {'picture': [],
				'added': '2014-05-26',
				'name': 'the mloppest mlop',
				'opening_date': None, 
				'operation_hours': '11-23',
				'pseudo': 'mlop'}
	response type	:	JSON

	- ce restaurant je le cherche en fonction d'une personne donc je doit te passer le l'id de cette personne 

	- qu'une seul photo
	- pas de added
	- pourquoi un speudo? 
	- note
	- liste des cathegorie des restau
	- (pour plus tard) personne qui aime ce restau et celle qui ne les aime pas
	- prix
	- (pour plus tard) liste des evenement 


Demand if restaurant name is available:
	address	:	localhost:5000restaurant/name_available
	type	:	GET
	payload	:	{'uid':'andrei'}
	response code	:	200
	response example	:	{'available':true, 'resto_name': 'Chez Jaime - Lausanne'}
	response type	:	JSON

	- les restaurant ne peuvent pas avoir le meme nom?

Get a full representation of a user information:
	address	:	localhost:5000user
	type	:	GET
	payload	:	{'uid':'Lauriane','nodeID':'1','full':'True'}
	response code	:	200 if success, 404 or 412 in case of failure
	response example : {joined_on': '2014-5-25',
				'birthday': '1993-8-4',
				'name': 'Lauriane Mollier',
				'pseudo': 'lauriane',
				'picture': [{'type': 'other_profile', 'quality': 1.0, 'uid': '8', 'payload': 'test_picture_payload-22'}],
				'review_list': [{'picture': [],
						'creation_date': '2014-05-26',
						'contents': u'Mloppily mlop blopity blopopblop',
						'title': u'the mloppest mlop is mloppily mlop'}],
						'follows': [],
						'followers': [] }
				
	- pas de speudo
	- la ville ou il habite
				
				
				
				
				
				
				
				
				
				
	response type	:	JSON


