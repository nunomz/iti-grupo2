import aiohttp
import json
import requests
from concurrent.futures import ThreadPoolExecutor
import asyncio
import random

chunk_size = 64*1024*1024
dir = 'client_gets'

def event(fname, url):
    loop = asyncio.new_event_loop()
    loop.run_until_complete(do_get(fname, url))

def listfiles():
    files = requests.get('http://0.0.0.0:5000/list_files/').text
    return files

async def do_get(fname, url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url+fname) as resp:

            filedir = dir+'/'+fname+'.zip'
            
            print(" Status:", resp.status)
            print(" Content-type:", resp.headers['content-type'])

            resp.content.read(10)
            
            print(" GETTING FILE...")

            with open(filedir, 'wb') as fd:
                for chunk in resp.content.iter_chunked(chunk_size):
                    fd.write(chunk)

            print("File saved to 'client_gets' folder!")


ficheiros = listfiles()
print(ficheiros)
# change the JSON string into a JSON object
jsonObject = json.loads(ficheiros)

num = input('Quantos pedidos em simultâneo? ')
num = int(num)

with ThreadPoolExecutor(max_workers=num) as pool:
    
    url='http://0.0.0.0:5000/download/'

    
    print(" Downloading " + str(num) + " random files: ")

    for i in range(num):
        value = jsonObject[i]
        pool.submit(event,value, url)