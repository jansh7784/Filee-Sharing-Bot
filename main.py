import os
import sys
from bot import Bot

def check_required_env_vars():
    """Check if all required environment variables are set"""
    required_vars = [
        "BOT_TOKEN",
        "API_ID", 
        "API_HASH",
        "OWNER_ID",
        "CHANNEL_ID",
        "FORCE_SUB_CHANNEL",
        "DB_URL"
    ]
    
    missing_vars = []
    for var in required_vars:
        if not os.environ.get(var):
            missing_vars.append(var)
    
    if missing_vars:
        print(f"❌ Missing required environment variables: {', '.join(missing_vars)}")
        print("Please set these variables in your Railway project settings.")
        sys.exit(1)
    
    print("✅ All required environment variables are set!")

if __name__ == "__main__":
    print("🚀 Starting Ansh Music Bot...")
    check_required_env_vars()
    Bot().run()
