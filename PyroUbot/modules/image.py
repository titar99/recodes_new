import asyncio
import io
import os

import cv2
import requests
from pyrogram import raw

from PyroUbot import *


__MODULE__ = "Image"
__HELP__ = """
<blockquote><b>◖ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɪᴍᴀɢᴇ◗</b></blockquote>
  <blockquote>
  <b>❑ ᴄᴍᴅ:</b> <code>{0}rbg</code> [ʀᴇᴘʟʏ ᴛᴏ ᴘʜᴏᴛᴏ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢʜᴀᴘᴜs ʟᴀᴛᴀʀ ʙᴇʟᴀᴋᴀɴɢ ɢᴀᴍʙᴀʀ

  <b>❑ ᴄᴍᴅ:</b> <code>{0}blur</code> [ʀᴇᴘʟʏ ᴛᴏ ᴘʜᴏᴛᴏ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴇʀɪᴋᴀ ᴇꜰᴇᴋ ʙʟᴜʀ ᴋᴇ ɢᴀᴍʙᴀʀ

  <b>❑ ᴄᴍᴅ:</b> <code>{0}miror</code> [ʀᴇᴘʟʏ ᴛᴏ ᴘʜᴏᴛᴏ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴇʀɪᴋᴀɴ ᴇꜰᴇᴋ ᴄᴇʀᴍɪɴ ᴋᴇ ɢᴀᴍʙᴀʀ

  <b>❑ ᴄᴍᴅ:</b> <code>{0}negative</code> [ʀᴇᴘʟʏ ᴛᴏ ᴘʜᴏᴛᴏ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴇʀɪᴋᴀɴ ᴇꜰᴇᴋ ɴᴇɢᴀᴛɪᴠᴇ ᴋᴇ ɢᴀᴍʙᴀʀ
  </blockquote>
"""


async def ReTrieveFile(input_file_name):
    headers = {
        "X-API-Key": RMBG_API,
    }
    files = {
        "image_file": (input_file_name, open(input_file_name, "rb")),
    }
    return requests.post(
        "https://api.remove.bg/v1.0/removebg",
        headers=headers,
        files=files,
        allow_redirects=True,
        stream=True,
    )
  

@PY.UBOT("rbg")
@PY.TOP_CMD
async def rbg_cmd(client, message):
    if RMBG_API is None:
        return
    if message.reply_to_message:
        reply_message = message.reply_to_message
        xx = await message.reply("<code>Processing...</code>")
        try:
            if (
                isinstance(reply_message.media, raw.types.MessageMediaPhoto)
                or reply_message.media
            ):
                downloaded_file_name = await client.download_media(
                    reply_message, "./downloads/"
                )
                await xx.edit("<code>Processing...</code>")
                output_file_name = await ReTrieveFile(downloaded_file_name)
                os.remove(downloaded_file_name)
            else:
                await xx.edit("<code>Gambar tidak dapat dihapus background nya.</code>")
        except Exception as e:
            await xx.edit(f"{(str(e))}")
            return
        contentType = output_file_name.headers.get("content-type")
        if "image" in contentType:
            with io.BytesIO(output_file_name.content) as remove_bg_image:
                remove_bg_image.name = "rbg.png"
                await client.send_document(
                    message.chat.id,
                    document=remove_bg_image,
                    force_document=True,
                    reply_to_message_id=message.id,
                )
                await xx.delete()
        else:
            await xx.edit(
                "<b>Error RMBG-API)</b>\n<i>{}</i>".format(
                    output_file_name.content.decode("UTF-8")
                ),
            )
    else:
        return await message.reply("Silakan balas ke gambar.")



@PY.UBOT("blur")
@PY.TOP_CMD
async def blur_cmd(client, message):
    ureply = message.reply_to_message
    xd = await message.reply("<code>Processing...</code>")
    if not ureply:
        return await xd.edit("Silakan balas ke gambar")
    yinsxd = await client.download_media(ureply, "./downloads/")
    if yinsxd.endswith(".tgs"):
        cmd = ["lottie_convert.py", yinsxd, "yin.png"]
        file = "yin.png"
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        img = cv2.VideoCapture(yinsxd)
        heh, lol = img.read()
        cv2.imwrite("yin.png", lol)
        file = "yin.png"
    yin = cv2.imread(file)
    ayiinxd = cv2.GaussianBlur(yin, (35, 35), 0)
    cv2.imwrite("yin.jpg", ayiinxd)
    await client.send_photo(
        message.chat.id,
        "yin.jpg",
        reply_to_message_id=message.id,
    )
    await xd.delete()
    os.remove("yin.png")
    os.remove("yin.jpg")
    os.remove(yinsxd)


@PY.UBOT("negative")
@PY.TOP_CMD
async def negative_cmd(client, message):
    ureply = message.reply_to_message
    ayiin = await message.reply("Processing...")
    if not ureply:
        return await ayiin.edit("Silakan balas ke gambar.")
    ayiinxd = await client.download_media(ureply, "./downloads/")
    if ayiinxd.endswith(".tgs"):
        cmd = ["lottie_convert.py", ayiinxd, "yin.png"]
        file = "yin.png"
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        img = cv2.VideoCapture(ayiinxd)
        heh, lol = img.read()
        cv2.imwrite("yin.png", lol)
        file = "yin.png"
    yinsex = cv2.imread(file)
    kntlxd = cv2.bitwise_not(yinsex)
    cv2.imwrite("yin.jpg", kntlxd)
    await client.send_photo(
        message.chat.id,
        "yin.jpg",
        reply_to_message_id=message.id,
    )
    await ayiin.delete()
    os.remove("yin.png")
    os.remove("yin.jpg")
    os.remove(ayiinxd)

@PY.UBOT("miror")
@PY.TOP_CMD
async def miror_cmd(client, message):
    ureply = message.reply_to_message
    kentu = await message.reply("<code>Processing...</code>")
    if not ureply:
        return await kentu.edit("Silakan balas ke gambar.")
    xnxx = await client.download_media(ureply, "./downloads/")
    if xnxx.endswith(".tgs"):
        cmd = ["lottie_convert.py", xnxx, "yin.png"]
        file = "yin.png"
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        img = cv2.VideoCapture(xnxx)
        kont, tol = img.read()
        cv2.imwrite("yin.png", tol)
        file = "yin.png"
    yin = cv2.imread(file)
    mmk = cv2.flip(yin, 1)
    ayiinxd = cv2.hconcat([yin, mmk])
    cv2.imwrite("yin.jpg", ayiinxd)
    await client.send_photo(
        message.chat.id,
        "yin.jpg",
        reply_to_message_id=message.id,
    )
    await kentu.delete()
    os.remove("yin.png")
    os.remove("yin.jpg")
    os.remove(xnxx)
