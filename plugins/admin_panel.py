import asyncio
from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from bot import Bot
from config import ADMINS
from database.database import full_userbase
from helper_func import get_readable_time
from datetime import datetime


@Bot.on_message(filters.command('admin') & filters.private & filters.user(ADMINS))
async def admin_panel(client: Bot, message: Message):
    help_text = """
🎵 <b>MUSIC BOT ADMIN PANEL</b> 🎵

📋 <b>Available Commands:</b>

🔗 <b>Link Generation:</b>
• <code>/genlink</code> - Create link for single file
• <code>/batch</code> - Create link for multiple files

👥 <b>User Management:</b>
• <code>/users</code> - View total users count
• <code>/broadcast</code> - Send message to all users

📊 <b>Bot Statistics:</b>
• <code>/stats</code> - View bot uptime
• <code>/id</code> - Get your user ID

📁 <b>File Management:</b>
• Send any file to bot - Auto-generate link
• Files auto-delete after 20 minutes

⚙️ <b>Bot Settings:</b>
• Force subscription: ✅ Enabled
• Content protection: ✅ Enabled  
• Auto-delete: 20 minutes
• Storage channel: Configured
• Force sub channel: Configured

🎯 <b>How to Use:</b>
1. Send file to bot → Get shareable link
2. Share link → Users must join your channel
3. Users get protected access (no forwarding)
4. Files auto-delete after 20 minutes

💡 <b>Pro Tips:</b>
• Use <code>/batch</code> for sharing multiple songs
• Use <code>/broadcast</code> to announce new content
• Check <code>/users</code> to see your audience growth

🔒 <b>Security Features:</b>
• Content protection prevents forwarding
• Force subscription grows your channel
• Auto-deletion prevents copyright issues
"""
    
    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔗 Generate Link", callback_data="genlink_help")],
        [InlineKeyboardButton("👥 View Users", callback_data="users_help")],
        [InlineKeyboardButton("📊 Bot Stats", callback_data="stats_help")],
        [InlineKeyboardButton("🔒 Close", callback_data="close")]
    ])
    
    await message.reply_text(help_text, reply_markup=reply_markup, parse_mode=ParseMode.HTML)


@Bot.on_message(filters.command('help') & filters.private & filters.user(ADMINS))
async def admin_help(client: Bot, message: Message):
    help_text = """
🎵 <b>MUSIC BOT ADMIN PANEL</b> 🎵

📋 <b>Available Commands:</b>

🔗 <b>Link Generation:</b>
• <code>/genlink</code> - Create link for single file
• <code>/batch</code> - Create link for multiple files

👥 <b>User Management:</b>
• <code>/users</code> - View total users count
• <code>/broadcast</code> - Send message to all users

📊 <b>Bot Statistics:</b>
• <code>/stats</code> - View bot uptime
• <code>/id</code> - Get your user ID

📁 <b>File Management:</b>
• Send any file to bot - Auto-generate link
• Files auto-delete after 20 minutes

⚙️ <b>Bot Settings:</b>
• Force subscription: ✅ Enabled
• Content protection: ✅ Enabled  
• Auto-delete: 20 minutes
• Storage channel: Configured
• Force sub channel: Configured

🎯 <b>How to Use:</b>
1. Send file to bot → Get shareable link
2. Share link → Users must join your channel
3. Users get protected access (no forwarding)
4. Files auto-delete after 20 minutes

💡 <b>Pro Tips:</b>
• Use <code>/batch</code> for sharing multiple songs
• Use <code>/broadcast</code> to announce new content
• Check <code>/users</code> to see your audience growth

🔒 <b>Security Features:</b>
• Content protection prevents forwarding
• Force subscription grows your channel
• Auto-deletion prevents copyright issues
"""
    
    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔗 Generate Link", callback_data="genlink_help")],
        [InlineKeyboardButton("👥 View Users", callback_data="users_help")],
        [InlineKeyboardButton("📊 Bot Stats", callback_data="stats_help")],
        [InlineKeyboardButton("🔒 Close", callback_data="close")]
    ])
    
    await message.reply_text(help_text, reply_markup=reply_markup, parse_mode=ParseMode.HTML)


# Ansh Jain 
# Don't Remove Credit 🥺
# GitHub: https://github.com/jansh7784
# LinkedIn: https://linkedin.com/in/ansh--jain
# Developer @jansh7784
