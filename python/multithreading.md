# The threading module

Using threads allows a program to run multiple operations concurrently in the same process space.
* A thread is the smallest unit of code that can be executed.
* A program that has more than one thread is multithreaded.
* A process is an executing instance of a program.
* A process as a complete set of data and variables while one or more threads may share the same data.

##### "_thread" vs. "threading" module  
The threading module constructs higher-level threading interfaces on top of the lower level \_thread module. We rarely touch the low level \_thread module.  

### Thread objects
The simplest way to use a Thread:
Instantiate it with a target function __f()__ and call __start()__ to let it begin.
The __target__ is the callable object to be invoked by the __run()__ method. Defaults to None, meaning nothing is called


```python
import threading

def f():
    print('thread function')
    return

if __name__ == '__main__':
    for i in range(3):
        t = threading.Thread(target=f)
        t.start()
```
The start() starts the thread's activity. It must be called at most once per thread object.

### Passing parameters  
To make a thread more useful, we want to pass __args__ to give more information about the work.
__args__ is the argument tuple for the target invocation. Defaults to ().

```python
import threading

def f(id):
    print('thread function {}'.format(id))
    return

if __name__ == '__main__':
    for i in range(3):
        t = threading.Thread(target=f, args=(i,))
        t.start()
```