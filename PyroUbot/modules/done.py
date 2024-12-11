import asyncio
import datetime
from PyroUbot import *

__MODULE__ = "done"
__HELP__ = """
 <blockquote><b>Bantuan Untuk Done</b>

• <b>Perintah</b> : <code>{0}done</code> <b>[name item],[harga] [pembayaran]</b>
• <b>Penjelasan : konfirmasi pembayaran.</b></blockquote>
"""

@PY.UBOT("done")
async def done_command(client, message):
    raxxy = await message.reply(f"<blockquote><emoji id=6160967592103120271>🔁</emoji> Sedang Diproses...</blockquote>")
    await asyncio.sleep(5)
    try:
        args = message.text.split(" ", 1)
        if len(args) < 2 or ',' not in args[1]:
            await raxxy.edit(f"<emoji id=6161010516006276367>❌</emoji> Bego liat di modulesnya cara makenya njing!.")
            return
        
        parts = args[1].split(",", 2)
        
        if len(parts) < 2:
            await raxxy.edit(f"<emoji id=6161010516006276367>❌</emoji> Bego liat di modulesnya cara makenya njing!.")
            return
        
        name_item = parts[0].strip()
        price = parts[1].strip()
        payment = parts[2].strip() if len(parts) > 2 else "Lainnya"        
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        response = (
            f"「 𝗧𝗥𝗔𝗡𝗦𝗔𝗞𝗦𝗜 𝗕𝗘𝗥𝗛𝗔𝗦𝗜𝗟 」\n\n"
            f"📦 <b>Barang : {name_item}</b>\n"
            f"💸 <b>Nominal : {price}</b>\n"
            f"🕰️ <b>Waktu : {time}</b>\n"
            f"💬 <b>Payment : {payment}</b>\n\n"
            f"𝗧𝗲𝗿𝗶𝗺𝗮𝗸𝗮𝘀𝗶𝗵 𝗧𝗲𝗹𝗮𝗵 𝗢𝗿𝗱𝗲𝗿"
        )
        await raxxy.edit(response)
    
    except Exception as e:
        await raxxy.edit(f"error: {e}")
