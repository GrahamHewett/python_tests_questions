#lists are mutable

def howManyInList(list):
	return len(list)

def lastInList(list):
	return list[-1]

def selectionSlice(list):
	return list[2:5]

def append(list):
	list.append('addtoEnd')

def insert(list):
	list.append('addtoStart')

def combine2Lists(list, list2): #like concat?
	list.extend(list2) #list2 added on the end

def removeValues(list):
	#courses.pop() lastItem removed

def rmLastInList1FromList2(list, list2)

def reverse(list):
	return list.reverse()

def sort(list):
	return list.sort() #sort alphabetically or ascending
	sortedList = sorted(list) #doesn't modify original

def sortDescending(list):
	return list.sort(reverse=true) #sort z-a or descending

def ValueInList(list):
	return 'present?' in list 
	# list.index('present?')