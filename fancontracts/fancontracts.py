from discord.ext.commands import bot
from discord.ext.commands.help import Paginator
from redbot.core import commands
from random import randrange
from redbot.core.bot import Red
import discord
import requests

class FanContracts(commands.Cog):
    def __init__(self, bot: Red):
        self.bot = bot

    async def red_delete_data_for_user(self, **kwargs):
        """Nothing to delete"""
        return

    @commands.command(aliases=["con"])
    async def fancontracts(self, ctx, string, method: str = "id"):

        url = "https://fancontracts.com/api/?method=" + method + "&query=" + string

        response = requests.post(url)
        data = response.json()
        entry = data

        embed = discord.Embed(title="FanContracts Lookup", color=0xC60000)

        # Expected JSON data example:
        # {
        #   "title": "The Terminator",
        #   "id": "2-30-9445647-51",
        #   "rating": "no votes",
        #   "platform": "PS",
        #   "mission": "Chongqing",
        #   "tcount": 4,
        #   "type": "Loud Gun-",
        #   "complications": "None-",
        #   "disguises": "Any Disguise-",
        #   "methods": "Shotgun-",
        #   "author": "Hichkas47",
        #   "more": "Greetings, T-47. I have some juicy intel here. We have found Sarah Conner's grandchidren under disguise in Chongqing, China. They are planning a wrathful war against us in the near future; So, rise and kill first! Don't forget your Shotgun."
        # }
        # Expected JSON if there are no results:
        # {"error":"Nothing Found"}
        
        # If JSON returns with no results, return an error message
        if "error" in entry:
            embed.add_field(name="Error", value="No results found for search method, " + method + ".")
            await ctx.send(embed=embed)
            return        
        else:
            embed.title = entry["title"]
            embed.add_field(name="ID", value=entry["id"], inline=True)
            embed.add_field(name="Rating", value=entry["rating"], inline=True)
            embed.add_field(name="Platform", value=entry["platform"], inline=True)
            embed.add_field(name="Mission", value=entry["mission"], inline=True)
            embed.add_field(name="Type", value=entry["type"], inline=True)
            embed.add_field(name="Complications", value=entry["complications"], inline=True)
            embed.add_field(name="Disguises", value=entry["disguises"], inline=True)
            embed.add_field(name="Methods", value=entry["methods"], inline=True)
            embed.add_field(name="Author", value=entry["author"], inline=True)
            embed.add_field(name="More", value=entry["more"], inline=True)

        embed.set_footer(text="Powered by https://fancontracts.com")
        await ctx.reply(embed=embed)
