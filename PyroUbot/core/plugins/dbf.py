from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pytz import timezone

from PyroUbot import *

# ========================== #
# 𝔻𝔸𝕋𝔸𝔹𝔸𝕊𝔼 ℙℝ𝔼𝕄𝕀𝕌𝕄 #
# ========================== #


async def prem_user(client, message):
    proses = await get_vars(client.me.id, "EMOJI_PROSES") or "5960640164114993927"
    Tm = await message.reply(f"<b><emoji id={proses}>⏳</emoji> ᴘʀᴏᴄᴇssɪɴɢ . . .</b>")
    if message.from_user.id not in await get_seles():
        return await Tm.edit(f"<blockquote>ᴜɴᴛᴜᴋ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ᴘᴇʀɪɴᴛᴀʜ ɪɴɪ ᴀɴᴅᴀ ʜᴀʀᴜs ᴍᴇɴᴊᴀᴅɪ ʀᴇsᴇʟʟᴇʀ ᴛᴇʀʟᴇʙɪʜ ᴅᴀʜᴜʟᴜ</blockquote>")
    user_id, get_bulan = await extract_user_and_reason(message)
    if not user_id:
        return await Tm.edit(f"<blockquote><b>{message.text} ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ - ʙᴜʟᴀɴ</b></blockquote>")
    try:
        get_id = (await client.get_users(user_id)).id
    except Exception as error:
        return await Tm.edit(error)
    if not get_bulan:
        get_bulan = 1
    premium = await get_prem()
    if get_id in premium:
        return await Tm.edit(f"<blockquote>ᴅɪᴀ sᴜᴅᴀʜ ʙɪsᴀ ᴍᴇᴍʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ</blockquote>")
    added = await add_prem(get_id)
    if added:
        now = datetime.now(timezone("Asia/Jakarta"))
        expired = now + relativedelta(months=int(get_bulan))
        await set_expired_date(get_id, expired)
        await Tm.edit(f"<blockquote><b><emoji id=6278555627639801385>✅</emoji>{get_id} ᴛᴇʟᴀʜ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ sᴇʟᴀᴍᴀ {get_bulan} ʙᴜʟᴀɴ\n\nsɪʟᴀʜᴋᴀɴ ʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ ᴅɪ @{bot.me.username}</b></blockquote>")
        await bot.send_message(
            OWNER_ID,
            f"• {message.from_user.id} ─> {get_id} •",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "👤 ᴘʀᴏғɪʟ",
                            callback_data=f"profil {message.from_user.id}",
                        ),
                        InlineKeyboardButton("ᴘʀᴏғɪʟ 👤", callback_data=f"profil {get_id}"),
                    ],
                ]
            ),
        )
    else:
        await Tm.delete()
        await message.reply_text("ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ ʏᴀɴɢ ᴛɪᴅᴀᴋ ᴅɪᴋᴇᴛᴀʜᴜɪ")


async def unprem_user(client, message):
    proses = await get_vars(client.me.id, "EMOJI_PROSES") or "5960640164114993927"
    user_id = await extract_user(message)
    Tm = await message.reply(f"<blockquote><b><emoji id={proses}>⏳</emoji> ᴘʀᴏᴄᴇssɪɴɢ . . .</b></blockquote>")
    
    if message.from_user.id not in await get_seles():
        return await Tm.edit(f"<blockquote>ᴜɴᴛᴜᴋ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ᴘᴇʀɪɴᴛᴀʜ ɪɴɪ ᴀɴᴅᴀ ʜᴀʀᴜs ᴍᴇɴᴊᴀᴅɪ ʀᴇsᴇʟʟᴇʀ</blockquote>")

    if not user_id:
        return await Tm.edit(f"<blockquote><b>ʙᴀʟᴀs ᴘᴇsᴀɴ ᴘᴇɴɢɢᴜɴᴀ ᴀᴛᴀᴜ ʙᴇʀɪᴋᴀɴ ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ</b></blockquote>")
    
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        await Tm.edit(error)
        return

    delpremium = await get_prem()
    if user.id not in delpremium:
        return await Tm.edit("<b>ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ</b>")
    
    removed = await remove_prem(user.id)
    if removed:
        await Tm.edit(f"<blockquote><b><emoji id=6278555627639801385>✅</emoji> {user.mention} ʙᴇʀʜᴀsɪʟ ᴅɪʜᴀᴘᴜs</b></blockquote>")
    else:
        await Tm.delete()
        await message.reply_text("ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ ʏᴀɴɢ ᴛɪᴅᴀᴋ ᴅɪᴋᴇᴛᴀʜᴜɪ")


async def get_prem_user(client, message):
    text = ""
    count = 0
    for user_id in await get_prem():
        try:
            user = await bot.get_users(user_id)
            count += 1
            userlist = f"• {count}: <a href=tg://user?id={user.id}>{user.first_name} {user.last_name or ''}</a> > <code>{user.id}</code>"
        except Exception:
            continue
        text += f"{userlist}\n"
    if not text:
        await message.reply_text("ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴘᴇɴɢɢᴜɴᴀ ʏᴀɴɢ ᴅɪᴛᴇᴍᴜᴋᴀɴ")
    else:
        await message.reply_text(text)


# ========================== #
# 𝔻𝔸𝕋𝔸𝔹𝔸𝕊𝔼 𝔹𝕃𝔸ℂ𝕂𝕃𝕀𝕊𝕋 #
# ========================== #


async def add_blaclist(client, message):
    proses = await get_vars(client.me.id, "EMOJI_PROSES") or "5960640164114993927"
    Tm = await message.reply(f"<b><emoji id={proses}>⏳</emoji> ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ . . .</b>")
    chat_id = message.chat.id
    chat_type = message.chat.type
    if chat_type in (ChatType.GROUP, ChatType.SUPERGROUP):
        sukses = await get_vars(client.me.id, "EMOJI_SUKSES") or "5787188704434982946"
        chat_id = message.chat.id
        blacklist = await get_chat(client.me.id)
        if chat_id in blacklist:
            return await Tm.edit(f"<blockquote><b><emoji id={sukses}>✅</emoji>{message.chat.title} • already included in the blacklist broadcast!</b></blockquote>")
        gagal = await get_vars(client.me.id, "EMOJI_GAGAL") or "5438630285635757876"
        sukses = await get_vars(client.me.id, "EMOJI_SUKSES") or "5787188704434982946"
        add_blacklist = await add_chat(client.me.id, chat_id)
        if add_blacklist:
            return await Tm.edit(f"<blockquote><b><emoji id={sukses}>✅</emoji><b>{message.chat.title} • has been added to the blacklist broadcast!</b></blockquote>")
        else:
            return await Tm.edit(f"<emoji id={gagal}>❎</emoji> ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ ʏᴀɴɢ ᴛɪᴅᴀᴋ ᴅɪᴋᴇᴛᴀʜᴜɪ")
    elif chat_type == ChatType.PRIVATE:
        sukses = await get_vars(client.me.id, "EMOJI_SUKSES") or "5787188704434982946"
        chat_id = message.chat.id
        user = message.chat
        rax = f"[{user.first_name} {user.last_name or ''}](tg://user?id={user.id})"
        blacklist = await get_chat(client.me.id)
        if chat_id in blacklist:
            return await Tm.edit(
                f"<blockquote><b><emoji id={sukses}>✅</emoji> {chat_id} | {rax} - Sudah Masuk Daftar Hitam Broadcast</b></blockquote>"
            )
        gagal = await get_vars(client.me.id, "EMOJI_GAGAL") or "5438630285635757876"
        add_blacklist = await add_chat(client.me.id, chat_id)
        if add_blacklist:
            return await Tm.edit(
                f"<blockquote><b><emoji id={sukses}>✅</emoji> {chat_id} | {rax} - Berhasil Di Masukkan Ke Daftar Hitam Broadcast</b></blockquote>"
            )
        else:
            return await Tm.edit(f"<blockquote><b><i><emoji id={gagal}>❎</emoji> TERJADI KESALAHAN YANG TIDAK DIKETAHUI</i></b></blockquote>")
    else:
        return await Tm.edit(f"<blockquote><emoji id={gagal}>❎</emoji> PERINTAH INI BERFUNGSI DI GROUP SAJA</blockquote>")


async def del_blacklist(client, message):
    proses = await get_vars(client.me.id, "EMOJI_PROSES") or "5960640164114993927"
    Tm = await message.reply(f"<b><emoji id={proses}>⏳</emoji> ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ . . .</b>")
    
    chat_id = message.chat.id
    chat_type = message.chat.type

    if chat_type in (ChatType.GROUP, ChatType.SUPERGROUP):
        sukses = await get_vars(client.me.id, "EMOJI_SUKSES") or "5787188704434982946"
        blacklist = await get_chat(client.me.id)
        
        if chat_id not in blacklist:
            return await Tm.edit(f"<blockquote><b><emoji id={sukses}>✅</emoji>{message.chat.title} • tidak ada dalam daftar hitam broadcast!</b></blockquote>")
        
        gagal = await get_vars(client.me.id, "EMOJI_GAGAL") or "5438630285635757876"
        del_blacklist = await remove_chat(client.me.id, chat_id)
        
        if del_blacklist:
            return await Tm.edit(f"<blockquote><b><emoji id={sukses}>✅</emoji><b>{message.chat.title} • berhasil dihapus dari daftar hitam broadcast!</b></blockquote>")
        else:
            return await Tm.edit(f"<emoji id={gagal}>❎</emoji> ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ ʏᴀɴɢ ᴛɪᴅᴀᴋ ᴅɪᴋᴇᴛᴀʜᴜɪ")
    
    elif chat_type == ChatType.PRIVATE:
        sukses = await get_vars(client.me.id, "EMOJI_SUKSES") or "5787188704434982946"
        user = message.chat
        rax = f"[{user.first_name} {user.last_name or ''}](tg://user?id={user.id})"
        blacklist = await get_chat(client.me.id)
        
        if chat_id not in blacklist:
            return await Tm.edit(
                f"<blockquote><b><emoji id={sukses}>✅</emoji> {chat_id} | {rax} - tidak ada dalam daftar hitam broadcast!</b></blockquote>"
            )
        
        gagal = await get_vars(client.me.id, "EMOJI_GAGAL") or "5438630285635757876"
        del_blacklist = await remove_chat(client.me.id, chat_id)
        
        if del_blacklist:
            return await Tm.edit(
                f"<blockquote><b><emoji id={sukses}>✅</emoji> {chat_id} | {rax} - berhasil dihapus dari daftar hitam broadcast!</b></blockquote>"
            )
        else:
            return await Tm.edit(f"<blockquote><b><i><emoji id={gagal}>❎</emoji> TERJADI KESALAHAN YANG TIDAK DIKETAHUI</i></b></blockquote>")
    
    else:
        gagal = await get_vars(client.me.id, "EMOJI_GAGAL") or "5438630285635757876"
        return await Tm.edit(f"<blockquote><emoji id={gagal}>❎</emoji> PERINTAH INI BERFUNGSI DI GROUP SAJA</blockquote>")


async def get_blacklist(client, message):
    proses = await get_vars(client.me.id, "EMOJI_PROSES") or "5960640164114993927"
    Tm = await message.reply(f"<b><b><emoji id={proses}>⏳</emoji> Please, wait a moment . . .</b>")
    msg = "<blockquote>"
    blacklist = await get_chat(client.me.id)
    msg += f"<b>Total Blacklist: {len(blacklist)}</b>\n"
    for X in blacklist:
        try:
            get = await client.get_chat(X)
            msg += f"<b>- {get.title or get.first_name} | <code>{get.id}</code></b>\n"
        except BaseException:
            msg += f"<b>- <code>{X}</code></b>\n"
    msg += "</blockquote>"
    await Tm.delete()
    await message.reply(msg)


async def rem_all_blacklist(client, message):
    proses = await get_vars(client.me.id, "EMOJI_PROSES") or "5960640164114993927"
    msg = await message.reply(f"<emoji id={proses}>⏳</emoji> <b>sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs....</b>", quote=True)
    gagal = await get_vars(client.me.id, "EMOJI_GAGAL") or "5438630285635757876"
    sukses = await get_vars(client.me.id, "EMOJI_SUKSES") or "5787188704434982946"
    get_bls = await get_chat(client.me.id)
    if len(get_bls) == 0:
        return await msg.edit(f"<b><emoji id={gagal}>❎</emoji> ᴅᴀғᴛᴀʀ ɴᴇʀᴀᴋᴀ ᴀɴᴅᴀ ᴋᴏsᴏɴɢ</b>")
    for X in get_bls:
        await remove_chat(client.me.id, X)
    await msg.edit(f"<blockquote><b><emoji id={sukses}>✅</emoji> sᴇᴍᴜᴀ ᴅᴀғᴛᴀʀ ɴᴇʀᴀᴋᴀ ᴛᴇʟᴀʜ ʙᴇʀʜᴀsɪʟ ᴅɪʜᴀᴘᴜs</b></blockquote>")


# ========================== #
# 𝔻𝔸𝕋𝔸𝔹𝔸𝕊𝔼 ℝ𝔼𝕊𝔼𝕃𝕃𝔼ℝ #
# ========================== #


async def seles_user(client, message):
    user_id = await extract_user(message)
    Tm = await message.reply(f"<blockquote><b>ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ . . .</b></blockquote>")
    if not user_id:
        return await Tm.edit(f"<blockquote><b>ʙᴀʟᴀs ᴘᴇsᴀɴ ᴘᴇɴɢɢᴜɴᴀ ᴀᴛᴀᴜ ʙᴇʀɪᴋᴀɴ ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ</b></blockquote>")
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        await Tm.edit(error)
    reseller = await get_seles()
    if user.id in reseller:
        return await Tm.edit("sᴜᴅᴀʜ ᴍᴇɴᴊᴀᴅɪ ʀᴇsᴇʟʟᴇʀ.")
    added = await add_seles(user.id)
    if added:
        await add_prem(user.id)
        await Tm.edit(f"<blockquote><b><emoji id=6278555627639801385>✅</emoji> {user.mention} ᴛᴇʟᴀʜ ᴍᴇɴᴊᴀᴅɪ ʀᴇsᴇʟʟᴇʀ</b></blockquote>")
    else:
        await Tm.delete()
        await message.reply_text("ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ ʏᴀɴɢ ᴛɪᴅᴀᴋ ᴅɪᴋᴇᴛᴀʜᴜɪ")


async def unseles_user(client, message):
    user_id = await extract_user(message)
    Tm = await message.reply(f"<blockquote><b>ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ . . .</b></blockquote>")
    if not user_id:
        return await Tm.edit(f"<blockquote><b>ʙᴀʟᴀs ᴘᴇsᴀɴ ᴘᴇɴɢɢᴜɴᴀ ᴀᴛᴀᴜ ʙᴇʀɪᴋᴀɴ ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ</b></blockquote>")
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        await Tm.edit(error)
    delreseller = await get_seles()
    if user.id not in delreseller:
        return await Tm.edit("ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ")
    removed = await remove_seles(user.id)
    if removed:
        await remove_prem(user.id)
        await Tm.edit(f"<blockquote>{user.mention} ʙᴇʀʜᴀsɪʟ ᴅɪʜᴀᴘᴜs</blockquote>")
    else:
        await Tm.delete()
        await message.reply_text("ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ ʏᴀɴɢ ᴛɪᴅᴀᴋ ᴅɪᴋᴇᴛᴀʜᴜɪ")


async def get_seles_user(cliebt, message):
    text = ""
    count = 0
    for user_id in await get_seles():
        try:
            user = await bot.get_users(user_id)
            count += 1
            user = f"• {count}: <a href=tg://user?id={user.id}>{user.first_name} {user.last_name or ''}</a> > <code>{user.id}</code>"
        except Exception:
            continue
        text += f"{user}\n"
    if not text:
        await message.reply_text(f"<blockquote>ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴘᴇɴɢɢᴜɴᴀ ʏᴀɴɢ ᴅɪᴛᴇᴍᴜᴋᴀɴ</blockquote>")
    else:
        await message.reply_text(text)


# ========================== #
# 𝔻𝔸𝕋𝔸𝔹𝔸𝕊𝔼 𝔼𝕏ℙ𝕀ℝ𝔼𝔻 #
# ========================== #


async def expired_add(client, message):
    Tm = await message.reply(f"<blockquote><b>ᴘʀᴏᴄᴇssɪɴɢ . . .</b></blockquote>")
    
    if message.from_user.id not in await get_seles():
        return await Tm.edit(f"<blockquote>ᴜɴᴛᴜᴋ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ᴘᴇʀɪɴᴛᴀʜ ɪɴɪ ᴀɴᴅᴀ ʜᴀʀᴜs ᴍᴇɴᴊᴀᴅɪ ʀᴇsᴇʟʟᴇʀ</blockquote>")
    
    user_id, get_day = await extract_user_and_reason(message)
    if not user_id:
        return await Tm.edit(f"<b>{message.text} ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ - ʜᴀʀɪ</b>")
    elif user_id not in ubot._get_my_id:
        return await Tm.edit(f"<blockquote><b>{user_id} ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴅᴀʟᴀᴍ sʏsᴛᴇᴍ</b></blockquote>")
    
    try:
        get_id = (await client.get_users(user_id)).id
    except Exception as error:
        return await Tm.edit(error)

    if not get_day:
        get_day = 30

    now = datetime.now(timezone("Asia/Jakarta"))
    expire_date = now + timedelta(days=int(get_day))
    await set_expired_date(user_id, expire_date)
    await Tm.edit(f"<blockquote>{get_id} ᴛᴇʟᴀʜ ᴅɪᴀᴋᴛɪғᴋᴀɴ sᴇʟᴀᴍᴀ {get_day} ʜᴀʀɪ.</blockquote>")


async def expired_cek(client, message):
    user_id = await extract_user(message)
    
    if message.from_user.id not in await get_seles():
        return await message.reply("<blockquote>ᴜɴᴛᴜᴋ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ᴘᴇʀɪɴᴛᴀʜ ɪɴɪ ᴀɴᴅᴀ ʜᴀʀᴜs ᴍᴇɴᴊᴀᴅɪ ʀᴇsᴇʟʟᴇʀ</blockquote>")
    
    if not user_id:
        return await message.reply("ᴘᴇɴɢɢᴜɴᴀ ᴛɪᴅᴀᴋ ᴛᴇᴍᴜᴋᴀɴ")
    
    expired_date = await get_expired_date(user_id)
    if expired_date is None:
        await message.reply(f"{user_id} ʙᴇʟᴜᴍ ᴅɪᴀᴋᴛɪғᴋᴀɴ.")
    else:
        remaining_days = (expired_date - datetime.now()).days
        await message.reply(f"<blockquote>{user_id} ᴀᴋᴛɪғ ʜɪɴɢɢᴀ {expired_date.strftime('%d-%m-%Y %H:%M:%S')}. ᴍᴀsɪʜ ᴀᴅᴀ ᴡᴀᴋᴛᴜ {remaining_days} ʜᴀʀɪ.</blockquote>")


async def un_expired(client, message):
    user_id = await extract_user(message)
    Tm = await message.reply("<b>ᴍᴇᴍᴘʀᴏsᴇs. . .</b>")
    
    if message.from_user.id not in await get_seles():
        return await Tm.edit("<blockquote>ᴜɴᴛᴜᴋ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ᴘᴇʀɪɴᴛᴀʜ ɪɴɪ ᴀɴᴅᴀ ʜᴀʀᴜs ᴍᴇɴᴊᴀᴅɪ ʀᴇsᴇʟʟᴇʀ</blockquote>")
    
    if not user_id:
        return await Tm.edit("<b>ᴜsᴇʀ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ</b>")
    
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await Tm.edit(error)

    await rem_expired_date(user.id)
    return await Tm.edit(f"<blockquote><b>✅ {user.id} ᴇxᴘɪʀᴇᴅ ᴛᴇʟᴀʜ ᴅɪʜᴀᴘᴜs</b></blockquote>")
