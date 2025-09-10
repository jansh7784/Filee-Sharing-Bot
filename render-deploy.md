# Render.com Deployment Guide

## Step 1: Prepare Your Repository
1. Push your bot code to GitHub
2. Ensure you have:
   - `main.py`
   - `requirements.txt`
   - `app.json`

## Step 2: Deploy on Render
1. Go to [Render.com](https://render.com)
2. Sign up with GitHub
3. Click "New +" → "Web Service"
4. Connect your GitHub repository
5. Configure:
   - **Name**: Your bot name
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python main.py`

## Step 3: Set Environment Variables
In Render dashboard, go to Environment tab:
```
BOT_TOKEN=your_bot_token_here
API_ID=your_api_id_here
API_HASH=your_api_hash_here
OWNER_ID=your_owner_id_here
CHANNEL_ID=your_channel_id_here
DB_URL=your_mongodb_url_here
DB_NAME=anshmusicbot
PORT=8080
```

## Step 4: Deploy
1. Click "Create Web Service"
2. Render will build and deploy automatically
3. Your bot will be live at a Render URL
4. Check logs to ensure it's running

## Step 5: Keep Bot Running
- Render free tier doesn't sleep
- 750 hours/month is usually enough
- Monitor usage in dashboard
