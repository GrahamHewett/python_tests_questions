#Turn a number into a string. Mix Numbers and strings.
from str2 import cast_to_string
from str2 import first_20_chars
from str2 import concatenate_strings
from str2 import convert_string_to_list
from str2 import kebab_case_to_snake_case

# class TestUM(unittest.TestCase):
#     def test_(self):
# 	self.assertEqual
def test_cast_to_string():
	assert cast_to_string(False) == "False"
	assert cast_to_string(0b111) == "7"

def test_first_n_chars():
	text = "The 1st 20 chars end| before the pipe"
	n = 20
	assert first_20_chars(text, n) == "The 1st 20 chars end"

# class TestUM(unittest.TestCase):
# 	def test_first_n_chars(self):
# 		text = "The 1st 20 chars end| before the pipe"
# 		self.assertEqual(first_20_chars(text, n), "The 1st 20 chars end")

	class TestUM(unittest.TestCase):
		def test_alternate_letters(self):
		text = ""
		self.assertEqual(first_20_chars(text, n), "The 1st 20 chars end")

def test_convert_string_to_list():
	sentence = "first - second - third" 
	assert convert_string_to_list(sentence) == ['first','second','third']

def test_kebab_case_to_snake_case():
	text = "peter-piper-picked-a-peck-of-pickled-peppers"
	assert kebab_case_to_snake_case(text) == "peter_piper_picked_a_peck_of_pickled_peppers"