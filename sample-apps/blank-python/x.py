import asyncio
from termcolor import colored
from colorama import init

async def foo():
    await asyncio.sleep(100)
    return 42

async def bazz():
    print("z")

async def my_coro(n):
    print(colored(f"The answer is {n}.",'blue'))
    task = asyncio.gather(foo(),bazz())
    done, pending = await asyncio.wait({task})
    if task in done:
        print("Done")

asyncio.run(my_coro(5))