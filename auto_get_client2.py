import aiohttp
import requests
from concurrent.futures import ThreadPoolExecutor
import asyncio
import random

async def main(fname, url):

    chunk_size = 64*1024*1024
    dir = 'client_gets'
    
    def get_files():
        url_files = 'http://0.0.0.0:5000/files/'
        return requests.get(url_files)

    async with aiohttp.ClientSession() as session:
        ficheiros = get_files()
        print(ficheiros)
        
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

def event(fname, url):
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main(fname, url))

with ThreadPoolExecutor(max_workers=10) as pool:
    
    url='http://0.0.0.0:5000/downlaod/'
    num = input('Quantos pedidos em simultâneo? ')
    num = int(num)
    #block comment: shift+alt+a
    #cut triple quotes and paste them where desired
    #change max workers too
    print(" Downloading " + str(num) + " random files: ")
    for i in range(num):
            filenum = random.randrange(90000, 90009)
            filenum = str(filenum)
            pool.submit(event,"0"+filenum, url)
    