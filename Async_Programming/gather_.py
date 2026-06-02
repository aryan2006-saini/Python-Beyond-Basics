import asyncio

async def func1():
    await asyncio.sleep(3)
    print("Func-1")
    return("F1")

async def func2():
    await asyncio.sleep(3)
    print("Func-2")
    return("F2")

async def func3():
    await asyncio.sleep(3)
    print("Func-3")
    return("F3")

async def main():
    results = await asyncio.gather(
        func1(),
        func2(),
        func3()
    )
    print(results)

asyncio.run(main())