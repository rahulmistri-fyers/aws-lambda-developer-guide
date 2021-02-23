import asyncio
from asyncio.runners import run
from asyncio.tasks import create_task
import random
from termcolor import colored
from colorama import init

async def my_coro(n):
    print(colored(f"The answer is {n}.",'blue'))

async def test():
    # print(colored('hello', 'red'), colored('world', 'green'))
    print(colored("HELLO",'red'))
    await asyncio.sleep(random.randint(1,10))
    print(colored("WORLD",'green'))

async def calc(num1,num2):
    for i in range(5):
        loop = asyncio.get_running_loop()
        x = loop.time()
        z = asyncio.all_tasks()
        print(z)
        print(f"{x:.2f} is the Loop Time")
        print(f"Addition is {i + num1}")
        print(f"Subtraction is {i - num1}")
        await asyncio.sleep(random.randint(1,2))

async def main():
    # await asyncio.gather(test(),test(),test())
    # await test()
    # await calc(5,6)
    # mytask = asyncio.create_task(my_coro(42))
    await asyncio.gather(
        test(),
        test(),
        calc(5,6),
        my_coro(42)
    )

async def f():
    f1 = asyncio.create_task(main())
    await f1

asyncio.run(f())