import aiohttp
import asyncio
import aiofiles
import os, random
import requests
from concurrent.futures import ThreadPoolExecutor

# async def file_sender(file_name=None):

#     async with aiofiles.open(file_name, 'r') as f:
#         chunk = await f.read(64*1024*1024)
#         while chunk:
#             yield chunk
#             chunk = await f.read(64*1024*1024) 
#     #return chunk

# form_data = (
#     "./imagens/divisao.jpg",
#     "./imagens/heart.jpg",
#     "./imagens/Schedule.png"
# )

# async def tester(request):
#     url = 'http://0.0.0.0:5000/'
#     dir = os.path.join(os.getcwd(), 'imagens/')
#     f = random.choice(os.listdir(dir))
#     file = os.path.join(dir, f)
#     #print(file)
#     files = {'file': open(file, 'rb')}
#     response = await requests.post('url', data=files)
    
#     if response.status_code == requests.codes.bad:
#         print('Headers: {} Response: {}'.format(response.headers, response.text))


def main(n, url):
    
    files = {'file': open(n, 'rb')}
    data = {'files': 'file', "filename": n}
    print(files["file"])
    return requests.post(url, files = files, data = data)
    # async with aiohttp.ClientSession() as session:
    #     with await session.post('http://0.0.0.0:5000/', data=n) as resp:
    #         print(resp.status)
    #         print(await resp.text())
        #ficheiro = file_sender(file_name)
        #async with session.post('http://0.0.0.0:5000/', data = ficheiro) as resp:
        #    print(resp.status)
        #    print(await resp.text())
        #with open(file_name, 'rb') as f:
        #    await session.post('http://0.0.0.0:5000?Key=file', data=f)
         
with ThreadPoolExecutor(max_workers=3) as pool:
    url='http://0.0.0.0:5000/upload'
    pool.submit(main,"client_files/divisao.jpg", url)
    pool.submit(main,"client_files/heart.jpg", url)
    pool.submit(main,"client_files/Schedule.png", url)