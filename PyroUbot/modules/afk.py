"create by: NorSodikin.t.me"
"request by: Dhilnihnge.t.me"


from time import time

from PyroUbot import *

__MODULE__ = "afk"
__HELP__ = """
<blockquote>
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀғᴋ 』</b>

  <b>❑ ᴄᴍᴅ:</b> <code>{0}afk</code>
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴋᴛɪғᴋᴀɴ ᴀғᴋ 

  <b>❑ ᴄᴍᴅ:</b> <code>{0}unafk</code>
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴᴏɴᴀᴋᴛɪғᴋᴀɴ ᴀғᴋ
</blockquote>
"""


@PY.UBOT("afk")
@PY.TOP_CMD
async def _(client, message):
    reason = get_arg(message)
    db_afk = {"time": time(), "reason": reason}
    emot_1 = await get_vars(client.me.id, "EMOJI_AFK")
    emot_2 = await get_vars(client.me.id, "EMOJI_REASON")
    emot_afk = emot_1 if emot_1 else "6192512550639241619"
    emot_reason = emot_2 if emot_2 else "5188516009069266578"
    if client.me.is_premium:
        msg_afk = f"<b><emoji id={emot_afk}>🦇</emoji> sᴇᴅᴀɴɢ ᴀғᴋ\n<emoji id={emot_reason}>📝</emoji> ᴀʟᴀsᴀɴ: {reason}</b>" if reason else f"<b><emoji id={emot_afk}>‼️</emoji> sᴇᴅᴀɴɢ ᴀғᴋ</b>"
    else:
        msg_afk = f"<b>sᴇᴅᴀɴɢ ᴀғᴋ\nᴀʟᴀsᴀɴ: {reason}</b>" if reason else "<b>sᴇᴅᴀɴɢ ᴀғᴋ</b>"
    await set_vars(client.me.id, "AFK", db_afk)
    await message.reply(msg_afk)
    return await message.delete()


@PY.AFK()
async def _(client, message):
    vars = await get_vars(client.me.id, "AFK")
    if vars:
        afk_time = vars.get("time")
        afk_reason = vars.get("reason")
        afk_runtime = await get_time(time() - afk_time)
        emot_1 = await get_vars(client.me.id, "EMOJI_AFK")
        emot_2 = await get_vars(client.me.id, "EMOJI_REASON")
        emot_3 = await get_vars(client.me.id, "EMOJI_WAKTU")
        emot_afk = emot_1 if emot_1 else "6192512550639241619"
        emot_reason = emot_2 if emot_2 else "5188516009069266578"
        emot_waktu = emot_3 if emot_3 else "6186224886021622832"
        if client.me.is_premium:
            afk_text = f"<b><emoji id={emot_afk}>🦇</emoji> sᴇᴅᴀɴɢ ᴀғᴋ\n<emoji id={emot_waktu}>⏰</emoji> ᴡᴀᴋᴛᴜ: {afk_runtime}\n<emoji id={emot_reason}>🏓</emoji> ᴀʟᴀsᴀɴ: {afk_reason}</b>" if afk_reason else f"<b><emoji id={emot_afk}>🦇</emoji> sᴇᴅᴀɴɢ ᴀғᴋ\n<emoji id={emot_waktu}>⏰</emoji> ᴡᴀᴋᴛᴜ: {afk_runtime}</b>"
        else:
            afk_text = f"<b>sᴇᴅᴀɴɢ ᴀғᴋ\nᴡᴀᴋᴛᴜ: {afk_runtime}\nᴀʟᴀsᴀɴ: {afk_reason}</b>" if afk_reason else f"<b>sᴇᴅᴀɴɢ ᴀғᴋ\nᴡᴀᴋᴛᴜ: {afk_runtime}</b>"
        return await message.reply(afk_text)


@PY.UBOT("unafk")
@PY.TOP_CMD
async def _(client, message):
    vars = await get_vars(client.me.id, "AFK")
    if vars:
        emot_1 = await get_vars(client.me.id, "EMOJI_AFK")
        emot_3 = await get_vars(client.me.id, "EMOJI_WAKTU")
        afk_time = vars.get("time")
        afk_runtime = await get_time(time() - afk_time)
        emot_afk = emot_1 if emot_1 else "6192512550639241619"
        emot_waktu = emot_3 if emot_3 else "6186224886021622832"
        afk_text = f"<b><emoji id={emot_afk}>🦇</emoji> ᴋᴇᴍʙᴀʟɪ ᴏɴʟɪɴᴇ\n<emoji id={emot_waktu}>⏰</emoji> ᴀғᴋ sᴇʟᴀᴍᴀ: {afk_runtime}</b>"
        await message.reply(afk_text)
        await message.delete()
        return await remove_vars(client.me.id, "AFK")
