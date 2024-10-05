from PyroUbot import *

__MODULE__ = "translate"
__HELP__ = """
<blockquote>
<b>◖ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴛʀᴀɴsʟᴀᴛᴇ ◗</b>

  <b>❑ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}tr</code> [ʀᴇᴘʟʏ/ᴛᴇxᴛ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴᴇʀᴊᴇᴍᴀʜᴋᴀɴ ᴛᴇxᴛ

  <b>❑ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}tts</code> [ʀᴇᴘʟʏ/ᴛᴇxᴛ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ ᴛᴇᴄᴛ ᴍᴇɴᴊᴀᴅɪ ᴍᴇɴᴊᴀᴅɪ ᴘᴇsᴀɴ sᴜᴀʀᴀ

  <b>❑ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}set_lang</code>
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ ʙᴀʜᴀsᴀ ᴛʀᴀɴsʟᴀᴛᴇ
</blockquote>  
"""


@PY.UBOT("tts")
@PY.TOP_CMD
async def _(client, message):
    await tts_cmd(client, message)


@PY.UBOT("tr")
@PY.TOP_CMD
async def _(client, message):
    await tr_cmd(client, message)


@PY.UBOT("set_lang")
@PY.TOP_CMD
async def _(client, message):
    await set_lang_cmd(client, message)


@PY.INLINE("^ubah_bahasa")
@INLINE.QUERY
async def _(client, inline_query):
    await ubah_bahasa_inline(client, inline_query)


@PY.CALLBACK("^set_bahasa")
@INLINE.DATA
async def _(client, callback_query):
    await set_bahasa_callback(client, callback_query)
