def run(coroutine):
    try:
        coroutine.send(None)
    except StopIteration as e:
        return e.value

async def fib(n):
    if n < 2:
        return 1
    else:
        return await fib(n-1) + await fib(n-2)

async def main():
    for n in range(8):
        print(await fib(n))

run(main())