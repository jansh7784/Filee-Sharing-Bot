import os, asyncio, humanize
from pyrogram import Client, filters, __version__
from pyrogram.enums import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import FloodWait, UserIsBlocked, InputUserDeactivated
from bot import Bot
from config import ADMINS, FORCE_MSG, START_MSG, CUSTOM_CAPTION, DISABLE_CHANNEL_BUTTON, PROTECT_CONTENT, FILE_AUTO_DELETE
from helper_func import subscribed, encode, decode, get_messages
from database.database import add_user, del_user, full_userbase, present_user

madflixofficials = FILE_AUTO_DELETE
jishudeveloper = madflixofficials
file_auto_delete = humanize.naturaldelta(jishudeveloper)





@Bot.on_message(filters.command('start') & filters.private & subscribed)
async def start_command(client: Client, message: Message):
    id = message.from_user.id
    if not await present_user(id):
        try:
            await add_user(id)
        except:
            pass
    
    
    text = message.text
    if len(text)>7:
        try:
            base64_string = text.split(" ", 1)[1]
        except:
            return
        string = await decode(base64_string)
        argument = string.split("-")
        if len(argument) == 3:
            try:
                start = int(int(argument[1]) / abs(client.db_channel.id))
                end = int(int(argument[2]) / abs(client.db_channel.id))
            except:
                return
            if start <= end:
                ids = range(start,end+1)
            else:
                ids = []
                i = start
                while True:
                    ids.append(i)
                    i -= 1
                    if i < end:
                        break
        elif len(argument) == 2:
            try:
                ids = [int(int(argument[1]) / abs(client.db_channel.id))]
            except:
                return
        temp_msg = await message.reply("Please Wait...")
        try:
            messages = await get_messages(client, ids)
        except:
            await message.reply_text("Something Went Wrong..!")
            return
        await temp_msg.delete()
    
        madflix_msgs = [] # List to keep track of sent messages

        for msg in messages:

            if bool(CUSTOM_CAPTION) & bool(msg.document):
                caption = CUSTOM_CAPTION.format(previouscaption = "" if not msg.caption else msg.caption.html, filename = msg.document.file_name)
            else:
                caption = "" if not msg.caption else msg.caption.html

            if DISABLE_CHANNEL_BUTTON:
                reply_markup = msg.reply_markup
            else:
                reply_markup = None

            try:
                madflix_msg = await msg.copy(chat_id=message.from_user.id, caption = caption, parse_mode = ParseMode.HTML, reply_markup = reply_markup, protect_content=PROTECT_CONTENT)
                # await asyncio.sleep(0.5)
                madflix_msgs.append(madflix_msg)
                
            except FloodWait as e:
                await asyncio.sleep(e.x)
                madflix_msg = await msg.copy(chat_id=message.from_user.id, caption = caption, parse_mode = ParseMode.HTML, reply_markup = reply_markup, protect_content=PROTECT_CONTENT)
                madflix_msgs.append(madflix_msg)
                
            except:
                pass


        k = await client.send_message(chat_id = message.from_user.id, text=f"""
🎵 <b>MUSIC ACCESS GRANTED</b> 🎵

⏰ <b>Deleted in 1200 seconds until then enjoy coding :)</b> 🐍💻😊

🔒 <b>Content Protection:</b> Enabled
📱 <b>Download Status:</b> Ready

💡 <b>Happy Coding!</b> 🚀
• Python is awesome! 🐍
• Enjoy your music while coding 🎵
• Content will auto-delete to protect copyrights 🔒

🎶 <b>Keep coding and keep grooving!</b> 🎶
""", parse_mode=ParseMode.HTML)

        # Schedule the file deletion
        asyncio.create_task(delete_files(madflix_msgs, client, k))
        
        # for madflix_msg in madflix_msgs: 
            # try:
                # await madflix_msg.delete()
                # await k.edit_text("Your Video / File Is Successfully Deleted ✅") 
            # except:    
                # pass 

        return
    else:
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("😊 About Me", callback_data = "about"),
                    InlineKeyboardButton("🔒 Close", callback_data = "close")
                ]
            ]
        )
        await message.reply_text(
            text = START_MSG.format(
                first = message.from_user.first_name,
                last = message.from_user.last_name,
                username = None if not message.from_user.username else '@' + message.from_user.username,
                mention = message.from_user.mention,
                id = message.from_user.id
            ),
            reply_markup = reply_markup,
            disable_web_page_preview = True,
            quote = True
        )
        return

    



    
    
@Bot.on_message(filters.command('start') & filters.private)
async def not_joined(client: Client, message: Message):
    buttons = [
        [
            InlineKeyboardButton(text="Join Channel", url=client.invitelink)
        ]
    ]
    try:
        buttons.append(
            [
                InlineKeyboardButton(
                    text = 'Try Again',
                    url = f"https://t.me/{client.username}?start={message.command[1]}"
                )
            ]
        )
    except IndexError:
        pass

    await message.reply(
        text = FORCE_MSG.format(
                first = message.from_user.first_name,
                last = message.from_user.last_name,
                username = None if not message.from_user.username else '@' + message.from_user.username,
                mention = message.from_user.mention,
                id = message.from_user.id
            ),
        reply_markup = InlineKeyboardMarkup(buttons),
        quote = True,
        disable_web_page_preview = True
    )





@Bot.on_message(filters.command('users') & filters.private & filters.user(ADMINS))
async def get_users(client: Bot, message: Message):
    msg = await client.send_message(chat_id=message.chat.id, text="🔄 Processing user data...")
    users = await full_userbase()
    
    user_text = f"""
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
    
    await msg.edit_text(user_text, reply_markup=reply_markup, parse_mode=ParseMode.HTML)



@Bot.on_message(filters.private & filters.command('broadcast') & filters.user(ADMINS))
async def send_text(client: Bot, message: Message):
    if message.reply_to_message:
        query = await full_userbase()
        broadcast_msg = message.reply_to_message
        total = 0
        successful = 0
        blocked = 0
        deleted = 0
        unsuccessful = 0
        
        # Beautiful broadcast start message
        broadcast_start = """
📢 <b>BROADCAST IN PROGRESS</b> 📢

🔄 Sending message to all users...
⏳ This may take a few minutes

📊 <b>Progress will be updated here</b>
"""
        
        pls_wait = await message.reply(broadcast_start, parse_mode=ParseMode.HTML)
        
        for chat_id in query:
            try:
                await broadcast_msg.copy(chat_id)
                successful += 1
            except FloodWait as e:
                await asyncio.sleep(e.x)
                await broadcast_msg.copy(chat_id)
                successful += 1
            except UserIsBlocked:
                await del_user(chat_id)
                blocked += 1
            except InputUserDeactivated:
                await del_user(chat_id)
                deleted += 1
            except:
                unsuccessful += 1
                pass
            total += 1
            
            # Update progress every 10 users
            if total % 10 == 0:
                progress_text = f"""
📢 <b>BROADCAST IN PROGRESS</b> 📢

🔄 Sending message to all users...
⏳ Progress: {total}/{len(query)} users

📊 <b>Current Stats:</b>
✅ Successful: {successful}
❌ Failed: {unsuccessful}
🚫 Blocked: {blocked}
💀 Deleted: {deleted}
"""
                try:
                    await pls_wait.edit_text(progress_text, parse_mode=ParseMode.HTML)
                except:
                    pass
        
        # Beautiful completion message
        status = f"""
🎉 <b>BROADCAST COMPLETED</b> 🎉

📊 <b>Final Statistics:</b>

👥 <b>Total Users:</b> <code>{total}</code>
✅ <b>Successful:</b> <code>{successful}</code>
❌ <b>Unsuccessful:</b> <code>{unsuccessful}</code>
🚫 <b>Blocked Users:</b> <code>{blocked}</code>
💀 <b>Deleted Accounts:</b> <code>{deleted}</code>

📈 <b>Success Rate:</b> <code>{(successful/total*100):.1f}%</code>

💡 <b>Tips:</b>
• Clean up blocked users automatically
• Monitor engagement with your audience
• Use broadcasts to announce new content
"""
        
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton("📊 View Users", callback_data="users_help")],
            [InlineKeyboardButton("🔙 Back to Help", callback_data="help_back")],
            [InlineKeyboardButton("🔒 Close", callback_data="close")]
        ])
        
        return await pls_wait.edit_text(status, reply_markup=reply_markup, parse_mode=ParseMode.HTML)

    else:
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
        
        msg = await message.reply(broadcast_help, reply_markup=reply_markup, parse_mode=ParseMode.HTML)
        await asyncio.sleep(15)
        await msg.delete()






# Function to handle file deletion
async def delete_files(messages, client, k):
    await asyncio.sleep(FILE_AUTO_DELETE)  # Wait for the duration specified in config.py
    for msg in messages:
        try:
            await client.delete_messages(chat_id=msg.chat.id, message_ids=[msg.id])
        except Exception as e:
            print(f"The attempt to delete the media {msg.id} was unsuccessful: {e}")
    # Beautiful deletion completion message
    deletion_message = """
🗑️ <b>CONTENT DELETED</b> 🗑️

✅ <b>Auto-Deletion Complete</b>
⏰ <b>Timer:</b> 20 minutes expired
🔒 <b>Security:</b> Content protected

📱 <b>What happened:</b>
• Your music/video has been automatically deleted
• This prevents copyright issues
• Content was protected from forwarding/saving

💡 <b>Next Steps:</b>
• Use our bot again for more content
• Join our channel for exclusive access
• Share our links with friends

🎵 <b>Thank you for using our music bot!</b> 🎵
"""
    await k.edit_text(deletion_message, parse_mode=ParseMode.HTML)



# Ansh Jain 
# Don't Remove Credit 🥺
# GitHub: https://github.com/jansh7784
# LinkedIn: https://linkedin.com/in/ansh--jain
# Developer @jansh7784
