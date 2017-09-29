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

```python
>>> greeting = '      Have a nice day :)     '
>>> greeting.strip()
'Have a nice day :)'
>>> greeting.rstrip()
'      Have a nice day :)'
>>> greeting.lstrip()
'Have a nice day :)     '

>>> greeting.strip(') :')
'Have a nice day'

>>> greeting = '===== Have a great day!! ====='
>>> greeting.strip('=')
' Have a great day!! '
```