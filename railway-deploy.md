# Railway.app Deployment Guide

## Step 1: Prepare Your Repository
1. Push your bot code to GitHub
2. Make sure you have all required files:
   - `main.py` (your bot's main file)
   - `requirements.txt` (already exists)
   - `app.json` (already exists)

## Step 2: Deploy on Railway
1. Go to [Railway.app](https://railway.app)
2. Sign up with GitHub
3. Click "New Project"
4. Select "Deploy from GitHub repo"
5. Choose your repository
6. Railway will automatically detect it's a Python app

## Step 3: Set Environment Variables
In Railway dashboard, go to Variables tab and add:
```
BOT_TOKEN=your_bot_token_here
API_ID=your_api_id_here
API_HASH=your_api_hash_here
OWNER_ID=your_owner_id_here
CHANNEL_ID=your_channel_id_here
DB_URL=your_mongodb_url_here
DB_NAME=anshmusicbot
```

## Step 4: Deploy
1. Railway will automatically build and deploy
2. Your bot will be live at a Railway URL
3. Check logs to ensure it's running properly

## Step 5: Keep Bot Running
- Railway doesn't have sleep mode on free tier
- Your bot will run 24/7 automatically
- Monitor usage in Railway dashboard
