Demand if pseudo is available:
	address	:	localhost:5000/pseudo_check/<pseudo>
	type	:	GET
	response example	:	{'available': true, 'pseudo': 'andrei'}
	response type	:	JSON
	requires user logged_in	:	False

Demand if restaurant name is available:
	address	:	localhost:5000/resto_name_check/<resto_name>
	type	:	GET
	response example	:	{'available':true, 'resto_name': 'Chez Jaime - Lausanne'}
	response type	:	JSON
	requires user logged_in	:	False

