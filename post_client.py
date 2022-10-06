import aiohttp
import asyncio
import aiofiles

async def file_sender(file_name=None):

    async with aiofiles.open(file_name, 'r') as f:
        chunk = await f.read(64*1024*1024)
        while chunk:
            yield chunk
            chunk = await f.read(64*1024*1024) 
    #return chunk

async def main():
    
    print('Intoduza o nome da imagem que deseja enviar: ')
    
    file_name = input()

    async with aiohttp.ClientSession() as session:
        url = 'http://0.0.0.0:5000/'
        files = {'file': open(file_name, 'rb')}

        await session.post(url, data=files)

        #ficheiro = file_sender(file_name)
        #async with session.post('http://0.0.0.0:5000/', data = ficheiro) as resp:
        #    print(resp.status)
        #    print(await resp.text())
        #with open(file_name, 'rb') as f:
        #    await session.post('http://0.0.0.0:5000?Key=file', data=f)
         

asyncio.run(main())