def truthy_or_falsy(value):
	if value:
		return 'truthy'
	return 'falsey'
print(truthy_or_falsy(0b110))
#falsey values are False, None, 0, '', [], (), {}

def smallest_num(a, b):
	if a < b:
		return 'The smallest number is ' + str(a)
	return 'The smallest number is ' + str(b)
print(smallest_num(0b110, 55))

def odd_or_even(num):
	if num % 2 == 0:
		return 'even'
	return 'odd'
#hint use the modulus operator %
print(odd_or_even(0o71))

def check_involving_or(value):
	if "condition 1" or "condition 2":
		return 'one of these conditions is true'
	return 'both of these conditions evaluate to false'

def check_if_positive_num(value):
	if type(value) == '?number?' and value > 0:
		return ''
	elif type(value) != '?number?':
		return ''
	return ''
#hint use the modulus operator %
print(odd_or_even(0o71))