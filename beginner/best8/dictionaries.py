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
def get_from_dic(a_dict):
	if "oe" in a_dict:
		return a_dict["oe"]["two"]
	return "the key outer does not exist"
print(get_from_dic({"one": {"two": 2}}))

print(get_from_dic({"one": {"two": 2}}))
#Create or Update if existing
	#dict['keyName'] = value
#Update (multiple values at a time)
car = {
"brand": "Subaru",
"model": "Impreza",
"year": 2010,
"color": "red",
"age": 22
}
car.update({"color": "blue", "gold rims": True})
print(car)

def one_mans(my_dict):
	d_copy = my_dict.copy()
	for key, value in my_dict.items():
		if type(value) is int:
			del d_copy[key]
	return d_copy

print (one_mans({
	"name": "Honest Harriet",
	"treasure": 'dog',
	"secrets": 0
}))

print (one_mans({
	"name": "Sneaky Sam",
	"debts": 10,
	"treasure": 'gold',
	"secrets": 30,
}))

#dict.update({key1: value1, key2: value2,})
#Delete (multiple values at a time)
	#del dict['keyName']
	#dict.pop('keyName')
	#dict.poplast()

#Loops
	# dicti.keys()
	# dicti.values()
	# dicti.items()
	# for key in dicti:
	# for value in dicti.values:			
	# for key, value in dicti.items():