from redbot.core import commands
from redbot.core.bot import Red
import discord
import hashlib

class MD5(commands.Cog):
    def __init__(self, bot: Red):
        self.bot = bot

    async def red_delete_data_for_user(self, **kwargs):
        """Nothing to delete"""
        return

    @commands.command()
    async def md5(self, ctx, string):
        if string:
            md5Result = hashlib.md5(string.encode("utf-8").lower()).hexdigest().upper()
            embedMD5 = discord.Embed(title="MD5 Hash", color=0xC60000)
            embedMD5.add_field(
                name=string.lower(), value="00" + md5Result[2:16], inline=False
            )
            await ctx.reply(embed=embedMD5)
        else:
            embedNoString = discord.Embed(title="MD5 Hash", color=0xC60000)
            embedNoString.add_field(
                name="Error", value="Please enter a string", inline=False
            )
            await ctx.reply(embed=embedNoString)
 