import unittest
from prime_function import prime_num

class PrimeTests(unittest.TestCase):
	
	def test_input_must_not_be_float(self):
		self.assertEqual(isPrime(10.5),"The number must be a whole number")
	
	def test_no_string(self):
		self.assertEqual(isPrime("a"), "Cannot allow letters")

	def test_no_list(self):
		self.assertEqual(isPrime([24]), "Cannot allow lists")
	
	def test_input_must_not_be_a_tuple(self):
		self.assertEqual(isPrime((100)),"The number must be a whole number")
	
	def test_not_big_integer(self):
		self.assertTrue(isPrime(isPrime>1000),'large numbers not allowed!!!')
	
	def test_input_must_not_be_a_boolean(self):
		self.assertEqual(isPrime(True),"The number must not be a boolean")

if __name__ == 'main':
	unittest.main()
