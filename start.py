#!/usr/bin/env python3
"""
Railway-optimized startup script for Ansh Music Bot
Starts web server first for healthcheck, then bot
"""

import os
import sys
import asyncio
import logging
from aiohttp import web
from plugins.route import routes

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S'
)

logger = logging.getLogger(__name__)

async def start_web_server():
    """Start web server for healthcheck"""
    try:
        app = web.Application()
        app.add_routes(routes)
        
        port = int(os.environ.get("PORT", "8080"))
        runner = web.AppRunner(app)
        await runner.setup()
        
        site = web.TCPSite(runner, "0.0.0.0", port)
        await site.start()
        
        logger.info(f"✅ Web server started on port {port}")
        return runner
    except Exception as e:
        logger.error(f"❌ Web server failed to start: {e}")
        raise

async def start_bot():
    """Start the Telegram bot"""
    try:
        logger.info("🤖 Starting Telegram bot...")
        from bot import Bot
        
        bot = Bot()
        await bot.start()
        
        logger.info("✅ Telegram bot started successfully!")
        return bot
    except Exception as e:
        logger.error(f"❌ Telegram bot failed to start: {e}")
        raise

async def main():
    """Main startup function"""
    try:
        logger.info("🚀 Starting Ansh Music Bot (Railway Optimized)...")
        logger.info("=" * 60)
        
        # Check environment variables
        required_vars = ["BOT_TOKEN", "API_ID", "API_HASH", "OWNER_ID", "CHANNEL_ID", "FORCE_SUB_CHANNEL", "DB_URL"]
        missing_vars = [var for var in required_vars if not os.environ.get(var)]
        
        if missing_vars:
            logger.error(f"❌ Missing environment variables: {', '.join(missing_vars)}")
            sys.exit(1)
        
        logger.info("✅ Environment variables validated")
        
        # Start web server first (for healthcheck)
        logger.info("🌐 Starting web server...")
        web_runner = await start_web_server()
        
        # Start bot
        logger.info("🤖 Starting Telegram bot...")
        bot = await start_bot()
        
        logger.info("🎵 Ansh Music Bot is now running!")
        logger.info("=" * 60)
        
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
    except KeyboardInterrupt:
        logger.info("🛑 Bot stopped by user")
    except Exception as e:
        logger.error(f"❌ Fatal error: {e}")
        sys.exit(1)
