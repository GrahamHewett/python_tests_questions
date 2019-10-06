def last_in_list(a_list):
	return a_list[-1]

def extend_list(list, items):
	list.extend(items)
#def combine_2_iterables(list, iterable1): 
#	list.extend(iterable1)

def item_in_list(a_list, item):
	return 'present?' in a_list 
	# list.index('present?')

def rm_from_list(a_list, list2):
	to_rm = a_list[-1]
	if to_rm in list2:
		return list2.remove(to_rm)
	return list2

def sorted(a_list):
	dedupe = [set(a_list)]
	dedupe.sort(reverse = True)
	return dedupe

#########################
# def howManyInList(list):
# 	return len(list)

# def selectionSlice(list):
# 	return list[2:5]

# def append(list):
# 	list.append('addtoEnd') #item added on the end

# def insert(list):
# 	list.insert('addtoStart')

# def removeValues(list):
# 	#courses.pop() lastItem removed
# 		#courses.remove() names item removed

# def reverse(list):
# 	return list.reverse()

# def sort(list):
# 	return list.sort() #sort alphabetically or ascending
# 	sortedList = sorted(list) #doesn't modify original

# def sortDescending(list):
# 	return list.sort(reverse=true) #sort z-a or descending

# #tuples are immutable lists. Far fewer methods than lists. Cannot use mutator 
# #methods. Both list and tuples are ordered. Sets are unorder

# list1 = [1,2,3,4]
# list2 = list1
# #same mutable list when assigned this way.

# tuple1 = (1,2,3,4)
# tuple2 = tuple1

# #sets are efficents for membership tests and uniques
# 'Hello' in list

# set1.intersection(set2)
# set1.difference(set2)
# set1.union(set2) #much more performant than lists and tuples

# #create empty sets, lists and tuples
# emptylist = []
# emptylist = list()

# emptytuple = ()
# emptytuple = tuple()

# #emptyset = {} ##WRONG!##
# emptyset = set()

# emptydict = {}
# emptydict = dict()