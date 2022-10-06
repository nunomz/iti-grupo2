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
    response = requests.post('http://0.0.0.0:5000/', files=f)
    if response.status_code == requests.codes.ok:
        print('Headers: {} Response: {}'.format(response.headers, response.text))


async def main():
    
    #print('Intoduza o nome da imagem que deseja enviar: ')
    
    #file_name = input()

    async with aiohttp.ClientSession() as session:
        urls = ['http://0.0.0.0:5000/'] * 2
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
            pool.map(tester, urls)
        
        
        #url = 'http://0.0.0.0:5000/'
        #directory= os.path.join(os.getcwd(), 'imagens/')
        
        #upload_list = []
        #for files in os.listdir(directory):
        #    with open("{folder}{name}".format(folder=directory, name=files), "rb") as data:
        #        upload_list.append(files, data.read())        
        #r = requests.post('http://0.0.0.0:5000/', files=*upload_list)

        #file_name = 'imagem'+i
        #files = {'file': open(file_name, 'rb')}
        #await session.post(url, data=files)

         

asyncio.run(main())