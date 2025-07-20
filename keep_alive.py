from aiohttp import web
import threading

def start_server():
    async def handler(request):
        return web.Response(text="Bot is alive!")

    app = web.Application()
    app.router.add_get("/", handler)

    web.run_app(app, port=8000)

def keep_alive():
    t = threading.Thread(target=start_server)
    t.start()
