import aiohttp
import asyncio

files = {'file': open('horarios.pdf', 'rb')}

async def main():

#url = 'http://0.0.0.0:8080'
#files = {'file': open('horarios.pdf', 'rb')}

    async with aiohttp.ClientSession() as session:
        async def file_sender(file_name=None):
            async with aiofiles.open(file_name, 'rb') as f:
                chunk = await f.read(64*1024)
                while chunk:
                    yield chunk
                    chunk = await f.read(64*1024)

        async with session.get('http://0.0.0.0:8080') as get_response:

            print("Status:", get_response.status)
            print("Content-type:", get_response.headers['content-type'])

            respget = await get_response.text()
            print("Body:", respget[:15], "...")

        async with session.post('http://0.0.0.0:8080', data=files) as post_response:
            
            print("\nStatus:", post_response.status)
            print("Content-type:", post_response.headers['content-type'])

            resppost = await post_response.text()
            print("Body:", resppost[:15], "...")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

#postloop = asyncio.post_event_loop()
#postloop.run_until_complete(main())