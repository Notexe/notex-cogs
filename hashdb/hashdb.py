from discord.ext.commands import bot
from discord.ext.commands.help import Paginator
from redbot.core import commands, app_commands
from redbot.core.bot import Red
from redbot.core.i18n import Translator, cog_i18n
import asyncio
import discord
import requests

_ = Translator("Converters", __file__)

@cog_i18n(_)
class HashDB(commands.Cog):
    """HashDB Cog"""
    def __init__(self, bot: Red):
        self.bot = bot

    async def red_delete_data_for_user(self, **kwargs):
        """Nothing to delete"""
        return

    @commands.hybrid_command()
    async def hashdb(self, ctx: commands.Context, string, resourcetype: str = "any", numberofresults: int = 10):
        """
        Searches for a hash using hitmandb.glaciermodding.org

        Parameters
        ----------
        string : str
            The hash or path to search for.
        
        resourcetype : str
            The type of resource to search for.
            Valid options are:
            - `any` and all the formats located at https://wiki.glaciermodding.org/glacier2/fileformats
        
        numberofresults : int
            The number of results to return.

        Usage:
        `[p]hashdb <string> [Resource Type] [Number of results]`
        """
        if numberofresults < 0:
            await ctx.reply("Negative number of results is not allowed.")
        elif numberofresults > 30:
            await ctx.reply("Number of results cannot exceed 30.")
            return
        else:
            url = "https://hitmandb.glaciermodding.org/search"
            pagenumber = 0

            reqJson = {
                "search_term": string,
                "number_of_results": numberofresults,
                "resource_type": resourcetype,
                "page_number": pagenumber,
            }

            response = requests.post(url, json=reqJson)

            if response.status_code == 200:
                data = response.json()
                entry = data
            else:
                return await ctx.send(
                    "Something went wrong. Please try again later."
                )

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

            embed.set_footer(text="Powered by https://hitmandb.glaciermodding.org")

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
                            "number_of_results": numberofresults,
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
                            text=f"Powered by https://hitmandb.glaciermodding.org - Page {pagenumber}"
                        )
                        await embed1.edit(embed=embed)
                        try:
                            await embed1.remove_reaction(reaction, user)
                        except:
                            print("Missing permissions!")

                    elif str(reaction.emoji) == "◀️" and pagenumber > 0:
                        pagenumber -= 1
                        reqJson = {
                            "search_term": string,
                            "number_of_results": numberofresults,
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
                            text=f"Powered by https://hitmandb.glaciermodding.org - Page {pagenumber}"
                        )
                        await embed1.edit(embed=embed)
                        try:
                            await embed1.remove_reaction(reaction, user)
                        except:
                            print("Missing permissions!")

                    elif str(reaction.emoji) == "❌":
                        await embed1.delete()

                except asyncio.TimeoutError:
                    try:
                        await embed1.clear_reactions()
                        break
                    except Exception:
                        break
                    # ending the loop if user doesn't react after x seconds
