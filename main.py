import discord
from discord.ext import commands
import asyncio
import os
from myserver import server_on


GUILD_ID = 923167904629928005  # ใส่ไอดีเซิร์ฟเวอร์ของคุณ

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'✅ บอทออนไลน์เป็น {bot.user}')

@bot.command()
async def dm_embed(ctx):
    await ctx.send("✅ บอทได้รับคำสั่งแล้ว กำลังทำงาน...")

    guild = bot.get_guild(GUILD_ID)
    if not guild:
        await ctx.send("❌ ไม่พบเซิร์ฟเวอร์")
        return

    # Embed ตัวแรก CZ Shop
    embed1 = discord.Embed(
        title="CZ Shop ร้านค้าขายโปร Free fire 🚀",
        description=(
            "+ เริ่มต้นแค่วันละ 35 บาท เท่านั้น !!\n"
            "+ CZ Panel `มอง ล็อคไหล่ สไนล็อค สไนสับไว`\n"
            "+ CZ Modmenu `มองเส้น ล็อคหัว`\n"
            "+ เติมเงินออโต้ รองรับทั้งธนาคาร และวอเล็ท"
        ),
        color=discord.Color.blue()
    )
    embed1.add_field(
        name="🌐 เว็บไซต์",
        value="ซื้อ CZ panel [คลิกที่นี่](https://czshop.rdcw.xyz/)",
        inline=False
    )
    embed1.set_image(url="https://i.postimg.cc/9f4tRtF4/Annotation-2025-03-16-005706.png")

    # Embed ตัวที่สอง Mazda Shop
    embed2 = discord.Embed(
        title="Mazda Shop ร้านค้าขายโปร Free fire และ โค้ด LV.8-30 พร้อมลงแรงค์ 🚀",
        description=(
            "+ จำหน่ายโค้ด LV.8-30 มีแพ็คเติมโต 1000 เพชร ราคาถูกก !!\n"
            "+ จำหน่ายโปร Free fire ios / PC\n"
            "+ เติมเงินออโต้ รองรับทั้งธนาคาร และวอเล็ท"
        ),
        color=discord.Color.green()
    )
    embed2.add_field(
        name="🌐 เว็บไซต์",
        value="ซื้อ โค้ด [คลิกที่นี่](https://mazdamodzshop.com/?page=homesite)",
        inline=False
    )
    embed2.set_image(url="https://i.postimg.cc/KvzK8cYj/Annotation-2025-03-16-010045.png")

    success = 0
    failed = 0

    for member in guild.members:
        if member.bot:
            continue
        try:
            await member.send(embeds=[embed1, embed2])
            await member.send("* Discord https://discord.gg/XyjyUnxPDw")
            success += 1
            print(f"✅ ส่งข้อความให้ {member.name}")
            await asyncio.sleep(10)
        except discord.Forbidden:
            failed += 1
            print(f"❌ ไม่สามารถส่งให้ {member.name} (ปิด DM)")
        except Exception as e:
            failed += 1
            print(f"❌ ข้อผิดพลาด {member.name}: {e}")

    await ctx.send(f"📌 ส่งข้อความสำเร็จ: {success} คน, ล้มเหลว: {failed} คน")

server_on()

bot.run(os.getenv('TOKEN'))
