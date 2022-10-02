from aiohttp import web
import multidict

async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)

async def store_mp3_handler(request):
    data = await request.post() 
    mp3 = data['mp3']
    filename = mp3.filename
    mp3_file = data['mp3'].file
    content = mp3_file.read()
    return web.Response(body=content,
                        headers={'CONTENT-DISPOSITION': mp3_file})
app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/{name}', handle)])

if __name__ == '__main__':
    web.run_app(app)
