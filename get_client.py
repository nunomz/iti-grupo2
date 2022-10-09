import aiohttp
import asyncio
import requests

def listfiles():
    files = requests.get('http://0.0.0.0:5000/list_files/').text
    return files

async def main():

    chunk_size = 64*1024*1024
    dir = 'client_gets'
    print('Os ficheiros disponiveis são: '+listfiles())

    fname = input("Qual o nome do ficheiro? (sem extensao) - ")
    filedir = dir+'/'+fname+'.zip'

    async with aiohttp.ClientSession() as session:
        async with session.get('http://0.0.0.0:5000/download/'+fname) as resp:
            
            print(" Status:", resp.status)
            print(" Content-type:", resp.headers['content-type'])

            await resp.content.read(10)
            
            print(" GETTING FILE...")

            with open(filedir, 'wb') as fd:
                async for chunk in resp.content.iter_chunked(chunk_size):
                    fd.write(chunk)

            print("File saved to 'client_gets' folder!")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())