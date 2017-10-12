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


### unittest.mock to test user input and program output



