# 🚀 Railway.app Deployment Guide

## Quick Start (5 Minutes!)

### Step 1: Push to GitHub
1. Create a new repository on GitHub
2. Upload all your bot files to the repository
3. Make sure these files are included:
   - `main.py` ✅
   - `bot.py` ✅
   - `config.py` ✅
   - `requirements.txt` ✅
   - `Procfile` ✅
   - `runtime.txt` ✅
   - `railway.json` ✅
   - `.railwayignore` ✅
   - All files from `plugins/` folder ✅
   - All files from `database/` folder ✅

### Step 2: Deploy on Railway
1. Go to [Railway.app](https://railway.app)
2. Sign up with your GitHub account
3. Click **"New Project"**
4. Select **"Deploy from GitHub repo"**
5. Choose your repository
6. Railway will automatically detect it's a Python app

### Step 3: Set Environment Variables
In Railway dashboard, go to your project → **Variables** tab and add:

```
BOT_TOKEN=1950074583:AAHS6Zh2fAsA-2HsIkJwF8tXGDsNUpWBH_I
API_ID=7162326
API_HASH=6fce46ac6f18aa4db3e4008716ca23e1
OWNER_ID=1991559687
CHANNEL_ID=-1003055836254
FORCE_SUB_CHANNEL=-1003006250672
DB_URL=mongodb+srv://johndarvis164_db_user:A8jXasyAYLC2YPTg@cluster0.gchctwz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
DB_NAME=anshmusicbot
PORT=8080
TG_BOT_WORKERS=4
FILE_AUTO_DELETE=1200
PROTECT_CONTENT=True
DISABLE_CHANNEL_BUTTON=True
ADMINS=1991559687 1716268996
```

### Step 4: Deploy!
1. Railway will automatically build and deploy
2. Your bot will be live at a Railway URL
3. Check the **Deployments** tab for logs
4. Your bot is now running 24/7! 🎉

## ✅ What's Optimized for Railway

- **Health Check Endpoint**: `/` and `/health` endpoints for Railway monitoring
- **Proper Logging**: Railway-friendly logging format
- **Environment Variables**: Automatic loading from Railway dashboard
- **Web Server**: Built-in web server for health checks
- **No Sleep Mode**: Runs 24/7 on Railway free tier
- **Auto Restart**: Automatic restart on failures

## 🔧 Troubleshooting

### Bot Not Starting?
1. Check the **Deployments** tab for error logs
2. Verify all environment variables are set correctly
3. Make sure your bot token is valid
4. Check if your MongoDB URL is accessible

### Environment Variables Not Loading?
1. Go to **Variables** tab in Railway dashboard
2. Make sure all variables are set (no empty values)
3. Redeploy after adding variables

### Web Server Issues?
1. The bot will still work even if web server fails
2. Check if PORT is set to 8080
3. Railway automatically assigns a port if not set

## 💰 Railway Free Tier Limits

- **$5 credit monthly** (enough for your bot)
- **No sleep mode** (always running)
- **Automatic HTTPS**
- **Custom domains available**

## 🎯 Your Bot is Ready!

Once deployed, your bot will:
- ✅ Run 24/7 without sleep
- ✅ Handle file sharing requests
- ✅ Work with your MongoDB database
- ✅ Support all your plugins
- ✅ Have health check endpoints

**Deploy now and enjoy your free 24/7 bot hosting!** 🚀
