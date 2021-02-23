import asyncio

async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')

# asyncio.run(main())

# Python 3.7+
async def x():
    await asyncio.gather(main(),main(),main())

asyncio.run(x())