import unittest
import leap_year

class testCaseLeapYear(unittest.TestCase):
	def test_4(self):
		self.assertEqual(leap_year.leap_year(4), True)

	if __name__ == '__main__':
		unittest.main()