import aiohttp
import asyncio
import aiofiles
import os, random
import requests
import concurrent.futures

async def file_sender(file_name=None):

    async with aiofiles.open(file_name, 'r') as f:
        chunk = await f.read(64*1024*1024)
        while chunk:
            yield chunk
            chunk = await f.read(64*1024*1024) 
    #return chunk

def tester(request):
    url = 'http://0.0.0.0:5000/'
    dir = os.path.join(os.getcwd(), 'imagens/')
    f = random.choice(os.listdir(dir))
    file = os.path.join(dir, f)
    #print(file)
    files = open(file, 'rb')
    response = requests.post('http://0.0.0.0:5000/', data=files, allow_redirects=True)
    
    if response.status_code == requests.codes.bad:
        print('Headers: {} Response: {}'.format(response.headers, response.text))


async def main():
    
    async with aiohttp.ClientSession() as session:
        urls = ['http://0.0.0.0:5000/'] * 2
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
            pool.map(tester, urls)

asyncio.run(main())