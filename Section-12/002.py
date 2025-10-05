# Running multiple coroutines
import asyncio
import time

# wait but in a non blocking manner
async def brew(name):
    print(f"Brewing {name} . . .")
    # await asyncio.sleep(3)
    time.sleep(3)
    print(f"{name} is ready !")

async def main():
    await asyncio.gather(
        brew("Masala Chai"),
        brew("Green Chai"),
        brew("Ginger Chai")
    )

asyncio.run(main()) # non blocking calls, total wait time will be 3 seconds only overall