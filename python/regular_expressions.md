 # Regular Expressions

Because regex string patterns make use of special sequences/characters that include the '\\', which signifies a character in a string that must be escaped, use Raw Strings.
Designate a raw string by prefixing the string with 'r', which tells Python nothing in the string should be escaped.


Meta Char. | Description
---|---
'.'|(Dot) In default mode, match any character except a newline 
'^'|(Caret) Match the start of the string. In 'multiline' mode, also match immdiately after newline
'$'|Match the end of the string or just before the newline at the end of the string, and in MULTILINE mode also matches before a newline



### `re.sub(pattern, repl, string, count=0, flags=0)`

Return the string obtained by replacing the leftmost non-overlapping occurrences of pattern in string by the replacement repl. If the pattern isn’t found, string is returned unchanged. repl can be a string or a function; if it is a string, any backslash escapes in it are processed. That is, \n is converted to a single newline character, \r, and so forth. 


```python
>>> s = '100 NORTH BROAD ROAD'
>>> s.replace('ROAD', 'RD.')
'100 NORTH BRD. RD.'

>>> s[:-4] + s[-4:].replace('ROAD', 'RD.')
'100 NORTH BROAD RD.'

>>> import re
>>> re.sub('ROAD$', 'RD.', s)
'100 NORTH BROAD RD.'

>>> s = '100 BROAD'
>>> re.sub('ROAD$', 'RD.', s)
'100 BRD.'

>>> re.sub('\\bROAD$', 'RD.', s)
'100 BROAD'

>>> re.sub(r'\bROAD$', 'RD.', s)
'100 BROAD'

>>> s = '100 BROAD ROAD APT. 3'
>>> re.sub(r'\bROAD$', 'RD.', s)
'100 BROAD ROAD APT. 3'

>>> re.sub(r'\bROAD\b', 'RD.', s)
'100 BROAD RD. APT 3'
```  

Example summary: String methods are not always ideal.  
Initial regex use will do string replacement job, but needs to know exactly what is needed.  
Instead of instructions to find `ROAD$`--'ROAD' *only* as it occurs at the end of a string('$'),  
instruct to find all occurances of whole-word ROAD with word-**b**oundaries at its side('\b').  


### `re.search(pattern, string, flags=0)`

Scan through string looking for the first location where the regular expression pattern produces a match, and return a corresponding match object. Return None if no position in the string matches the pattern


##### Checking for Thousands in roman numerals
```python
>>> import re
>>> pattern = '^M?M?M?$'        ①
>>> re.search(pattern, 'M')     ②
<_sre.SRE_Match object at 0106FB58>
>>> re.search(pattern, 'MM')    ③
<_sre.SRE_Match object at 0106C290>
>>> re.search(pattern, 'MMM')   ④
<_sre.SRE_Match object at 0106AA38>
>>> re.search(pattern, 'MMMM')  ⑤
>>> re.search(pattern, '')      ⑥
<_sre.SRE_Match object at 0106F4A8>
```

Example summary:  
1. The pattern has 3 parts. '^' to designate the pattern must match from the very first character of the string, and '$' to match the end. Combined, they state that the pattern must match the entire string, with no other characters allowed before or after. 'M?'--optionally(0 or 1 repetitions of the preceding RE) match 'M'. Three 'M?' means match anywhere from zero to three 'M' chars in a row.     
2. `re.search()` takes a pattern(RE), and a string('M') to try to match against the RE. If found, return an object to describe the match. If not, return `None`.  
3. First two 'M's match. Third is ignored. Returns a match.  
4. All three characters match.  
5. Three match, but the pattern expects a stop. Returns `None`.  
6. Since the pattern designates optional characters, an empty string returns a positive match.  

##### Checking for Hundreds in roman numerals
```python

```

