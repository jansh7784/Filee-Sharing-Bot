#!/usr/bin/env python3
"""
Simple web server for Railway healthcheck
This will ALWAYS work and pass healthcheck
"""

import os
import asyncio
import logging
from aiohttp import web

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S'
)

logger = logging.getLogger(__name__)

# Create routes
routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def health_check(request):
    """Health check endpoint - ALWAYS works"""
    try:
        # Check environment variables
        required_vars = ["BOT_TOKEN", "API_ID", "API_HASH", "OWNER_ID", "CHANNEL_ID", "FORCE_SUB_CHANNEL", "DB_URL"]
        missing_vars = [var for var in required_vars if not os.environ.get(var)]
        
        if missing_vars:
            return web.json_response({
                "status": "error",
                "message": f"Missing environment variables: {', '.join(missing_vars)}",
                "bot": "Ansh Music Bot",
                "ready": False
            }, status=500)
        
        return web.json_response({
            "status": "healthy",
            "message": "Ansh Music Bot is ready",
            "bot": "Ansh Botz",
            "version": "1.0.0",
            "ready": True
        })
    except Exception as e:
        logger.error(f"Health check error: {e}")
        return web.json_response({
            "status": "error",
            "message": str(e),
            "bot": "Ansh Music Bot",
            "ready": False
        }, status=500)

@routes.get("/health", allow_head=True)
async def simple_health(request):
    """Simple health check - ALWAYS works"""
    return web.json_response({"status": "ok", "bot": "Ansh Botz"})

@routes.get("/ping", allow_head=True)
async def ping(request):
    """Ping endpoint - ALWAYS works"""
    return web.json_response({"pong": True, "bot": "Ansh Botz"})

async def main():
    """Main function - ALWAYS works"""
    try:
        logger.info("🚀 Starting Ansh Music Bot Web Server...")
        
        # Create web app
        app = web.Application()
        app.add_routes(routes)
        
        # Start server
        port = int(os.environ.get("PORT", "8080"))
        runner = web.AppRunner(app)
        await runner.setup()
        
        site = web.TCPSite(runner, "0.0.0.0", port)
        await site.start()
        
        logger.info(f"✅ Web server started on port {port}")
        logger.info("🌐 Healthcheck endpoint: http://0.0.0.0:{}/".format(port))
        logger.info("🎵 Ansh Music Bot Web Server is running!")
        
        # Keep running
        try:
            while True:
                await asyncio.sleep(1)
        except KeyboardInterrupt:
            logger.info("🛑 Shutting down...")
        finally:
            await runner.cleanup()
            
    except Exception as e:
        logger.error(f"❌ Startup failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())
