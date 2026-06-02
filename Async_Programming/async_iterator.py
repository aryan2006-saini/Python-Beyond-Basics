import asyncio

async def numbers():
    for i in range(5):
        await asyncio.sleep(1)
        yield i

async def main():
    async for n in numbers():
        print(n)

asyncio.run(main())