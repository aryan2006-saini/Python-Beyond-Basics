import asyncio

async def func1():
    await asyncio.sleep(3)
    print("Func-1")

async def main():
    task = asyncio.create_task(
        func1()
    )
    print("Working on something else.")
    await task
    
asyncio.run(main())