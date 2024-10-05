from PyroUbot import *

__MODULE__ = "search"
__HELP__ = """
<blockquote>
<b>◖ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴇᴀʀᴄʜ ◗</b>

  <b>❑ ᴄᴍᴅ:</b> <code>{0}pic</code> [ǫᴜᴇʀʏ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴᴄᴀʀɪ ᴘʜᴏᴛᴏ ʀᴀɴᴅᴏᴍ ᴅᴀʀɪ ɢᴏᴏɢʟᴇ

  <b>❑ ᴄᴍᴅ:</b> <code>{0}gif</code> [ǫᴜᴇʀʏ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴᴄᴀʀɪ ɢɪꜰᴛ/ᴀɴɪᴍᴀᴛɪᴏɴ ʀᴀɴᴅᴏᴍ ᴅᴀʀɪ ɢᴏᴏɢʟᴇ
</blockquote>  
"""


@PY.UBOT("pic")
@PY.TOP_CMD
async def _(client, message):
    await pic_bing_cmd(client, message)


@PY.UBOT("bing")
@PY.TOP_CMD
async def _(client, message):
    await pic_bing_cmd(client, message)


@PY.UBOT("gif")
@PY.TOP_CMD
async def _(client, message):
    await gif_cmd(client, message)
