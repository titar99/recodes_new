from PyroUbot import *

__MODULE__ = "qrcode"
__HELP__ = """
<blockquote>
<b>◖ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ǫʀᴄᴏᴅᴇ ◗</b>

  <b>❑ ᴄᴍᴅ:</b> <code>{0}qrGen</code> [ᴛᴇxᴛ ǫʀᴄᴏᴅᴇ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ ǫʀᴄᴏᴅᴇ ᴛᴇxᴛ ᴍᴇɴᴊᴀᴅɪ ɢᴀᴍʙᴀʀ

  <b>❑ ᴄᴍᴅ:</b> <code>{0}qrRead</code> [ʀᴇᴘʟʏ ᴛᴏ ᴍᴇᴅɪᴀ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ ǫʀᴄᴏᴅᴇ ᴍᴇɴᴊᴀᴅɪ ᴛᴇxᴛ
</blockquote>  
"""


@PY.UBOT("qrgen")
@PY.TOP_CMD
async def _(client, message):
    await qr_gen_cmd(client, message)


@PY.UBOT("qrread")
@PY.TOP_CMD
async def _(client, message):
    await qr_read_cmd(client, message)
