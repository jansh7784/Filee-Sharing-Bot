import os
import sys
import traceback

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
        value = os.environ.get(var)
        if not value or value.strip() == "":
            missing_vars.append(var)
        else:
            print(f"✅ {var}: {'*' * len(value)}")
    
    if missing_vars:
        print(f"❌ Missing required environment variables: {', '.join(missing_vars)}")
        print("Please set these variables in your Railway project settings.")
        sys.exit(1)
    
    print("✅ All required environment variables are set!")

if __name__ == "__main__":
    try:
        print("🚀 Starting Ansh Music Bot...")
        print("=" * 50)
        check_required_env_vars()
        print("=" * 50)
        
        from bot import Bot
        print("📦 Bot module imported successfully")
        
        bot = Bot()
        print("🤖 Bot instance created successfully")
        
        print("🔄 Starting bot...")
        bot.run()
        
    except Exception as e:
        print(f"❌ Error starting bot: {str(e)}")
        print("📋 Full traceback:")
        traceback.print_exc()
        sys.exit(1)
