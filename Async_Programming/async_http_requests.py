import aiohttp
import asyncio

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    html = await fetch("https://www.facebook.com")
    print(html)
    print(f"Length of html: {len(html)}")

asyncio.run(main())