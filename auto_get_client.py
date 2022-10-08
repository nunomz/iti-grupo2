import aiohttp
from concurrent.futures import ThreadPoolExecutor
import asyncio

# fname = input("Qual o nome do ficheiro? (sem extensao) - ")
# filedir = dir+'/'+fname+'.zip'

async def main(fname, url):

    chunk_size = 64*1024*1024
    dir = 'client_gets'

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

def event(fname, url):
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main(fname, url))

with ThreadPoolExecutor(max_workers=10) as pool:
    
    url='http://0.0.0.0:5000/downlaod/'

    #block comment: shift+alt+a
    #cut triple quotes and paste them where desired
    #change max workers too

    pool.submit(event,"090000", url)
    pool.submit(event,"090001", url)
    pool.submit(event,"090002", url)
    pool.submit(event,"090003", url)
    pool.submit(event,"090004", url)
    pool.submit(event,"090005", url)
    pool.submit(event,"090006", url)
    pool.submit(event,"090007", url)
    pool.submit(event,"090008", url)
    pool.submit(event,"090009", url)
