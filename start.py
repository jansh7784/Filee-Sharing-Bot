#!/usr/bin/env python3
"""
Railway Startup Script - BULLETPROOF
"""

import os
import sys
import asyncio
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S'
)

logger = logging.getLogger(__name__)

async def start_web_server():
    """Start web server for healthcheck"""
    try:
        from aiohttp import web
        
        app = web.Application()
        
        @app.route('/')
        async def health_check(request):
            return web.json_response({
                "status": "healthy",
                "message": "Ansh Music Bot is ready",
                "bot": "Ansh Botz",
                "version": "1.0.0"
            })
        
        @app.route('/health')
        async def simple_health(request):
            return web.json_response({"status": "ok", "bot": "Ansh Botz"})
        
        port = int(os.environ.get("PORT", "8080"))
        runner = web.AppRunner(app)
        await runner.setup()
        
        site = web.TCPSite(runner, "0.0.0.0", port)
        await site.start()
        
        logger.info(f"✅ Web server started on port {port}")
        return runner
        
    except Exception as e:
        logger.error(f"❌ Web server failed: {e}")
        raise

async def start_bot():
    """Start the Telegram bot"""
    try:
        from bot import Bot
        
        bot = Bot()
        await bot.start()
        
        logger.info("✅ Telegram bot started successfully!")
        return bot
        
    except Exception as e:
        logger.error(f"❌ Telegram bot failed: {e}")
        raise

async def main():
    """Main startup function"""
    try:
        logger.info("🚀 Starting Ansh Music Bot...")
        
        # Start web server first
        web_runner = await start_web_server()
        
        # Check environment variables
        required_vars = ["BOT_TOKEN", "API_ID", "API_HASH", "OWNER_ID", "CHANNEL_ID", "FORCE_SUB_CHANNEL", "DB_URL"]
        missing_vars = [var for var in required_vars if not os.environ.get(var)]
        
        if missing_vars:
            logger.error(f"❌ Missing environment variables: {', '.join(missing_vars)}")
            logger.info("🌐 Web server running for healthcheck")
            # Keep web server running
            while True:
                await asyncio.sleep(1)
        else:
            # Start bot
            bot = await start_bot()
            logger.info("🎵 Ansh Music Bot is now running!")
            
            # Keep running
            try:
                await bot.idle()
            except KeyboardInterrupt:
                logger.info("🛑 Shutting down...")
            finally:
                await web_runner.cleanup()
                await bot.stop()
                
    except Exception as e:
        logger.error(f"❌ Startup failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        logger.error(f"❌ Fatal error: {e}")
        sys.exit(1)
