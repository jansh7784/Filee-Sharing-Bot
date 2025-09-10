#!/usr/bin/env python3
"""
Ansh Music Bot - Simple and Clean
Railway.app Optimized
"""

import os
import json
import logging

# Load environment variables from app.json for local development
def load_env_from_app_json():
    try:
        with open('app.json', 'r') as f:
            app_config = json.load(f)
            env_vars = app_config.get('env', {})
            
            for key, value_config in env_vars.items():
                if isinstance(value_config, dict) and 'value' in value_config:
                    value = value_config['value']
                    if value:  # Only set if value is not empty
                        os.environ[key] = str(value)
    except Exception as e:
        print(f"⚠️ Could not load app.json: {e}")

# Set up logging for Railway
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[logging.StreamHandler()]  # Railway-friendly logging
)

# Suppress Pyromod message
logging.getLogger("pyromod").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info("🚀 Starting Ansh Music Bot on Railway...")
    
    # Load environment variables from app.json FIRST (for local development)
    load_env_from_app_json()
    
    # Check if required variables are set
    required_vars = ["BOT_TOKEN", "API_ID", "API_HASH", "OWNER_ID", "CHANNEL_ID", "DB_URL"]
    missing_vars = [var for var in required_vars if not os.environ.get(var)]
    
    if missing_vars:
        logger.error(f"❌ Missing required environment variables: {', '.join(missing_vars)}")
        logger.error("Please set environment variables in Railway dashboard")
        exit(1)
    
    logger.info("✅ All required environment variables loaded")
    
    # Import and start bot (bot.py already handles web server)
    from bot import Bot
    Bot().run()