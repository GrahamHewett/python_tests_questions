def smallestNum(a, b):
	if a < b:
		return 'The smallest number is ' + str(a)
	return 'The smallest number is ' + str(b)
print(smallestNum(0b110, 55))

def OddOrEven(num):
	if num % 2 == 0:
		return 'even'
	return 'odd'
#hint use the modulus operator %
print(OddOrEven(0xe1b))

def equality(truthy):
	if truthy:
		return 'truthy'
	return 'falsey'
print(equality(0b110))

#falsey values are False, None, 0, '', [], (), {}
