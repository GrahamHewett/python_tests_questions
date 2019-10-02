#like js objects key value pairs
#keys can be any immutable data type, str num etc.
#CRUD
#Read 
	#dict['keyName'] 
	#but KeyError if key doesn;t exist
		#dict.get('keyName')
		#returns None if no key found
		#dict.get('keyName', 'key not found')
		#returns 'key not found' if no key found
#Create or Update if existing
	#dict['keyName'] = value
#Update (multiple values at a time)
	#dict.update({key1: value1, key2: value2,})
#Delete (multiple values at a time)
	#del dict['keyName']
	#dict.pop('keyName')

#Loops
	# dicti.keys()
	# dicti.values()
	# dicti.items()
	# for key in dicti:
	# for value in dicti.values:			
	# for key, value in dicti.items():