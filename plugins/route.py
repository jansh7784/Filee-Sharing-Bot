from aiohttp import web
import os
import logging

logger = logging.getLogger(__name__)
routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    """Health check endpoint for Railway"""
    try:
        # Check if required environment variables are set
        required_vars = ["BOT_TOKEN", "API_ID", "API_HASH", "OWNER_ID", "CHANNEL_ID", "FORCE_SUB_CHANNEL", "DB_URL"]
        missing_vars = [var for var in required_vars if not os.environ.get(var)]
        
        if missing_vars:
            return web.json_response({
                "status": "error",
                "message": f"Missing environment variables: {', '.join(missing_vars)}",
                "bot": "Ansh Music Bot"
            }, status=500)
        
        return web.json_response({
            "status": "healthy",
            "message": "Ansh Music Bot is running",
            "bot": "Ansh Botz",
            "version": "1.0.0"
        })
    except Exception as e:
        logger.error(f"Health check error: {e}")
        return web.json_response({
            "status": "error",
            "message": str(e),
            "bot": "Ansh Music Bot"
        }, status=500)

@routes.get("/health", allow_head=True)
async def health_check(request):
    """Additional health check endpoint"""
    return web.json_response({"status": "ok", "bot": "Ansh Botz"})




# Ansh Jain 
# Don't Remove Credit 🥺
# GitHub: https://github.com/jansh7784
# LinkedIn: https://linkedin.com/in/ansh--jain
# Developer @jansh7784
