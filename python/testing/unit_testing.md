# unit tests

### unit testing framework

Testing conventions:

* Create a separate module beginning with name __"test\_"__  
* Import the unittest module as well as the module to be tested  
* To run the tests, __unittest__ must be run as the main module:  
`$ python -m unittest test_palindrome.py`
* To run the test module by itself, add `if name == '__main__': unittest.main()`

* Subclass unittest.TestCase 
* Group different types of tests in different functions
* Funcs named "test\_x" will be called with unittest.main()  

[List of assert methods for testing](https://docs.python.org/3/library/unittest.html#assert-methods)

```python

"""
import example_palindrome
import unittest

class TestPalindrome(unittest.TestCase):

    def test_valid(self):
        # check valid input strings
        self.assertTrue(palindrome.is_palindrome('kek'))
        self.assertTrue(palindrome.is_palindrome("Dammit, I'm mad!"))
        self.assertFalse(palindrome.is_palindrome('zzz'))
        self.assertFalse(palindrome.is_palindrome('cool'))

    # Use of context manager, `with` when testing exceptions
    def test_error(self):
        # check only the exception raised
        with self.assertRaises(ValueError):
            palindrome.is_palindrome('abc123')

        with self.assertRaises(TypeError):
            palindrome.is_palindrome(7)

        # check error message as well
        with self.assertRaises(ValueError) as cm:
            palindrome.is_palindrome('on 2 no')
        em = str(cm.exception)
        self.assertEqual(em, 'Characters other than alphabets and punctuations')

        with self.assertRaises(ValueError) as cm:
            palindrome.is_palindrome('to')
        em = str(cm.exception)
        self.assertEqual(em, 'Less than 3 alphabets')

if __name__ == '__main__':
    unittest.main()
    
```


* create a subclass of unittest.TestCase (inheritance)
* Group different check types in separate functions - function names starting with "test" are automatically called by unittest.main()
* assertTrue, assertFalse, assertRaises, assertEqual, etc. can be used depending on the test

### Setup and Teardown
Factor out repetitive code with setUp and tearDown.  
__setUp__ & __tearDown__ method: runs the method code before each test, and after each test.  
__setUpClass__ & __tearDownClass__ Class method: runs the classmethod code once before and after the individual class run. For processes too costly to do before or after every test e.g. populating an entire DB to run the tests against.  

Note: class attributes need the `self.` for reference
```python
class TestEmployee(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')
    
    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('Corey', 'Schafer', 50000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)

    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        print('test_email')
        ~~self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')~~
        ~~self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')~~

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp_2.fullname, 'Sue Smith')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Schafer')
        self.assertEqual(self.emp_2.fullname, 'Jane Smith')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Schafer/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Smith/June')
            self.assertEqual(schedule, 'Bad Response!')

if __name__ == '__main__':
    unittest.main()

```





### unittest.mock to test user input and program output



