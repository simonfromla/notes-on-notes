# The threading module

Using threads allows a program to run multiple operations concurrently in the same process space.
* A thread is the smallest unit of code that can be executed.
* A program that has more than one thread is multithreaded.
* A process is an executing instance of a program.
* A process as a complete set of data and variables while one or more threads may share the same data.

##### "_thread" vs. "threading" module  
The threading module constructs higher-level threading interfaces on top of the lower level \_thread module. We rarely touch the low level \_thread module.  

### Threading concepts
With performing multiple tasks, shared variables between the simultaneous tasks becomes an issue. 
To avoid shared variables, must use a __Lock__. Putting a lock on a var/func does not allow other tasks to access it. From the point of reference to the modification of the var, keep it locked. Then unlock after modification so that another thread can access it.  
If a thread reaches the var and it's locked, it will sit and wait(like a queue) until unlocked. 

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
The __start()__ starts the thread's activity. It must be called at most once per thread object.

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

__An Example__

```python
import threading
from queue import Queue
import time

print_lock = threading.Lock()

def exampleJob(worker):
    time.sleep(.5) # pretend to do some work.
    with print_lock:
        print(threading.current_thread().name,worker) # Once the with statement completes, the lock will automatically unlock.     
        
# The threader thread pulls an worker from the queue and processes it
def threader():
    while True:
        # gets an worker from the queue
        worker = q.get()

        # Run the example job with the avail worker in queue (thread)
        exampleJob(worker)

        # completed with the job
        q.task_done()

# Create the queue and threader 
q = Queue()

# how many threads are we going to allow for
for x in range(10):
     t = threading.Thread(target=threader)

     # classifying as a daemon, so they will die when the main dies
     t.daemon = True

     # begins, must come after daemon definition
     t.start()

start = time.time()

# 20 jobs assigned.
for worker in range(20):
    q.put(worker)

# wait until the thread terminates.
q.join()

# with 10 workers and 20 tasks, with each task being .5 seconds, then the completed job
# is ~1 second using threading. Normally 20 tasks with .5 seconds each would take 10 seconds.
print('Entire job took:',time.time() - start)

```

