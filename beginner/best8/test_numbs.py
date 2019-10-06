#integers, floats, complex
# Awaiting for evaluation result...

from numbs import stay_positive, total, age_magic, maximus, crowd_fund
import unittest 

class TestUM(unittest.TestCase):
	def test_stay_positive(self):
		self.assertEqual(stay_positive(-17.7), 17)
		self.assertEqual(stay_positive(21.0), 21)

class t2(unittest.TestCase):
	def test_stay_positive(self):
		self.assertEqual(stay_positive(-0.3), 0)
		self.assertEqual(stay_positive(-0o241),161)

class TestUM(unittest.TestCase):
	def test_age_magic(self):
		self.assertEqual(age_magic(70), 76)
		self.assertEqual(age_magic(33), 39)

class TestUM(unittest.TestCase):
	def test_total(self):
		self.assertEqual(total([1,2,3]), 6)
		self.assertEqual(total([1,0,-9]), -8)

class TestUM(unittest.TestCase):
	def test_total(self):
		self.assertEqual(total([-30,60,40]), 70)
		self.assertEqual(total([0b111,0x12,-0o10]), 17)