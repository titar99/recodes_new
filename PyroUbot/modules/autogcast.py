from PyroUbot import *
from PyroUbot.config import *

__MODULE__ = "auto gcast"
__HELP__ = """
<blockquote>
<b>◖ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀᴜᴛᴏ ɢᴄᴀꜱᴛ◗</b>

  <b>❑ ᴄᴍᴅ:</b> <code>{0}auto_gcast</code> (ǫᴜᴇʀʏ) - (ᴠᴀʟᴜᴇ)
      <b>❑> ǫᴜᴇʀʏ & ᴠᴀʟᴜᴇ:</b>
      <b>├➠ ON/OFF:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴋᴛɪғᴋᴀɴ ᴅᴀɴ ᴍᴇɴᴏɴᴀᴋᴛɪғᴋᴀɴ ɢᴄᴀsᴛ ᴏᴛᴏᴍᴀᴛɪs
      <b>├➠ TEXT - ᴋᴀᴛᴀ-ᴋᴀᴛᴀ/ʀᴇᴘʟʏ_ᴛᴇxᴛ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ᴛᴇxᴛ ᴋᴇ ᴅᴀᴛᴀʙᴀsᴇ ɢᴄᴀsᴛ ᴏᴛᴏᴍᴀᴛɪs
      <b>├➠ DELAY - ᴀɴɢᴋᴀ:</b> ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ ᴅᴜʀᴀsɪ ᴅᴇʟᴀʏ ᴘᴀᴅᴀ sᴇᴛɪᴀᴘ ᴘᴜᴛᴀʀᴀɴ ɢᴄᴀsᴛ ᴏᴛᴏᴍᴀᴛɪs
      <b>├➠ LIST - </b> ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ʟɪsᴛ ᴋᴀᴛᴀ ᴋᴀᴛᴀ ᴀᴜᴛᴏ ɢᴄᴀsᴛ ᴋᴀᴍᴜ ʏᴀɴɢ ɢᴀᴋ sᴇʙᴇʀᴀᴘᴀ ɪᴛᴜ
      <b>├➠ REMOVE - </b> ᴜɴᴛᴜᴋ ᴍᴇɴɢʜᴀᴘᴜs sᴇᴍᴜᴀ ᴋᴀᴛᴀ ᴋᴀᴛᴀ ᴀᴜᴛᴏ ɢᴄᴀsᴛ ʟᴜ ʏᴀɴɢ ᴊᴇʟᴇᴋ ɪᴛᴜ
      <b>╰➠ LIMIT - ON/OFF:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴋᴛɪғᴋᴀɴ ᴅᴀɴ ᴍᴇɴᴏɴᴀᴋᴛɪғᴋᴀɴ ғᴜɴɢsɪ ᴄᴇᴋ ʟɪᴍɪᴛ ᴏᴛᴏᴍᴀᴛɪs sᴇᴛɪᴀᴘ 𝟷𝟻 ᴍᴇɴɪᴛ
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍᴋᴀɴ ᴘᴇsᴀɴ ɢᴄᴀsᴛ sᴇᴄᴀʀᴀ ᴏᴛᴏᴍᴀᴛɪs
</blockquote>
"""

AG = []
LT = []

@PY.UBOT("auto_gcast")
@PY.TOP_CMD
async def _(client, message):
    proses = await EMO.PROSES(client)
    gagal = await EMO.GAGAL(client)
    sukses = await EMO.SUKSES(client)
    msg = await message.reply("<b>{proses}ʟᴏᴀᴅɪɴɢ...</b>", quote=True)
    type, value = extract_type_and_text(message)
    auto_text_vars = await get_vars(client.me.id, "AUTO_TEXT")

    if type == "on":
        if not auto_text_vars:
            return await msg.edit("<b>{gagal} ʜᴀʀᴀᴘ sᴇᴛᴛɪɴɢ ᴛᴇxᴛ ɢᴄᴀsᴛ ᴀɴᴅᴀ ᴛᴇʀʟᴇʙɪʜ ᴅᴀʜᴜʟᴜ</b>")

        if client.me.id not in AG:
            await msg.edit("<b>{sukses} ᴀᴜᴛᴏ ɢᴄᴀsᴛ ᴅɪᴀᴋᴛɪғᴋᴀɴ</b>")

            AG.append(client.me.id)

            done = 0
            while client.me.id in AG:
                delay = await get_vars(client.me.id, "DELAY_GCAST") or 1
                blacklist = await get_chat(client.me.id)
                txt = random.choice(auto_text_vars)

                group = 0
                async for dialog in client.get_dialogs():
                    if dialog.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP):
                        if dialog.chat.id not in blacklist and dialog.chat.id not in BLACKLIST_CHAT:
                            try:
                                await asyncio.sleep(1)
                                await client.send_message(dialog.chat.id, f"{txt} {random.choice(range(999))}")
                                group += 1
                            except FloodWait as e:
                                await asyncio.sleep(e.value)
                                await client.send_message(dialog.chat.id, f"{txt} {random.choice(range(999))}")
                                group += 1
                            except Exception:
                                pass

                if client.me.id not in AG:
                    return

                done += 1
                warning = await EMO.WARNING(client)
                sukses = await EMO.SUKSES(client)
                await msg.reply(
                    f"<b><emoji id={sukses}></emoji> ᴀᴜᴛᴏ ɢᴄᴀsᴛ ᴘᴜᴛᴀʀᴀɴ {done} ʙᴇʀʜᴀsɪʟ ᴅᴀɴ ᴛᴇʀᴋɪʀɪᴍ ᴋᴇ: {group} ɢʀᴏᴜᴘ\n\n{warning} ᴍᴇɴᴜɴɢɢᴜ {delay} ᴍᴇɴɪᴛ ʟᴀɢɪ ᴜɴᴛᴜᴋ ᴍᴇɴɢᴜʟᴀɴɢ ᴍᴇɴɢɪʀɪᴍ ᴘᴇsᴀɴ</b>",
                    quote=True,
                )
                await asyncio.sleep(int(60 * int(delay)))
        else:
            return await msg.delete()

    elif type == "off":
        if client.me.id in AG:
            AG.remove(client.me.id)
            return await msg.edit("<b><emoji id=6113647841459047673>✅</emoji> ᴀᴜᴛᴏ ɢᴄᴀsᴛ ᴛᴇʟᴀʜ ᴅɪɴᴏɴᴀᴋᴛɪғᴋᴀɴ</b>")
        else:
            return await msg.delete()

    elif type == "text":
        if not value:
            return await msg.edit("<b>ʜᴀʀᴀᴘ ᴍᴀsᴜᴋᴋᴀɴ ᴛᴇxᴛ ᴜɴᴛᴜᴋ ᴅɪ sɪᴍᴘᴀɴ sᴇʙᴀɢᴀɪ ᴛᴇxᴛ ᴀᴜᴛᴏ ɢᴄᴀsᴛ</b>")
        await add_auto_text(client, value)
        return await msg.edit("<b>ᴀᴜᴛᴏ ɢᴄᴀsᴛ ᴛᴇxᴛ: ʙᴇʀʜᴀsɪʟ ᴅɪ sɪᴍᴘᴀɴ</b>")

    elif type == "delay":
        await set_vars(client.me.id, "DELAY_GCAST", value)
        return await msg.edit(f"<b>ᴀᴜᴛᴏ ɢᴄᴀsᴛ ᴅᴇʟᴀʏ: ʙᴀʀʜᴀsɪʟ ᴋᴇ sᴇᴛᴛɪɴɢ {value} ᴍᴇɴɪᴛ</b>")

    elif type == "remove":
        if not value:
            return await msg.edit("<b>ʜᴀʀᴀᴘ ᴍᴀsᴜᴋᴋᴀɴ ᴀɴɢᴋᴀ ᴜɴᴛᴜᴋ ᴍᴇɴɢʜᴀᴘᴜs ʟɪsᴛ ᴛᴇxᴛ</b>")
        if value == "all":
            await set_vars(client.me.id, "AUTO_TEXT", [])
            return await msg.edit("<b>sᴇᴍᴜᴀ ᴛᴇxᴛ ʙᴇʀʜᴀsɪʟ ᴅɪʜᴀᴘᴜs</b>")
        try:
            value = int(value) - 1
            auto_text_vars.pop(value)
            await set_vars(client.me.id, "AUTO_TEXT", auto_text_vars)
            return await msg.edit(f"<b>ᴀᴜᴛᴏ ɢᴄᴀsᴛ ʀᴇᴍᴏᴠᴇ: ᴛᴇxᴛ ᴋᴇ {value+1} ʙᴇʀʜᴀsɪʟ ᴅɪʜᴀᴘᴜs\n\nsɪʟᴀʜᴋᴀɴ ᴋᴇᴛɪᴋ: <code>{message.text.split()[0]} list</code>, ᴋᴇᴍʙᴀʟɪ ᴜɴᴛᴜᴋ ᴍᴇɴɢᴇᴄᴇᴋ ᴀᴘᴀᴋᴀʜ sᴜᴅᴀʜ ᴛᴇʀʜᴀᴘᴜs</b>")
        except Exception as error:
            return await msg.edit(str(error))

    elif type == "list":
        if not auto_text_vars:
            return await msg.edit("<b>ᴀᴜᴛᴏ ɢᴄᴀsᴛ ᴛᴇxᴛ ᴋᴏsᴏɴɢ</b>")
        txt = "<b>ᴅᴀғᴛᴀʀ ᴀᴜᴛᴏ ɢᴄᴀsᴛ ᴛᴇxᴛ</b>\n\n"
        for num, x in enumerate(auto_text_vars, 1):
            txt += f"{num}: {x}\n\n"
        txt += f"<b>\nᴜɴᴛᴜᴋ ᴍᴇɴɢʜᴀᴘᴜs ᴛᴇxᴛ ᴋᴇᴛɪᴋ: <code>{message.text.split()[0]} remove ᴀɴɢᴋᴀ/ᴀʟʟ</code></b>"
        return await msg.edit(txt)

    elif type == "limit":
        if value == "off":
            if client.me.id in LT:
                LT.remove(client.me.id)
                return await msg.edit("<b>ᴀᴜᴛᴏ ᴄᴇᴋ ʟɪᴍɪᴛ ᴅɪɴᴏɴᴀᴋᴛɪғᴋᴀɴ</b>")
            else:
                return await msg.delete()

        elif value == "on":
            if client.me.id not in LT:
                LT.append(client.me.id)
                await msg.edit("<b>ᴀᴜᴛᴏ ᴄᴇᴋ ʟɪᴍɪᴛ sᴛᴀʀᴛᴇᴅ</b>")
                while client.me.id in LT:
                    for x in range(2):
                        await limit_cmd(client, message)
                        await asyncio.sleep(5)
                    await asyncio.sleep(1200)
            else:
                return await msg.delete()
        else:
            return await msg.edit("<b>~ʜᴀʀᴀᴘ ᴍᴀsᴜᴋᴋᴀɴ ᴠᴀʟᴇᴜ ᴏɴ/ᴏғғ ᴜɴᴛᴜᴋ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ᴘᴇʀɪɴᴛᴀʜ ɪɴɪ</b>")
    else:
        return await msg.edit("<b>ǫᴜᴇʀʏ ʏᴀɴɢ ᴅɪᴍᴀsᴜᴋᴋᴀɴ sᴀʟᴀʜ</b>")


async def add_auto_text(client, text):
    auto_text = await get_vars(client.me.id, "AUTO_TEXT") or []
    auto_text.append(text)
    await set_vars(client.me.id, "AUTO_TEXT", auto_text)


def extract_type_and_text(message):
    args = message.text.split(None, 2)
    if len(args) < 2:
        return None, None

    type = args[1]
    msg = message.reply_to_message.text if message.reply_to_message else args[2] if len(args) > 2 else None
    return type, msg

@PY.BOT("send")
@PY.UBOT("send")
@PY.TOP_CMD
async def send_msg_cmd(client, message):
    if message.reply_to_message:
        if len(message.command) < 2:
            chat_id = message.chat.id
        else:
            chat_id = message.text.split()[1]
        send_done = await get_vars(client.me.id, "SEND_DONE") or "6111585093220830556"
        if not client.me.id == client.me.id:
            if message.reply_to_message.reply_markup:
                try:
                    x = await client.get_inline_bot_results(client.me.username, f"get_send {id(message)}")
                    await client.send_inline_bot_result(chat_id, x.query_id, x.results[0].id)
                    tm = await message.reply(f"<emoji id=6113647841459047673>✅</emoji> Pesan berhasil dikirim ke {chat_id}")
                    await asyncio.sleep(5)
                    await message.delete()
                    await tm.delete()
                except Exception as error:
                    await message.reply(str(error))
        else:
            try:
                await message.reply_to_message.copy(chat_id)
                tm = await message.reply(f"<emoji id=6113647841459047673>✅</emoji> Pesan berhasil dikirim ke {chat_id}")
                await asyncio.sleep(3)
            except Exception as t:
                return await message.reply(str(t))
    else:
        if len(message.command) < 3:
            return await message.reply("Ketik yang benar")
        chat_id = message.text.split(None, 2)[1]
        chat_text = message.text.split(None, 2)[2]
        try:
            await client.send_message(chat_id, chat_text)
            tm = await message.reply(f"<emoji id=6113647841459047673>✅</emoji> Pesan berhasil dikirim ke {chat_id}")
            await asyncio.sleep(3)
        except Exception as t:
            return await message.reply(str(t))
          

@PY.INLINE("^get_send")
@INLINE.QUERY
async def send_inline(client, inline_query):
    _id = int(inline_query.query.split()[1])
    m = [obj for obj in get_objects() if id(obj) == _id][0]
    await client.answer_inline_query(
        inline_query.id,
        cache_time=0,
        results=[
            (
                InlineQueryResultArticle(
                    title="get send!",
                    reply_markup=m.reply_to_message.reply_markup,
                    input_message_content=InputTextMessageContent(m.reply_to_message.text),
                )
            )
        ],
    )
