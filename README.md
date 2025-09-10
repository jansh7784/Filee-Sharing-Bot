# 🎵 Ansh Music Bot

A powerful Telegram bot for secure music file sharing with advanced features like content protection, force subscription, and auto-deletion.

## ✨ Features

- 🔒 **Content Protection** - Prevents forwarding and saving
- 👥 **Force Subscription** - Users must join your channel
- ⏰ **Auto-Deletion** - Files delete after 20 minutes
- 📊 **Admin Panel** - Beautiful UI with statistics
- 🔗 **Link Generation** - Single and batch file links
- 📢 **Broadcast System** - Send messages to all users
- 🗄️ **MongoDB Integration** - User tracking and management

## 🚀 Quick Deploy

### Deploy to Railway (Recommended)

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/your-template-id)

1. Click the deploy button above
2. Set up your environment variables
3. Deploy!

### Deploy to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/jansh7784/ansh-music-bot)

## ⚙️ Environment Variables

| Variable | Description | Required | Example |
|----------|-------------|----------|---------|
| `BOT_TOKEN` | Your bot token from @BotFather | ✅ | `1234567890:ABC...` |
| `API_ID` | Your API ID from my.telegram.org | ✅ | `1234567` |
| `API_HASH` | Your API Hash from my.telegram.org | ✅ | `abcdef123456...` |
| `OWNER_ID` | Your Telegram user ID | ✅ | `123456789` |
| `CHANNEL_ID` | Storage channel ID (where files are stored) | ✅ | `-1001234567890` |
| `FORCE_SUB_CHANNEL` | Channel ID for force subscription | ✅ | `-1001234567890` |
| `DB_URL` | MongoDB connection string | ✅ | `mongodb+srv://...` |
| `DB_NAME` | Database name | ❌ | `anshmusicbot` |
| `ADMINS` | Space-separated admin user IDs | ❌ | `123456789 987654321` |
| `PROTECT_CONTENT` | Enable content protection | ❌ | `True` |
| `FILE_AUTO_DELETE` | Auto-delete time in seconds | ❌ | `1200` |
| `PORT` | Server port | ❌ | `8080` |
| `TG_BOT_WORKERS` | Number of bot workers | ❌ | `4` |

> **Note:** Copy `env.example` to `.env` and fill in your actual values for local development.

## 📋 Setup Instructions

### 1. Create Telegram Bot
1. Message [@BotFather](https://t.me/BotFather)
2. Create a new bot with `/newbot`
3. Get your bot token

### 2. Get API Credentials
1. Go to [my.telegram.org](https://my.telegram.org)
2. Create a new application
3. Get your API ID and API Hash

### 3. Create Channels
1. Create a private channel for file storage
2. Create a channel for force subscription
3. Add your bot as admin to both channels
4. Get channel IDs (use [@userinfobot](https://t.me/userinfobot))

### 4. Setup MongoDB
1. Go to [MongoDB Atlas](https://cloud.mongodb.com)
2. Create a free cluster
3. Create a database user
4. Get your connection string

### 5. Deploy
1. Fork this repository
2. Deploy to Railway/Heroku
3. Set environment variables
4. Start your bot!

## 🎯 Usage

### Admin Commands
- `/admin` - Open admin panel
- `/help` - Show help menu
- `/genlink` - Create single file link
- `/batch` - Create multiple file links
- `/users` - View user statistics
- `/broadcast` - Send message to all users
- `/stats` - View bot statistics

### How It Works
1. **Upload** - Send files to your bot
2. **Generate** - Bot creates secure links
3. **Share** - Share links with users
4. **Access** - Users must join your channel
5. **Download** - Protected access for 20 minutes
6. **Auto-Delete** - Files automatically removed

## 🔒 Security Features

- **Content Protection** - Users cannot forward or save files
- **Force Subscription** - Must join your channel to access
- **Auto-Deletion** - Files expire after 20 minutes
- **Admin Controls** - Full management capabilities

## 📊 Admin Panel

The bot includes a beautiful admin panel with:
- User statistics and growth tracking
- Broadcast system with progress tracking
- Link generation tools
- Bot performance monitoring
- Interactive navigation

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Developer

**Ansh Jain**
- GitHub: [@jansh7784](https://github.com/jansh7784)
- LinkedIn: [ansh--jain](https://linkedin.com/in/ansh--jain)

## 🙏 Acknowledgments

- [Pyrogram](https://github.com/pyrogram/pyrogram) - Telegram MTProto API
- [MongoDB](https://www.mongodb.com) - Database
- [Railway](https://railway.app) - Hosting platform

## ⚠️ Disclaimer

This bot is for educational purposes. Please respect copyright laws and only share content you have rights to distribute.

---

⭐ **Star this repository if you found it helpful!**