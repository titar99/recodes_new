from PyroUbot import *

__MODULE__ = "youtube"
__HELP__ = """
<blockquote>
<b>◖ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʏᴏᴜᴛᴜʙᴇ ◗</b>

  <b>❑ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}song</code> [sᴏɴɢ ᴛɪᴛʟᴇ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>  ᴜɴᴛᴜᴋ ᴍᴇɴᴅᴏᴡɴʟᴏᴀᴅ ᴍᴜsɪᴄ ʏᴀɴɢ ᴅɪɪɴɢɪɴᴋᴀɴ

  <b>❑ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}vsong</code> [sᴏɴɢ ᴛɪᴛʟᴇ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏ ʏᴀɴɢ ᴅɪɪɴɢɪɴᴋᴀɴ
</blockquote>  
"""


@PY.UBOT("vsong")
@PY.TOP_CMD
async def _(client, message):
    await vsong_cmd(client, message)


@PY.UBOT("song")
@PY.TOP_CMD
async def _(client, message):
    await song_cmd(client, message)
