from pyrogram import __version__
from bot import Bot
from config import OWNER_ID, ADMINS
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from database.database import full_userbase
from helper_func import get_readable_time
from datetime import datetime



@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    user_id = query.from_user.id
    
    # Check if user is admin for admin-only features
    is_admin = user_id in ADMINS
    
    if data == "about":
        await query.message.edit_text(
            text = f"<b>🤖 My Name :</b> <a href='https://t.me/FileSharingXProBot'>File Sharing Bot</a> \n<b>📝 Language :</b> <a href='https://python.org'>Python 3</a> \n<b>📚 Library :</b> <a href='https://pyrogram.org'>Pyrogram {__version__}</a> \n<b>🚀 Server :</b> <a href='https://heroku.com'>Heroku</a> \n<b>📢 Channel :</b> <a href='https://t.me/Madflix_Bots'>Madflix Botz</a> \n<b>🧑‍💻 Developer :</b> <a href='tg://user?id={OWNER_ID}'>Jishu Developer</a>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    
    elif data == "genlink_help" and is_admin:
        genlink_help = """
🔗 <b>LINK GENERATION HELP</b> 🔗

<b>Available Commands:</b>

📁 <b>Single File:</b>
• <code>/genlink</code> - Create link for one file
• Forward any file from your storage channel
• Get instant shareable link

📁 <b>Multiple Files:</b>
• <code>/batch</code> - Create link for multiple files
• Forward first file from storage channel
• Forward last file from storage channel
• Get one link for all files in between

💡 <b>Tips:</b>
• Use <code>/genlink</code> for single songs
• Use <code>/batch</code> for albums/playlists
• Links work for 20 minutes
• Content is protected from forwarding
"""
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton("🔙 Back to Help", callback_data="help_back")],
            [InlineKeyboardButton("🔒 Close", callback_data="close")]
        ])
        await query.message.edit_text(genlink_help, reply_markup=reply_markup, parse_mode=ParseMode.HTML)
    
    elif data == "users_help" and is_admin:
        users = await full_userbase()
        users_text = f"""
👥 <b>USER STATISTICS</b> 👥

📊 <b>Total Users:</b> <code>{len(users)}</code>

📈 <b>Growth Insights:</b>
• Active users in database
• Users who have used your bot
• Potential audience for broadcasts

💡 <b>Tips:</b>
• Use <code>/broadcast</code> to engage your audience
• Share more content to grow user base
• Monitor growth with this command
"""
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton("📢 Broadcast Message", callback_data="broadcast_help")],
            [InlineKeyboardButton("🔙 Back to Help", callback_data="help_back")],
            [InlineKeyboardButton("🔒 Close", callback_data="close")]
        ])
        await query.message.edit_text(users_text, reply_markup=reply_markup, parse_mode=ParseMode.HTML)
    
    elif data == "stats_help" and is_admin:
        now = datetime.now()
        delta = now - client.uptime
        time = get_readable_time(delta.seconds)
        stats_text = f"""
📊 <b>BOT STATISTICS</b> 📊

⏰ <b>Uptime:</b> {time}
🤖 <b>Bot Status:</b> Online
🔒 <b>Content Protection:</b> Enabled
⏱️ <b>Auto-Delete:</b> 20 minutes
👥 <b>Total Users:</b> {len(await full_userbase())}

⚙️ <b>Configuration:</b>
• Force subscription: ✅ Enabled
• Content protection: ✅ Enabled
• Auto-deletion: ✅ Enabled
• MongoDB: ✅ Connected

💡 <b>Performance:</b>
• Bot running smoothly
• All features active
• Ready for content sharing
"""
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton("🔙 Back to Help", callback_data="help_back")],
            [InlineKeyboardButton("🔒 Close", callback_data="close")]
        ])
        await query.message.edit_text(stats_text, reply_markup=reply_markup, parse_mode=ParseMode.HTML)
    
    elif data == "broadcast_help" and is_admin:
        broadcast_help = """
📢 <b>BROADCAST HELP</b> 📢

<b>How to use broadcast:</b>

1️⃣ <b>Reply to any message</b> with <code>/broadcast</code>
2️⃣ <b>Bot will send</b> that message to all users
3️⃣ <b>Get detailed statistics</b> of the broadcast

<b>Example:</b>
<code>/broadcast (as reply to your message)</code>

💡 <b>Tips:</b>
• Use for announcements
• Share new content updates
• Engage with your audience
• Monitor user engagement
"""
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton("🔙 Back to Help", callback_data="help_back")],
            [InlineKeyboardButton("🔒 Close", callback_data="close")]
        ])
        await query.message.edit_text(broadcast_help, reply_markup=reply_markup, parse_mode=ParseMode.HTML)
    
    elif data == "help_back" and is_admin:
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
        await query.message.edit_text(help_text, reply_markup=reply_markup, parse_mode=ParseMode.HTML)
    
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass





# Ansh Jain 
# Don't Remove Credit 🥺
# GitHub: https://github.com/jansh7784
# LinkedIn: https://linkedin.com/in/ansh--jain
# Developer @jansh7784
