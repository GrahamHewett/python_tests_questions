#lists are mutable

from lists import last_in_list, extend_list, sorted, item_in_list, rm_from_list
import unittest 

class Testa1(unittest.TestCase):
	def test_last_in_list(self):
		self.assertEqual(last_in_list([-17.7, 17]), 17)

class Testa2(unittest.TestCase):
	def test_last_in_list(self):
		self.assertEqual(last_in_list([-17.7, 17]), 17)

class Testb1(unittest.TestCase):
	def test_extend_list(self):
		self.assertEqual(extend_list([-17.7, 17], [1]), 17)

class Testb1(unittest.TestCase):
	def test_extend_list(self):
		self.assertEqual(extend_list([-17.7, 17], [1]), 17)

class Testb1(unittest.TestCase):
	def test_item_in_list(self):
		self.assertEqual(item_in_list([-17.7, 17], ["present?"]), 17)

class Testb1(unittest.TestCase):
	def test_item_in_list(self):
		self.assertEqual(item_in_list([-17.7, 17], ["pre?"]), 17)

class Testb1(unittest.TestCase):
	def test_rm_from_list(self):
		self.assertEqual(rm_from_list([-17.7, 17], [-17.7, 17]), 17)

class Testb1(unittest.TestCase):
	def test_rm_from_list(self):
		self.assertEqual(rm_from_list([-17.7, 17], [-17.7, 17]), 17)

class Testb1(unittest.TestCase):
	def test_sorted(self):
		self.assertEqual(sorted([-17.7, 17]), 17)

class Testb1(unittest.TestCase):
	def test_sorted(self):
		self.assertEqual(sorted([-17.7, 17]), 17)