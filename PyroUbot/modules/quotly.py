from PyroUbot import *

__MODULE__ = "quotly"
__HELP__ = """
<blockquote>
<b>◖ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ǫᴜᴏᴛʟʏ ◗</b>

  <b>❑ ᴄᴍᴅ:</b> <code>{0}q</code> [ʀᴇᴘʟʏ ᴛᴏ ᴛᴇxᴛ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ ᴛᴇxᴛ ᴍᴇɴᴊᴀᴅɪ sᴛɪᴄᴋᴇʀ
</blockquote>  
"""


@PY.UBOT("q")
@PY.TOP_CMD
async def _(client, message):
    await quotly_cmd(client, message)
