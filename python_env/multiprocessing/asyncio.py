'''template format'''
'''asyncio is Python's standard library used to manage asynchronous, single-threaded concurrency using async and await syntax.'''

Event Loop
    │
    ├── Task 1 (Boiler Temp Check)
    │   ├── Check hardware pin
    │   ├── await I/O response  [Pause here, run Task 2]
    │   └── Resume when response arrives
    │
    ├── Task 2 (Card Reader Check)
    │   ├── Send connection ping
    │   ├── await I/O response  [Pause here, run Task 3]
    │   └── Resume when response arrives