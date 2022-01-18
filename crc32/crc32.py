from tkinter import N
from unicodedata import name
from redbot.core import commands
from redbot.core.bot import Red
import discord
import crcengine
import codecs

class CRC32(commands.Cog):
    def __init__(self, bot: Red):
        self.bot = bot

    async def red_delete_data_for_user(self, **kwargs):
        """Nothing to delete"""
        return

    @commands.command()
    async def crc32(self, ctx, string):
        if string:
            crc_algorithm = crcengine.new("crc32")
            crc32Result = crc_algorithm(string.encode("utf-8"))
            crc32ResultHex = hex(crc32Result)[2:].upper()
            crc32ResultHexLittle = codecs.encode(codecs.decode(crc32ResultHex, 'hex')[::-1], 'hex').decode().upper()
            embedCRC32 = discord.Embed(title="CRC32 Hash", color=0xC60000)
            embedCRC32.add_field(
                name="Decimal:", value=crc32Result, inline=False)
            embedCRC32.add_field(
                name="Hexadecimal:", value=crc32ResultHex, inline=False
            )
            embedCRC32.add_field(
                name="Hexadecimal (Little Endian):", value=crc32ResultHexLittle, inline=False
            )
            await ctx.reply(embed=embedCRC32)
        else:
            embedNoString = discord.Embed(title="CRC32 Hash", color=0xC60000)
            embedNoString.add_field(
                name="Error", value="Please enter a string", inline=False
            )
            await ctx.reply(embed=embedNoString)
