from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("Ansh Botz")




# Ansh Jain 
# Don't Remove Credit 🥺
# GitHub: https://github.com/jansh7784
# LinkedIn: https://linkedin.com/in/ansh--jain
# Developer @jansh7784
