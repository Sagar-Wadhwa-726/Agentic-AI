import asyncio
import aiohttp # asyncio http, for making async web requests

# Can mimic an endpoint which has "n" seconds of delay in giving a response
# https://httpbin.org/delay/5

# coroutine
async def fetch_url(session, url):
    async with session.get(url) as response:
        print(f"Fetched {url} with status {response.status}")

async def main():
    urls = ["https://httpbin.org/delay/2"] * 3
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        await asyncio.gather(*tasks)
    
asyncio.run(main())