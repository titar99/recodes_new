"""
yang hapus credits pantatnya bisulan
create by: https://t.me/NorSodikin 
"""

from .. import *

__MODULE__ = "sudo"
__HELP__ = """
<blockquote>
◖ <b>ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴜᴅᴏ</b> ◗

  <b>❑ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}addsudo</code>
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ᴜsᴇʀ ᴋᴇ ᴅᴀʟᴀᴍ ᴅᴀғᴛᴀʀ sᴜᴅᴏ

  <b>❑ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}delsudo</code>
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢʜᴀᴘᴜs ᴜsᴇʀ ᴅᴀʀɪ ᴅᴀғᴛᴀʀ sᴜᴅᴏ
  
  <b>❑ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}getsudo</code>
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ ᴅᴀғᴛᴀʀ sᴜᴅᴏ
</blockquote>  
"""


@PY.UBOT("addsudo")
@PY.TOP_CMD
async def _(client, message):
    msg = await message.reply("<b>sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs...</b>")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit("<b>➡️ Hᴀʀᴀᴘ ʙᴀʟᴀs ᴋᴇ ᴜsᴇʀ ᴀᴛᴀᴜ ᴋᴇᴛɪᴋ ᴜsᴇʀ_ɪᴅ ʏᴀɴɢ ɪɴɢɪɴ ᴅɪᴛᴀᴍʙᴀʜᴋᴀɴ ᴋᴇ ᴅᴀғᴛᴀʀ sᴜᴅᴏ</b>")

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    sudo_users = await get_list_from_vars(client.me.id, "SUDO_USERS")

    if user.id in sudo_users:
        return await msg.edit(f"<b>✨ [{user.first_name} {user.last_name or ''}](tg://user?id={user.id}) sᴜᴅᴀʜ ʙᴇʀᴀᴅᴀ ᴅᴀʟᴀᴍ ᴅᴀғᴛᴀʀ sᴜᴅᴏ</b>")

    try:
        await add_to_vars(client.me.id, "SUDO_USERS", user.id)
        return await msg.edit(f"<b>✅ [{user.first_name} {user.last_name or ''}](tg://user?id={user.id}) ʙᴇʀʜᴀsɪʟ ᴅɪᴛᴀᴍʙᴀʜᴋᴀɴ ᴋᴇ ᴅᴀғᴛᴀʀ sᴜᴅᴏ</b>")
    except Exception as error:
        return await msg.edit(error)


@PY.UBOT("delsudo")
@PY.TOP_CMD
async def _(client, message):
    msg = await message.reply("<b>sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs...</b>")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit("<b>➡️ ʜᴀʀᴀᴘ ʙᴀʟᴀs ᴋᴇ ᴜsᴇʀ ᴀᴛᴀᴜ ᴋᴇᴛɪᴋ ᴜsᴇʀ_ɪᴅ ʏᴀɴɢ ᴍᴀᴜ ᴅɪʜᴀᴘᴜs ᴅᴀʀɪ ᴅᴀғᴛᴀʀ sᴜᴅᴏ</b>")

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    sudo_users = await get_list_from_vars(client.me.id, "SUDO_USERS")

    if user.id not in sudo_users:
        return await message.reply(f"<b>✨ [{user.first_name} {user.last_name or ''}](tg://user?id={user.id}) ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴅᴀʟᴀᴍ ᴅᴀғᴛᴀʀ sᴜᴅᴏ</b>")

    try:
        await remove_from_vars(client.me.id, "SUDO_USERS", user.id)
        return await msg.edit(f"<b>❌ [{user.first_name} {user.last_name or ''}](tg://user?id={user.id}) ʙᴇʀʜᴀsɪʟ ᴅɪʜᴀᴘᴜs ᴅᴀʀɪ ᴅᴀғᴛᴀʀ sᴜᴅᴏ</b>")
    except Exception as error:
        return await msg.edit(error)


@PY.UBOT("getsudo")
@PY.TOP_CMD
async def _(client, message):
    msg = await message.reply("<b>sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs...</b>")
    sudo_users = await get_list_from_vars(client.me.id, "SUDO_USERS")

    if not sudo_users:
        return await msg.edit("<s>ᴅᴀғᴛᴀʀ sᴜᴅᴏ ᴋᴏsᴏɴɢ</s>")

    sudo_list = []
    for user_id in sudo_users:
        try:
            user = await client.get_users(int(user_id))
            sudo_list.append(f" ├ [{user.first_name} {user.last_name or ''}](tg://user?id={user.id}) | <code>{user.id}</code>")
        except:
            continue

    if sudo_list:
        response = "<b>❏ ᴅᴀғᴛᴀʀ sᴜᴅᴏ:</b>\n" + "\n".join(sudo_list) + f"\n <b>╰ ᴛᴏᴛᴀʟ sᴜᴅᴏ_ᴜsᴇʀs:</b> <code>{len(sudo_list)}</code>"
        return await msg.edit(response)
    else:
        return await msg.edit("<b>ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇɴɢᴀᴍʙɪʟ ᴅᴀғᴛᴀʀ sᴜᴅᴏ sᴀᴀᴛ ɪɴɪ</b>")
