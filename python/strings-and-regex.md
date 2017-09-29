# String methods

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

