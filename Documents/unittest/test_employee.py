import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def test_email(self):
        emp_1 = Employee('mohame','elshankety',343)
        self.assertEqual(emp_1.email,'mohame.eldshankety@email.com')

if __name__ == '__main__':
    unittest.main()