from pyrogram.enums import ChatType
from asyncio import sleep

from PyroUbot import *

__MODULE__ = "archive"
__HELP__ = """
<blockquote><b>『 bantuan untuk archive 』</b>

  <b>• perintah:</b> <code>{0}archiveall</code> group or users
  <b>• penjelasan:</b> untuk mengarchivekan semua pesan pribadi
  <b>• contoh : </b> <code>{0}archiveall</code> group

  <b>• perintah:</b> <code>{0}unarchiveall</code> group or users
  <b>• penjelasan:</b> untuk mengarchivekan semua pesan pribadi
  <b>• contoh : </b> <code>{0}unarchiveall</code> group

  <b>• perintah:</b> <code>{0}archive</code>
  <b>• penjelasan:</b> untuk mengarchivekan pesan chat saat ini

  <b>• perintah:</b> <code>{0}unarchive</code>
  <b>• penjelasan:</b> untuk mengunarchivekan chat saat ini</blockquote>

"""


cnt = "<emoji id=5211112665237175703>✅</emoji>"
ex = "<emoji id=5852812849780362931>❌</emoji>"
brs = "<emoji id=5210935111289159311>🔘</emoji>"


@PY.UBOT("archiveall")
@PY.TOP_CMD
async def _(client, message):
    done = 0
    gagal = 0
    rizal = await message.reply_text("<emoji id=6010111371251815589>⏳</emoji>proccesing....")

    if len(message.command) != 2:
        await rizal.edit(f"{ex} gunakan type users atau group")
        return

    query = message.command[1]

    chat_ids = await get_data_id(client, query)

    for chat_id in chat_ids:
        await sleep(1)
        try:
            await client.archive_chats(chat_id)
            done += 1
        except:
            gagal += 1
            pass

    await rizal.edit(f"""{brs} **berhasil menjalankan archive**
<blockquote>{cnt}**berhasil** : {done} **grup**</blockquote>
<blockquote>{ex}**gagal** : {gagal} **grup**</blockquote>
**powered by : **<a href=tg://user?id={client.me.id}>{client.me.first_name} {client.me.last_name or ''}</a>""")


@PY.UBOT("unarchiveall")
@PY.TOP_CMD
async def _(client, message):
    done = 0
    gagal = 0
    rizal = await message.reply_text("<emoji id=6010111371251815589>⏳</emoji>proccesing....")

    if len(message.command) != 2:
        await rizal.edit(f"{ex} gunakan type users atau group")
        return

    query = message.command[1]

    chat_ids = await get_data_id(client, query)

    for chat_id in chat_ids:
        await sleep(1)
        try:
            await client.unarchive_chats(chat_id)
            done += 1
        except:
            gagal += 1
            pass

    await rizal.edit(f"""{brs} **berhasil menjalankan unarchive**
<blockquote>{cnt}**berhasil** : {done} **grup**</blockquote>
<blockquote>{ex}**gagal** : {gagal} **grup**</blockquote>
**powered by : **<a href=tg://user?id={client.me.id}>{client.me.first_name} {client.me.last_name or ''}</a>""")


@PY.UBOT("archive")
@PY.TOP_CMD
async def _(client, message):
    user_id = message.chat.id
    c = await client.archive_chats(user_id)
    if c:
        await message.reply_text(f"{cnt} berhasil meng archivekan pengguna..")
    else:
                await message.reply_text(f"{ex} gagal meng archivekan pengguna..")

@PY.UBOT("unarchive")
@PY.TOP_CMD
async def _(client, message):
    user_id = message.chat.id
    c = await client.archive_chats(user_id)
    if c:
        await message.reply_text(f"{cnt} berhasil mengun archivekan pengguna..")
    else:
                await message.reply_text(f"{ex} gagal meng archivekan pengguna..")
