# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper




from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery



@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ 𝐎ᴡɴᴇʀ : <a href='https://t.me/Fushiguro_x'>𝐅ᴜsʜɪɢᴜʀᴏ</a> \n ○ 𝐀ɴɪᴍᴇ 𝐂ʜᴀɴɴᴇʟ : <a href='https://t.me/Anime_Duo'>𝐀ɴɪᴍᴇ 𝐇ɪɴᴅɪ</a>  \n ○ 𝐇ᴀɴɪᴍᴇ 𝐂ʜᴀɴɴᴇʟ : <a href='https://t.me/+rqJjl4BBd3M4NDc1'>𝐇ᴜɴᴛᴀɪ 𝐖ᴏʀʟᴅ</a> \n ○ 𝐃ᴇᴠʟᴏᴘᴇʀ : <a href='https://t.me/VR_Necromancer'>ɴᴇᴄʀᴏᴍᴀɴᴄᴇʀ</a> </b> \n\n ᴘᴏᴡᴇʀᴇᴅ ʙʏ <a href='https://t.me/VR_unreal'>ᴠʀ ᴜɴʀᴇᴀʟ✨</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("⚡️ ᴀɴɪᴍᴇ ᴅᴜᴏ", url='https://t.me/Anime_Duo'),
                        InlineKeyboardButton("✨ ʜᴇᴍᴛᴀɪ ᴡᴏʀʟᴅ", url='https://t.me/+rqJjl4BBd3M4NDc1')
                    ],[
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ],[
                        InlineKeyboardButton("📡 ᴠʀ ᴜɴʀᴇᴀʟ", url='https://t.me/vr_unreal'),
                        InlineKeyboardButton("📹 ᴠʀ ꜱᴜᴘᴘᴏʀᴛ", url='https://t.me/vr_support')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
