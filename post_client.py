import aiohttp
import asyncio
import aiofiles

async def file_sender(file_name=None):

    async with aiofiles.open(file_name, 'rb') as f:
        chunk = await f.read(64*1024*1024)
        while chunk:
            yield chunk
            chunk = await f.read(64*1024*1024)   

async def main():

    print('Intoduza o nome da imagem que deseja enviar: ')
    
    file_name = input("Prompt")

    async with aiohttp.ClientSession() as session:
        async with session.post('http://0.0.0.0:5000/', data = file_sender(file_name)) as resp:
            print(resp.status)
            print(await resp.text())
         

asyncio.run(main())