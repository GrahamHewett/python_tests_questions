#Turn a number into a string. Mix Numbers and strings.
from str import monty_python_quote, spam, same_length, replace_text, occurences

import unittest

class TestUM(unittest.TestCase):
	def test_spam(self):
		self.assertEqual(spam("a", 2), "aa")
		self.assertEqual(spam("b", 3), "bbb")

def test_MontyPythonQuote():
	assert monty_python_quote() == "We interrupt this program to annoy you and make things generally irritating!"

def test_spam():
	assert spam("developers ", 3) == "developers developers developers developers" or "developers developers developers developers "

def test_same_length():
	assert same_length("hello ", "world") == False
	assert same_length("hello", "world") == True

def test_replace_text():
	sentence = "He's not the Messiah, he's a very cheeky boy!" 
	assert replace_text(sentence) == "He's not the Messiah, he's a very naughty boy!"

def test_occurences1():
	toungeTwister = "peter piper picked a peck of pickled peppers"
	phrase = "p"
	assert occurences(toungeTwister, phrase) == 9

def test_occurences2():
	toungeTwister = "she sells seashells by the seashore, the shells she sells are sea shells I'm sure. So if she sells sea shells on the seashore, then I'm sure she sells seashore shells"
	phrase = "she"
	assert occurences(toungeTwister, phrase) == 9