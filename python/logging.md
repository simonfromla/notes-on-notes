# Logging

__Logging Levels__
CRITICAL	50 -- A serious problem, indicating that the program itself may be unable to continue running  
ERROR	40 -- Due to a more serious problem, the software has not been able to run as expected  
WARNING	30 -- A warning that something unexpected happened, or indicative of a problem in the near future. Software is still running as expected  
INFO	20 -- Confirmation that things are working as expected  
DEBUG	10 -- Detailed information, typically of interest only when diagnosing problems  

__Sample log__  
DEBUG:root:Add: 2 + 2 = 4  
(level):(logger):(message)  
"root" logger is used when a logger is not specified (OK with small programs) -- see "Specifying logger" below  


* The default logging level is WARNING. This means, when using the logging module to print logs out to the console:
```
def add(x, y):
    return x + y

num_1, num_2 = 10, 15
result = add(num_1, num_2)

logging.warning('Add: {} + {} = {}'.format(num_1, num2, result))
\# logging.warning must be used to see output
```

__Change basic configurations__
```python
import logging

logging.basicConfig(level=logging.DEBUG)
...
logging.debug('Add: {} + {} = {}'.format(num_1, num2, result))

```
will now print all logs of level minimum DEBUG to the console  


### Log Files  
Track logs on a file instead of console:  

```python
import logging

logging.basicConfig(filename="test.log", level=logging.DEBUG)
```
This will create __test.log__ with the logs  


##### Changing log format

Peruse the [log record attributes](https://docs.python.org/3/library/logging.html#logrecord-attributes) and bring in the attributes desired, colon separated

```python
logging.basicConfig(filename="test.log", level=logging.DEBUG, format='%(asctime)s:%(funcName)s:%(levelname)s:%(message)s')
```

### Specifying Loggers  
When importing modules into other modules, run the risk of mangling/sharing loggers/configurations.  
This happens because if two logging configs are set on separate modules, the imported module will run first, initializing *its* logger.  

```python
import logging

logger = logging.getLogger(__name__)

logging.basicConfig(filename="test.log", level=logging.DEBUG, format='%(asctime)s:%(funcName)s:%(levelname)s:%(message)s')
...
\# important: change from `logging` to new `logger`
logger.debug('Add: {} + {} = {}'.format(num_1, num2, result))
```
__note:__  
* loggers operate on hierarchy. Not setting configs for a new `logger` will have it fall back and use the configs of "root" logger.  However let's leave the root logger alone and apply the configs to the new logger, below.  


##### Configuring a new logger  

```python
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO) # set the logging level
formatter = logging.Formatter('%(asctime)s:%(funcName)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('program.log')
\# file handler created, next, add it to the logger

logger.addHandler(file_handler) # Now change format by adding the formatting to the *file handler* and *not the logger*
file_handler.setFormatter(formatter)
```
__note:__  
* `logger = logging.getLogger(__name__)` is convention. Will name the logger `__main__` if main, or name specified here: `logging.FileHandler('program.log')`  



### Advanced usage  
* In the case you want to keep the logger level set to DEBUG or INFO, but want to log only ERRORs to the file handler, set a level on the file handler:  
```
file_handler.setLevel(logging.ERROR)
```
This will create a log file but not log your INFO statements. Only ERRORs (if you had any `logger.error('Tried to divde by zero')` in your code.  


* To log the entire traceback:  
```python
def divide(x, y):
    """Divide Function"""
    try:
        result = x / y
    except ZeroDivisionError:
        logger.exception('Tried to divide by zero')
    else:
        return result
```
This will log the logger format with the traceback.  


* If you wanted to log the DEBUG levels *to the console* only, create a __stream handler__

```python
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter) # Can also specify the format for the stream handler. Will output to console formatted.

logger.addHandler(file_handler)
logger.addHandler(stream_handler)
```  


### Further Reading  
[Py Docs -- logging module](https://docs.python.org/3/library/logging.html#module-logging)  
[Advanced logging tutorial (video)](https://www.youtube.com/watch?v=jxmzY9soFXg)  