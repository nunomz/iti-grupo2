import aiohttp
import asyncio

async def main():

    value = input("Qual o nome do ficheiro? \n")


    async with aiohttp.ClientSession() as session:
        async with session.get('http://0.0.0.0:5000/download/'+value) as get_response:

            print("Status:", get_response.status)
            print("Content-type:", get_response.headers['content-type'])

            respget = await get_response.text()
            print("Body:", respget)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())