#Turn a number into a string. Mix Numbers and strings, conversions

def cast_to_string(input=False):
	return str(input)
print(cast_to_string)

def first_20_chars(text, n):
	return text[0:n:2]
	#slicing
print(first_20_chars("the beautiful letter: is lost after the colon", 20)) 

def alternate_letters(str1, str2):
	return str1 + str2
print(concatenate_strings("When two ", "become one"))

strL = "first - second - third"
def convert_string_to_list(strList):
	return strList.split(' - ')
print(convert_string_to_list(strL))

def kebab_case_to_snake_case(text):
	return '_'.join(text.split('-'))

print(kebab_case_to_snake_case("peter-piper-picked-a-peck-of-pickled-peppers"))