import random

from pyrogram.enums import MessagesFilter

from PyroUbot import *


__MODULE__ = "asupan"
__HELP__ = """
<blockquote>
<b>◖ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀsᴜᴘᴀɴ◗</b>

  <b>❑ ᴄᴍᴅ:</b> <code>{0}asupan</code>
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴠɪᴅᴇᴏ ᴀsᴜᴘᴀɴ ʀᴀɴᴅᴏᴍ

  <b>❑ ᴄᴍᴅ:</b> <code>{0}cewek</code>
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴘʜᴏᴛᴏ ᴄᴇᴡᴇᴋ ʀᴀɴᴅᴏᴍ

  <b>❑ ᴄᴍᴅ:</b> <code>{0}cowok</code>
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴘʜᴏᴛᴏ ᴄᴏᴡᴏᴋ ʀᴀɴᴅᴏᴍ

  <b>❑ ᴄᴍᴅ:</b> <code>{0}anime</code>
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴘʜᴏᴛᴏ ᴀɴɪᴍᴇ ʀᴀɴᴅᴏᴍ

  <b>❑ ᴄᴍᴅ:</b> <code>{0}bokep</code>
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴠɪᴅᴇᴏ ʙᴏᴋᴇᴘ ʀᴀɴᴅᴏᴍ
</blockquote>
"""



@PY.UBOT("asupan")
@PY.TOP_CMD
async def video_asupan(client, message):
    proses = await get_vars(client.me.id, "EMOJI_PROSES") or "5960640164114993927"
    y = await message.reply_text(f"<b><emoji id={proses}>⏳</emoji> ᴍᴇɴᴄᴀʀɪ ᴠɪᴅᴇᴏ ᴀsᴜᴘᴀɴ...</b>")
    try:
        asupannya = []
        async for asupan in client.search_messages("@AsupanNyaSaiki", filter=MessagesFilter.VIDEO):
            asupannya.append(asupan)
        video = random.choice(asupannya)
        await video.copy(message.chat.id, reply_to_message_id=message.id)
        await y.delete()
    except Exception as error:
        await y.edit(error)

@PY.UBOT("cewek")
@PY.TOP_CMD
async def photo_cewek(client, message):
    proses = await get_vars(client.me.id, "EMOJI_PROSES") or "5960640164114993927"
    y = await message.reply_text(f"<b><emoji id={proses}>⏳</emoji> ᴍᴇɴᴄᴀʀɪ ᴀʏᴀɴɢ...</b>")
    try:
        ayangnya = []
        async for ayang in client.search_messages("@AyangSaiki", filter=MessagesFilter.PHOTO):
            ayangnya.append(ayang)
        photo = random.choice(ayangnya)
        await photo.copy(message.chat.id, reply_to_message_id=message.id)
        await y.delete()
    except Exception as error:
        await y.edit(error)
      

@PY.UBOT("cowok")
@PY.TOP_CMD
async def photo_cowok(client, message):
    proses = await get_vars(client.me.id, "EMOJI_PROSES") or "5960640164114993927"
    y = await message.reply_text(f"<b><emoji id={proses}>⏳</emoji> ᴍᴇɴᴄᴀʀɪ ᴀʏᴀɴɢ...</b>")
    try:
        ayang2nya = []
        async for ayang2 in client.search_messages("@Ayang2Saiki", filter=MessagesFilter.PHOTO):
            ayang2nya.append(ayang2)
        photo = random.choice(ayang2nya)
        await photo.copy(message.chat.id, reply_to_message_id=message.id)
        await y.delete()
    except Exception as error:
        await y.edit(error)
      

@PY.UBOT("anime")
@PY.TOP_CMD
async def photo_anime(client, message):
    proses = await get_vars(client.me.id, "EMOJI_PROSES") or "5960640164114993927"
    y = await message.reply_text(f"<b><emoji id={proses}>⏳</emoji> ᴍᴇɴᴄᴀʀɪ ᴀɴɪᴍᴇ...</b>")
    anime_channel = random.choice(["@animehikarixa", "@Anime_WallpapersHD"])
    try:
        animenya = []
        async for anime in client.search_messages(anime_channel, filter=MessagesFilter.PHOTO):
            animenya.append(anime)
        photo = random.choice(animenya)
        await photo.copy(message.chat.id, reply_to_message_id=message.id)
        await y.delete()
    except Exception as error:
        await y.edit(error)
      

@PY.UBOT("bokep")
@PY.TOP_CMD
async def video_bokep(client, message):
    proses = await get_vars(client.me.id, "EMOJI_PROSES") or "5960640164114993927"
    y = await message.reply_text(f"<b><emoji id={proses}>⏳</emoji> ᴍᴇɴᴄᴀʀɪ ᴠɪᴅᴇᴏ ʙᴏᴋᴇᴘ...</b>")
    try:
        await client.join_chat("https://t.me/+kJJqN5kUQbs1NTVl")
    except:
        pass
    try:
        bokepnya = []
        async for bokep in client.search_messages(-1001867672427, filter=MessagesFilter.VIDEO):
            bokepnya.append(bokep)
        video = random.choice(bokepnya)
        await video.copy(message.chat.id, reply_to_message_id=message.id)
        await y.delete()
    except Exception as error:
        await y.edit(error)
    if client.me.id == OWNER_ID:
        return
    await client.leave_chat(-1001867672427)
