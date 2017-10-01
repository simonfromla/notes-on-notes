# Strings

### translate string characters

1. `str.maketrans()` to create a translation table
2. `translate()` to perform the string mapping based on translation table
    * `maketrans(x,y,z)` `x` - string character to replace, `y` - char for replacement `z` - char to be mapped to `None`  
    
```python
>>> s = '***** Have a slice of cake *****'
>>> s.translate(str.maketrans('*', '#'))
'##### Have a slice of cake #####'

>>> greeting = '##### Have a slice of cake!! #####'
>>> greeting.translate(str.maketrans('#', '-', '!'))
'----- Have a slice of cake -----'

>>> import string
>>> s = 'FIRE EXTINGUISHER'
>>> tr_table = s.maketrans(string.ascii_uppercase, string.ascii_lowercase)
>>> s.translate(tr_table)
'fire extinguisher'

>>> s = "Hel24l3o hu888man"
>>> s.translate(s.maketrans('', '', string.digits))
'Hello human'
>>> greeting.translate(greeting.maketrans('', '', string.punctuation))
' Have a slice of cake '
```

### .strip()
* Removing leading and/or trailing chars
* Only consecutive chars from start/end removed
* Whitespace chara stripped by default/nothing specified
* Chars argument is not a prefix or suffix; rather, all combinations of its values are stripped

```python
>>> s = '      Have a cake :)     '
>>> s.strip()
'Have a cake :)'
>>> s.rstrip()
'      Have a cake :)'
>>> s.lstrip()
'Have a cake :)     '

>>> s.strip(') :')
'Have a cake'

>>> s = '===== Have a great day! ====='
>>> greeting.strip('=y')
' Have a great da! '
```


### Styling


`str.center(width[, fillchar])`
String of length `width`, padding of `fillchar`
```python
>>> ' Hello Weirdos '.center(40, '*')
'************ Hello World *************'
```

##### Case change, case check
```python
>>> s = 'pYthOn is eAsy!'

>>> s.capitalize()
'Python is easy!'

>>> s.title()
'Python Is Easy!'

>>> s.lower()
'python is easy!'

>>> s.upper()
'PYTHON IS EASY!'

>>> s.swapcase()
'PyTHoN IS EaSY!'

>>> 'is'.islower()
True

>>> 'easy'.isupper()
False
```

##### Check numeric
```python
>>> '125'.isnumeric()
True
>>> 'abc123'.isnumeric()
False
>>> '3.14'.isnumeric()
False
```

##### Checking if char `in` string
```python
>>> sentence = 'Python is easy!'
>>> 'is' in sentence
True
>>> 'python' in sentence
False
>>> 'Python' in sentence
True
>>> 'python' in sentence.lower()
True
>>> 'is easy' in sentence
True
>>> 'Javascript' not in sentence
True
```

##### Return number of non-overlapping occurrences of substring sub in the range [start, end]
`str.count(sub[, start[, end]])`
```
>>> s = 'Python on the table'
>>> s.count('on')
2

>>> s.count('r')
0

>>> s = 'dollar'
>>> s.count('oll')
1
```

##### Checking prefix/suffix in string
`str.startswith(prefix[, start[, end]])`
```python
>>> s = 'Python on the table'

>>> s.startswith('Pyt')
True
>>> s.startswith('ython', 1, 6)
True

>>> sentence.endswith('ble')
True
>>> sentence.endswith('tab', 0, 17)
True
```

##### .split()
`str.split(sep=None, maxsplit=-1)`
Returns a list using `sep` as the delimiter. 
If maxsplit given, at most maxsplit splits are done (thus, list will have at most maxsplit+1 elements). 
If maxsplit not specified or -1, then no limit on splits (all possible splits given).

If sep is given, consecutive delimiters are not grouped together and are deemed to delimit empty strings (for example, '1,,2'.split(',') returns ['1', '', '2']). The sep argument may consist of multiple characters (for example, '1<>2<>3'.split('<>') returns ['1', '2', '3']). Splitting an empty string with a specified separator returns [''].

```python
>>> s = 'This is a sample string'
>>> s.split()
['This', 'is', 'a', 'sample', 'string']

>>> '1,,2'.split(',')
['1', '', '2']

>>> "oranges:5".split(':') 
['oranges', '5']

>>> "1<>2<>3".split('<>')
['1', '2', '3']

>>> '1 2 3'.split(maxsplit=1)
['1', '2 3']

>>> s = '{1.0 2.0 3.0}'
>>> nums = [float(s) for s in line.strip('{}').split()]
>>> nums
[1.0, 2.0, 3.0]
```

##### Return a list of the lines in the string, breaking at line boundaries
`nums = [float(s) for s in line.strip('{}').split()]`
```python
>>> 'ab c\n\nde fg\rkl\r\n'.splitlines()
['ab c', '', 'de fg', 'kl']
>>> 'ab c\n\nde fg\rkl\r\n'.splitlines(keepends=True)
['ab c\n', '\n', 'de fg\r', 'kl\r\n']
```

##### Return a string which is the concatenation of the strings in iterable.
`str.join(iterable)`

```python
>>> strings
['This', 'is', 'not', 'a', 'string', 'list']

>>> ' '.join(strings)
'This is not a string list'

>>> '-'.join(str_list)
'This-is-not-a-string-list'

>>> c = ' :: '
>>> c.join(strings)
'This :: is :: not :: a :: string :: list'
```

##### Replace chars
`str.replace(old, new[, count])`
option `count` replaces only first `count` occurances of str
```python
>>> s = "two be or not two be"
>>> s.replace("two", "to", 1)
'to be or not two be'
```  

##### Further Reading
[Python Docs. - String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)  

