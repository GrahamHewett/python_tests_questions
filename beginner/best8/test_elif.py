from if_else import odd_or_even, truthy_or_falsy, smallest_num, _and, _or

class TestUM(unittest.TestCase):
    def test_truthy_or_falsy(self):
	self.assertEqual(truthy_or_falsy(0),
	"falsy")
	self.assertEqual(truthy_or_falsy(-13),
	"truthy")
	self.assertEqual(truthy_or_falsy(0b000),
	"falsy")
	self.assertEqual(truthy_or_falsy(0x101),
	"truthy")

class TestUM(unittest.TestCase):
    def test_truthy_or_falsy(self):
	self.assertEqual(truthy_or_falsy(''),
	"Falsy")
	self.assertEqual(truthy_or_falsy("false"),
	"Truthy")
	self.assertEqual(truthy_or_falsy("""-##!"""),
	"Truthy")

class TestUM(unittest.TestCase):
    def test_truthy_or_falsy(self):
	self.assertEqual(truthy_or_falsy([1,2,3]), 
	"Truthy")
	self.assertEqual(truthy_or_falsy([]), 
	"Falsy")
	self.assertEqual(truthy_or_falsy([0, None, {}]), 
	"Truthy")

class TestUM(unittest.TestCase):
    def test_truthy_or_falsy(self):
	self.assertEqual(truthy_or_falsy({}),
	"Falsy")
	self.assertEqual(truthy_or_falsy({"isfalse": False}),
	"Truthy")

class TestUM(unittest.TestCase):
    def test_odd_or_even(self):
	self.assertEqual(odd_or_even(-5),"Odd")
	self.assertEqual(odd_or_even(22), "Even")
	self.assertEqual(odd_or_even(0), "Even")

class TestUM(unittest.TestCase):
    def test_odd_or_even(self):
	self.assertEqual(odd_or_even(-0o776),"Even")
	self.assertEqual(odd_or_even(-0b110), "Even")
	self.assertEqual(odd_or_even(0x111), "Odd")

class TestUM(unittest.TestCase):
    def test_smallest_num(self):
	self.assertEqual(smallest_num(-2, 3),
	"The smallest number is -2")
	self.assertEqual(smallest_num(15, 5),
	"The smallest number is 5")

class TestUM(unittest.TestCase):
    def test_smallest_num(self):
	self.assertEqual(smallest_num(0o765, 0x11),
	"The smallest number is 17")
	self.assertEqual(smallest_num(0b110, 55),
	"The smallest number is 6")

class TestUM(unittest.TestCase):
    def test_check_if_positive_num(self):
	self.assertEqual(check_if_positive_num(-3),
	"")
	self.assertEqual(check_if_positive_num(27), "")

# def test_truthy_or_falsy(value):
# 	assert truthy_or_falsy(0b110) == 'Truthy'
# 	

# def test_odd_or_even():
# 	a, b, c, d, e = 0, 7, -8, 100, -99
# 	assert OddOrEven(a) == 'Even'
# 	assert OddOrEven(b) == 'Odd'
# 	assert OddOrEven(c) == 'Even'	
# 	assert OddOrEven(d) == 'Even'	
# 	assert OddOrEven(e) == 'Odd'	

# def test_smallest_num():
# 	x, y = 0b1101, -900
# 	a, b = 0xef40, -0b111
# 	assert smallestNum(2, -1) == 'The smallest number is -1'
# 	assert smallestNum(2, 3) == 'The smallest number is 2'
# 	assert smallestNum(0b111, -0xef4) == 'The smallest number is -3828'
# 	assert smallestNum(0b110, 55) == 'The smallest number is 6'