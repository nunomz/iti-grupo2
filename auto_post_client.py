import aiohttp
import asyncio
import aiofiles
import os, random
import requests
import concurrent.futures

async def file_sender(file_name=None):
    async with aiofiles.open(file_name, 'rb') as f:
        chunk = await f.read(64*1024*1024)
        while chunk:
            yield chunk
            chunk = await f.read(64*1024*1024) 

def tester(request):
    url = 'http://0.0.0.0:5000/'
    dir = os.path.join(os.getcwd(), 'imagens/')
    f = random.choice(os.listdir(dir))
    file = os.path.join(dir, f)
    print(file)
    #files = open(file, 'r')
    files = file_sender(file)
    response = requests.post(url, data=files)
    
    if response.status_code == requests.codes.bad:
        print('Headers: {} Response: {}'.format(response.headers, response.text))


async def main():
    
    async with aiohttp.ClientSession() as session:
        urls = ['http://0.0.0.0:5000/'] * 2
        print(urls)
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
            results = pool.map(tester, urls)
        print(results)

asyncio.run(main())