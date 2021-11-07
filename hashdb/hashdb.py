from discord.ext.commands import bot
from discord.ext.commands.help import Paginator
from redbot.core import commands
from random import randrange
from redbot.core.bot import Red
import asyncio
import discord
import requests

class HashDB(commands.Cog):
    def __init__(self, bot: Red):
        self.bot = bot

    async def red_delete_data_for_user(self, **kwargs):
        """Nothing to delete"""
        return

    @commands.command()
    async def hashdb(self, ctx, string, resourcetype: str = "any"):

        url = "https://hitmandb.notex.app/search"
        pagenumber = 0

        reqJson = {
            "search_term": string,
            "number_of_results": 10,
            "resource_type": resourcetype,
            "page_number": pagenumber,
        }

        response = requests.post(url, json=reqJson)
        data = response.json()
        entry = data

        embed = discord.Embed(title="Hash Lookup", color=0xC60000)

        if not entry["results"]:
            embed.add_field(name="Error", value="No Results", inline=False)
        else:
            for y in range(len(entry["results"])):
                result = entry["results"][y]
                if not result["string"]:
                    embed.add_field(
                        name="{}.{}".format(result["hash"], result["type"]),
                        value="Unknown string",
                        inline=False,
                    )
                else:
                    embed.add_field(
                        name="{}.{}".format(result["hash"], result["type"]),
                        value="`" + "{}".format(result["string"]) + "`",
                        inline=False,
                    )

        embed.set_footer(text="Powered by https://hitmandb.notex.app")

        embed1 = await ctx.reply(embed=embed)
        await embed1.add_reaction("◀️")
        await embed1.add_reaction("❌")
        await embed1.add_reaction("▶️")

        def check(reaction, user):
            return (
                reaction.message.id == embed1.id
                and user == ctx.author
                and str(reaction.emoji) in ["◀️", "❌", "▶️"]
            )

        while True:
            try:
                reaction, user = await ctx.bot.wait_for(
                    "reaction_add", timeout=30, check=check
                )

                if str(reaction.emoji) == "▶️" and entry["results"]:
                    pagenumber += 1
                    reqJson = {
                        "search_term": string,
                        "number_of_results": 10,
                        "resource_type": resourcetype,
                        "page_number": pagenumber,
                    }

                    response = requests.post(url, json=reqJson)
                    data = response.json()
                    entry = data

                    embed = discord.Embed(title="Hash Lookup", color=0xC60000)

                    if not entry["results"]:
                        embed.add_field(name="Error", value="No Results", inline=False)
                    else:
                        for y in range(len(entry["results"])):
                            result = entry["results"][y]
                            if not result["string"]:
                                embed.add_field(
                                    name="{}.{}".format(result["hash"], result["type"]),
                                    value="Unknown string",
                                    inline=False,
                                )
                            else:
                                embed.add_field(
                                    name="{}.{}".format(result["hash"], result["type"]),
                                    value="`" + "{}".format(result["string"]) + "`",
                                    inline=False,
                                )

                    embed.set_footer(
                        text=f"Powered by https://hitmandb.notex.app - Page {pagenumber}"
                    )
                    await embed1.edit(embed=embed)
                    await embed1.remove_reaction(reaction, user)

                elif str(reaction.emoji) == "◀️" and pagenumber > 0:
                    pagenumber -= 1
                    reqJson = {
                        "search_term": string,
                        "number_of_results": 10,
                        "resource_type": resourcetype,
                        "page_number": pagenumber,
                    }

                    response = requests.post(url, json=reqJson)
                    data = response.json()
                    entry = data

                    embed = discord.Embed(title="Hash Lookup", color=0xC60000)

                    if not entry["results"]:
                        embed.add_field(name="Error", value="No Results", inline=False)
                    else:
                        for y in range(len(entry["results"])):
                            result = entry["results"][y]
                            if not result["string"]:
                                embed.add_field(
                                    name="{}.{}".format(result["hash"], result["type"]),
                                    value="Unknown string",
                                    inline=False,
                                )
                            else:
                                embed.add_field(
                                    name="{}.{}".format(result["hash"], result["type"]),
                                    value="`" + "{}".format(result["string"]) + "`",
                                    inline=False,
                                )

                    embed.set_footer(
                        text=f"Powered by https://hitmandb.notex.app - Page {pagenumber}"
                    )
                    await embed1.edit(embed=embed)
                    await embed1.remove_reaction(reaction, user)

                elif str(reaction.emoji) == "❌":
                    await embed1.delete()

            except asyncio.TimeoutError:
                try:
                    await embed1.clear_reactions()
                    break
                except Exception:
                    break
                # ending the loop if user doesn't react after x seconds
