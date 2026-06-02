import asyncio

async def func1():
    await asyncio.sleep(3)
    print("Func-1")

async def func2():
    await asyncio.sleep(3)
    print("Func-2")

async def func3():
    await asyncio.sleep(3)
    print("Func-3")

async def main():
    await asyncio.gather(
        func1(),
        func2(),
        func3()
    )

asyncio.run(main())