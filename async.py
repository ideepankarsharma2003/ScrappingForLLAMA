import asyncio
import json


l= '''https://huggingface.co/spaces/mteb/leaderboard,https://huggingface.co/spaces/mteb/leaderboard,'''*500

import aiohttp
# l


async def get_similarity(url, sesion, i):
    async with sesion.get(url) as response:
            data = await response.json()
            print(f'index: {i} ', data)

async def get_similarity_home(url, sesion, i):
    async with sesion.get(url) as response:
            data = ("{'hello': 'world'}")
            print(f'index: {i} ', data)
    
async def main(l):
    url= f"http://54.193.173.165/base?text={l}"
    url1= f"http://54.193.173.165/large?text={l}"
    url2= f"http://54.193.173.165/?text={l}"
    
    
    task= []
    
    
    async with aiohttp.ClientSession() as custom:
        # async with custom.get(f"http://54.193.173.165/base?text={l}") as response:
        #     data = await response.json()
        #     print(data)
        # await get_similarity(url, custom)
        for i in range(100):
            task.append(asyncio.ensure_future(get_similarity(url, custom, str(i)+"base")))
            task.append(asyncio.ensure_future(get_similarity(url1, custom, str(i)+"large")))
            task.append(asyncio.ensure_future(get_similarity_home(url2, custom, str(i)+"home_page")))
            
        await asyncio.gather(*task)


# while True:
asyncio.run(main(l))




