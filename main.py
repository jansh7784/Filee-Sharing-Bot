#!/usr/bin/env python3
"""
Ansh Music Bot - Railway Deployment Ready
Professional Telegram File Sharing Bot
"""

import os
import sys
import traceback
import asyncio
import logging

# Set up basic logging first
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S'
)

logger = logging.getLogger(__name__)

def check_required_env_vars():
    """Check if all required environment variables are set"""
    required_vars = {
        "BOT_TOKEN": "Your bot token from @BotFather",
        "API_ID": "Your API ID from my.telegram.org", 
        "API_HASH": "Your API Hash from my.telegram.org",
        "OWNER_ID": "Your Telegram user ID",
        "CHANNEL_ID": "Storage channel ID (where files are stored)",
        "FORCE_SUB_CHANNEL": "Channel ID for force subscription",
        "DB_URL": "MongoDB connection string"
    }
    
    missing_vars = []
    for var, description in required_vars.items():
        value = os.environ.get(var)
        if not value or value.strip() == "":
            missing_vars.append(f"{var} ({description})")
        else:
            logger.info(f"✅ {var}: {'*' * min(len(value), 10)}")
    
    if missing_vars:
        logger.error("❌ Missing required environment variables:")
        for var in missing_vars:
            logger.error(f"   - {var}")
        logger.error("Please set these variables in your Railway project settings.")
        return False
    
    logger.info("✅ All required environment variables are set!")
    return True

def validate_config():
    """Validate configuration values"""
    try:
        # Test integer conversions
        api_id = int(os.environ.get("API_ID", "0"))
        owner_id = int(os.environ.get("OWNER_ID", "0"))
        channel_id = int(os.environ.get("CHANNEL_ID", "0"))
        force_sub = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))
        
        if api_id <= 0:
            logger.error("❌ API_ID must be a positive integer")
            return False
        if owner_id <= 0:
            logger.error("❌ OWNER_ID must be a positive integer")
            return False
        if channel_id >= 0:
            logger.error("❌ CHANNEL_ID must be negative (channel ID)")
            return False
        if force_sub >= 0:
            logger.error("❌ FORCE_SUB_CHANNEL must be negative (channel ID)")
            return False
            
        logger.info("✅ Configuration validation passed!")
        return True
        
    except ValueError as e:
        logger.error(f"❌ Configuration validation failed: {e}")
        return False

async def main():
    """Main function to start the bot"""
    try:
        logger.info("🚀 Starting Ansh Music Bot...")
        logger.info("=" * 60)
        
        # Check environment variables
        if not check_required_env_vars():
            sys.exit(1)
            
        # Validate configuration
        if not validate_config():
            sys.exit(1)
            
        logger.info("=" * 60)
        
        # Import and start bot
        logger.info("📦 Importing bot module...")
        from bot import Bot
        
        logger.info("🤖 Creating bot instance...")
        bot = Bot()
        
        logger.info("🔄 Starting bot...")
        await bot.start()
        
        logger.info("✅ Bot started successfully!")
        logger.info("🎵 Ansh Music Bot is now running!")
        
        # Keep the bot running
        await bot.idle()
        
    except KeyboardInterrupt:
        logger.info("🛑 Bot stopped by user")
    except Exception as e:
        logger.error(f"❌ Fatal error: {str(e)}")
        logger.error("📋 Full traceback:")
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    try:
        # Run the bot
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("🛑 Bot stopped by user")
    except Exception as e:
        logger.error(f"❌ Startup failed: {str(e)}")
        traceback.print_exc()
        sys.exit(1)