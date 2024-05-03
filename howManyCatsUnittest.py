import unittest

from howManyCats import categorize_cats

class TestCatCategorization(unittest.TestCase):
	
	def test_many_cats(self):
		self.assertEqual(categorize_cats('4'), 'That is a lot of cats') 
		self.assertEqual(categorize_cats('5'), 'That is a lot of cats')
		self.assertEqual(categorize_cats('100'), 'That is a lot of cats') 
		
	def test_few_cats(self):
		self.assertEqual(categorize_cats('3'), 'That is not that many cats.')
		self.assertEqual(categorize_cats('2'), 'That is not that many cats.')
		self.assertEqual(categorize_cats('1'), 'That is not that many cats.')
	
	def test_no_number(self):
		self.assertEqual(categorize_cats('none'), 'You did not enter a number')
		self.assertEqual(categorize_cats('three'), 'You did not enter a number')
		
if __name__ == '__main__':
	unittest.main()
		