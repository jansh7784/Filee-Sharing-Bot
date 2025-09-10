# 🚀 File Sharing Bot

A powerful Telegram file sharing bot with MongoDB database support, built with Pyrogram.

## ✨ Features

- 📁 **File Storage**: Store files in private channels
- 🔗 **Link Generation**: Generate secure sharing links
- 👥 **Force Subscription**: Force users to join channels
- 🛡️ **Admin Panel**: Manage bot settings
- 📊 **Statistics**: Bot usage statistics
- 🔒 **Protected Content**: Prevent content forwarding
- ⏰ **Auto Delete**: Automatic file deletion after specified time

## 🚀 Quick Deploy on Railway

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/deploy)

### Manual Deployment Steps:

1. **Fork this repository**
2. **Go to [Railway.app](https://railway.app)**
3. **Sign up with GitHub**
4. **Click "New Project" → "Deploy from GitHub repo"**
5. **Select your forked repository**
6. **Add environment variables** (see `railway-env-vars.txt`)
7. **Deploy!** 🎉

## ⚙️ Environment Variables

Copy the variables from `railway-env-vars.txt` to Railway dashboard:

### Required Variables:
- `BOT_TOKEN` - Your bot token from @BotFather
- `API_ID` - Your API ID from my.telegram.org
- `API_HASH` - Your API Hash from my.telegram.org
- `OWNER_ID` - Your Telegram user ID
- `CHANNEL_ID` - Database channel ID (make bot admin)
- `DB_URL` - MongoDB connection string

### Optional Variables:
- `FORCE_SUB_CHANNEL` - Channel ID for force subscription
- `ADMINS` - Space-separated admin user IDs
- `FILE_AUTO_DELETE` - Auto delete time in seconds (default: 1200)
- `PROTECT_CONTENT` - Protect content from forwarding (default: True)

## 📋 Setup Instructions

### 1. Create Telegram Bot
1. Message [@BotFather](https://t.me/BotFather)
2. Create new bot with `/newbot`
3. Get your bot token

### 2. Get API Credentials
1. Go to [my.telegram.org](https://my.telegram.org)
2. Login with your phone number
3. Go to "API Development Tools"
4. Create new application
5. Get API ID and API Hash

### 3. Setup Database Channel
1. Create a private channel
2. Add your bot as admin
3. Get channel ID (use @userinfobot)

### 4. Setup MongoDB
1. Create account at [MongoDB Atlas](https://cloud.mongodb.com)
2. Create cluster
3. Get connection string
4. Replace password in connection string

## 🛠️ Local Development

```bash
# Clone repository
git clone https://github.com/jansh7784/Filee-Sharing-Bot.git
cd Filee-Sharing-Bot

# Install dependencies
pip install -r requirements.txt

# Set environment variables
cp railway-env-vars.txt .env
# Edit .env with your values

# Run bot
python main.py
```

## 📁 Project Structure

```
File-Sharing-Bot/
├── main.py                 # Main entry point
├── bot.py                  # Bot class and web server
├── config.py               # Configuration settings
├── requirements.txt        # Python dependencies
├── railway.json           # Railway configuration
├── Procfile               # Process file for Railway
├── runtime.txt            # Python version
├── plugins/               # Bot plugins
│   ├── start.py          # Start command
│   ├── link_generator.py # Link generation
│   ├── admin_panel.py    # Admin commands
│   └── ...
├── database/              # Database utilities
└── railway-env-vars.txt   # Environment variables template
```

## 🔧 Dependencies

- `pyrogram` - Telegram MTProto API client
- `TgCrypto` - Fast Telegram crypto library
- `pyromod` - Pyrogram extensions
- `pymongo` - MongoDB driver
- `aiohttp` - Async HTTP client/server
- `humanize` - Human-readable data

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Developer

**Ansh Jain**
- GitHub: [@jansh7784](https://github.com/jansh7784)
- LinkedIn: [ansh--jain](https://linkedin.com/in/ansh--jain)

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## ⭐ Support

If you found this project helpful, please give it a star! ⭐

---

**Made with ❤️ by [Ansh Jain](https://github.com/jansh7784)**
