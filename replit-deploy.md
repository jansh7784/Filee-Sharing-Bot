# Replit Deployment Guide (Easiest)

## Step 1: Create Replit Account
1. Go to [Replit.com](https://replit.com)
2. Sign up with GitHub
3. Click "Create Repl"

## Step 2: Set Up Project
1. Choose "Python" template
2. Name your project (e.g., "file-sharing-bot")
3. Click "Create Repl"

## Step 3: Upload Your Code
1. Delete the default `main.py`
2. Upload your bot files:
   - Copy content from your `main.py`
   - Copy content from your `config.py`
   - Copy all files from `plugins/` folder
   - Copy `database/` folder
   - Copy `requirements.txt`

## Step 4: Install Dependencies
1. In the Shell tab, run:
```bash
pip install -r requirements.txt
```

## Step 5: Set Environment Variables
1. Click the "Secrets" tab (lock icon)
2. Add these secrets:
```
BOT_TOKEN=your_bot_token_here
API_ID=your_api_id_here
API_HASH=your_api_hash_here
OWNER_ID=your_owner_id_here
CHANNEL_ID=your_channel_id_here
DB_URL=your_mongodb_url_here
DB_NAME=anshmusicbot
```

## Step 6: Run Your Bot
1. Click the "Run" button
2. Your bot will start running
3. Enable "Always On" in the settings (if available)

## Step 7: Keep Bot Active
- Use UptimeRobot to ping your bot every 5 minutes
- Or use a simple keep-alive script
