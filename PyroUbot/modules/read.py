from PyroUbot import *

__MODULE__ = "read"
__HELP__ = """
<blockquote>
<b>◖ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴏᴄʀ ◗</b>

  <b>❑ ᴄᴍᴅ:</b> <code>{0}ocr</code> [ʀᴇᴘʟʏ ᴛᴏ ᴍᴇᴅɪᴀ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴀᴄᴀ ᴛᴇxᴛ ᴘᴀᴅᴀ ᴍᴇᴅɪᴀ ʏᴀɴɢ ᴅɪ ʀᴇᴘʟʏ
</blockquote>  
"""


@PY.UBOT("ocr")
@PY.TOP_CMD
async def _(client, message):
    await read_cmd(client, message)
