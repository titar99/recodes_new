from PyroUbot import *

__MODULE__ = "memes"
__HELP__ = """
<blockquote>
<b>◖ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴍᴇᴍᴇs◗</b>

  <b>❑ ᴄᴍᴅ:</b> <code>{0}memes</code> [ᴛᴇxᴛ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ sᴛɪᴋᴇʀ ᴍᴇᴍᴇs ʀᴀɴᴅᴏᴍ
</blockquote>  
"""


@PY.UBOT("memes")
@PY.TOP_CMD
async def _(client, message):
    await memes_cmd(client, message)
