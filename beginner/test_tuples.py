#tuples are immutable lists. Far fewer methods than lists. Cannot use mutator 
#methods. Both list and tuples are ordered. Sets are unorder

list1 = [1,2,3,4]
list2 = list1
#same mutable list when assigned this way.

tuple1 = (1,2,3,4)
tuple2 = tuple1

#sets are efficents for membership tests and uniques
'Hello' in list

set1.intersection(set2)
set1.difference(set2)
set1.union(set2) #much more performant than lists and tuples

#create empty sets, lists and tuples
emptylist = []
emptylist = list()

emptytuple = ()
emptytuple = tuple()

#emptyset = {} ##WRONG!##
emptyset = set()

emptydict = {}
emptydict = dict()