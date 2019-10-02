from if_else import odd_or_even
from if_else import smallest_num
# from if_else import odd_or_even
# from if_else import odd_or_even
# from if_else import odd_or_even

def test_odd_or_even():
	a, b, c, d, e = 0, 7, -8, 100, -99
	assert OddOrEven(a) == 'even'
	assert OddOrEven(b) == 'odd'
	assert OddOrEven(c) == 'even'	
	assert OddOrEven(d) == 'even'	
	assert OddOrEven(e) == 'odd'	

def test_smallest_num():
	x, y = 0b1101, -900
	a, b = 0xef40, -0b111
	assert smallestNum(2, -1) == 'The smallest number is -1'
	assert smallestNum(2, 3) == 'The smallest number is 2'
	assert smallestNum(0b111, -0xef4) == 'The smallest number is -3828'
	assert smallestNum(0b110, 55) == 'The smallest number is 6'