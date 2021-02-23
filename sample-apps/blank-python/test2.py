import asyncio

async def greet(name):
    return 'Hello ' + name

def run(coroutine):
    try:
        coroutine.send(None)
    except StopIteration as e:
        return e.value

# print(run(greet('Rahul')))
async def main():
    names = ["Rahul","rushabh","saurav"]
    for name in names:
        print(await greet(name))

run(main())