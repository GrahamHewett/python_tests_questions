#Turn a number into a string. Mix Numbers and strings, conversions

def cast_to_string(input=False): #casting
	return str(input)
print(cast_to_string)

def first_n_chars(text, n): #slicing
	return text[0:n:2]
print(first_n_chars("the beautiful letter: is lost after the colon", 20)) 

def selected_letters(text, n, step):
	return text[0:n:step]
print(selected_letters("When two ", "become one"))

strL = "first - second - third"
def convert_string_to_list(strList):
	return strList.split(' - ')
print(convert_string_to_list(strL))

def kebab_case_to_snake_case(text):
	return '_'.join(text.split('-'))

print(kebab_case_to_snake_case("peter-piper-picked-a-peck-of-pickled-peppers"))