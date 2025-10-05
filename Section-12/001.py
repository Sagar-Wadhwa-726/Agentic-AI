# Asyncio in python

"""function can be paused - declare a corouting (special function which can be paused) and then called and resumed as needed

Await pauses the execution until the result is ready - other tasks are completed while one task which is taking time is being done.

Event loop - the engine that runs and schedule co-routines in python

"""
import asyncio

async def brew_chai():
    print("Brewing Chai . . . ")
    await asyncio.sleep(2) # non blocking - does not blocks the main thread at all, can perform some other task while this task is being completed at the background
    
    print("Chai is ready !")

asyncio.run(brew_chai())

