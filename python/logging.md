# Logging

__Logging Levels__
CRITICAL	50 -- A serious problem, indicating that the program itself may be unable to continue running
ERROR	40 -- Due to a more serious problem, the software has not been able to run as expected
WARNING	30 -- A warning that something unexpected happened, or indicative of a problem in the near future. Software is still running as expected
INFO	20 -- Confirmation that things are working as expected
DEBUG	10 -- Detailed information, typically of interest only when diagnosing problems


The default logging level is WARNING. This means, when using the logging module to print logs out to the console:
```
def add(x, y):
    return x + y

num_1, num_2 = 10, 15
result = add(num_1, num_2)

logging.warning('Add: {} + {} = {}'.format(num_1, num2, result))

```

```python
import logging

logging.basicConfig(level=logging.DEBUG)

```