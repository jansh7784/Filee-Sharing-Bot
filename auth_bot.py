#!/usr/bin/env python3
"""
Bot Authorization Script
Run this first to authorize your bot
"""

import os
import json
import asyncio
from pyrogram import Client

# Load environment variables from app.json
def load_env_from_app_json():
    try:
        with open('app.json', 'r') as f:
            app_config = json.load(f)
            env_vars = app_config.get('env', {})
            
            for key, value_config in env_vars.items():
                if isinstance(value_config, dict) and 'value' in value_config:
                    value = value_config['value']
                    if value:
                        os.environ[key] = str(value)
    except Exception as e:
        print(f"⚠️ Could not load app.json: {e}")

async def authorize_bot():
    """Authorize the bot"""
    load_env_from_app_json()
    
    api_id = int(os.environ.get("API_ID", "0"))
    api_hash = os.environ.get("API_HASH", "")
    bot_token = os.environ.get("BOT_TOKEN", "")
    
    if not all([api_id, api_hash, bot_token]):
        print("❌ Missing required credentials in app.json")
        return
    
    print("🤖 Starting bot authorization...")
    
    # Create client
    app = Client(
        "Bot",
        api_id=api_id,
        api_hash=api_hash,
        bot_token=bot_token
    )
    
    try:
        await app.start()
        me = await app.get_me()
        print(f"✅ Bot authorized successfully!")
        print(f"📱 Bot name: {me.first_name}")
        print(f"🆔 Bot username: @{me.username}")
        print(f"🆔 Bot ID: {me.id}")
        
        # Test database connection
        try:
            from database.database import user_data
            print("✅ Database connection successful!")
        except Exception as e:
            print(f"⚠️ Database connection issue: {e}")
            
    except Exception as e:
        print(f"❌ Authorization failed: {e}")
    finally:
        await app.stop()

if __name__ == "__main__":
    asyncio.run(authorize_bot())
