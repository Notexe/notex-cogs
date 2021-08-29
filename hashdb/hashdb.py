from redbot.core import commands
from random import randrange
from dislash import *
import discord
import requests
import random
import hashlib
import json


class HashDB(commands.Cog):
    @commands.command()
    async def hashdb(self, ctx, string, resourcetype: str = "any"):

        emoji = [
            "<:47Angry:836567784766308352>",
            "<:47Constipated:846427458872803328>",
            "<:47OhShit:836567510345187348>",
            "<:47Stare:842321510835814442>",
            "<:47What:836242357426585691>",
            "<:abrakHelicopter:855422380183519243>",
            "<:angrydoggo:861855672232706058>",
            "<:bruh:854676551407501312>",
            "<:cateeth:859053529200459776>",
            "<:cursed47:835098987991269376>",
            "<:drunkDiana:842322054484328448>",
            "<:gigachad47_L:835110791060652052>",
            "<:gigachad47_R:835110788560584735>",
            "<:glonk_47:848759340588073000>",
            "<:goose_stab:862723944217182238>",
            "<:GWseremePeepoLife:838766302263902219>",
            "<:GWseremePeepoThink:861856123795800103>",
            "<:GWvertiPeepoChrist:851983156373487646>",
            "<:hakan:855418090220683304>",
            "<:hihi:859053465007554571>",
            "<:ioiMoment:828451959283384351>",
            "<:KEK:837936832373194812>",
            "<:kevin:855406759018758174>",
            "<:LUL:759564041965666356>",
            "<:lulAgony:847506792498200586>",
            "<:mario47Cursed:836239391454134373>",
            "<:marioSmug:836540135692697611>",
            "<:misinfo_47:855178644984168458>",
            "<:mkII:759684183131160576>",
            "<:mkIII:759684147215728710>",
            "<:mkIIWorn:759684167537000469>",
            "<:peepoEvol:855404692494745610>",
            "<:peepoMad:857237684288618508>",
            "<:peepoMadTongue:857660298546511884>",
            "<:peepoPizza2:856816884485455892>",
            "<:peepoSSip:836956012974964767>",
            "<:rocco:823028032012025906>",
            "<:roccoCringe:842692483972333571>",
            "<:roccoCringeC:844205348368941086>",
            "<:RoccoPog:837680147729088532>",
            "<:roccoSmile:847514780913762345>",
            "<:roccoSmile2:847514795192352778>",
            "<:roccoThink:859039772725870633>",
            "<:rpkg:849257066228744264>",
            "<:SodersStare:862548891696889877>",
            "<:TheCoolestNabeel:863560511697321995>",
            "<:Wut:861165804166578176>",
            "These are not the hashes you're looking for",
            "The hashes are in another castle!"
        ]

        url = "https://hitmandb.notex.app/search"

        reqJson = {
            "search_term": string,
            "number_of_results": 10,
            "resource_type": resourcetype,
            "page_number": 0
        }

        response = requests.post(url, json=reqJson)
        data = response.json()
        entry = data

        embed = discord.Embed(title="Hash Lookup", color=0xC60000)

        if (not entry["results"]):
            embed.add_field(name="No Results",
                            value=random.choice(emoji), inline=False)
        else:
            for y in range(len(entry['results'])):
                result = entry['results'][y]
                embed.add_field(name='{}.{}'.format(
                    result['hash'], result['type']), value="`" + '{}'.format(result['string']) + "`", inline=False)

        embed.set_footer(text="Powered by https://hitmandb.notex.app")
        await ctx.send(embed=embed)

    @commands.command()
    async def md5(self, ctx, string):
        if string:
            md5Result = hashlib.md5(string.encode(
                'utf-8').lower()).hexdigest().upper()
            embedMD5 = discord.Embed(title="MD5 Hash", color=0xC60000)
            embedMD5.add_field(name=string.lower(),
                               value="00" + md5Result[2:16], inline=False)
            await ctx.send(embed=embedMD5)
        else:
            embedNoString = discord.Embed(title="MD5 Hash", color=0xC60000)
            embedNoString.add_field(
                name="No string inputted", value="<:GWseremePeepoLife:838766302263902219>", inline=False)
            await ctx.send(embed=embedNoString)

    @commands.command()
    async def id(self, ctx: commands.Context, version=None):
        def random_with_N_digits(n):
            range_start = 10**(n-1)
            range_end = (10**n)-1
            return randrange(range_start, range_end)

        if not version:
            await ctx.send("**Error:** ID version required\nAllowed versions: official or peacock")
            return
        try:
            version = str(version)
            if version not in ["official", "peacock"]:
                raise ValueError
        except (ValueError, TypeError):
            await ctx.send(
                f"**Error:** Invalid version {version}." + " Allowed versions: official or peacock"
            )
            return
        if version == "official":
            await ctx.send("ID: 1-" + str(random_with_N_digits(2)) + "-" + str(random_with_N_digits(6)) + "-" + str(random_with_N_digits(2)))
        if version == "peacock":
            await ctx.send("ID: 0-" + str(random_with_N_digits(2)) + "-" + str(random_with_N_digits(6)) + "-" + str(random_with_N_digits(2)))

    @commands.command()
    async def buttontest(self, ctx):
        row_of_buttons = [
            ActionRow(
                Button(
                    style=ButtonStyle.blurple,
                    label="Click",
                    # emoji=discord.PartialEmoji(name="\U0001faa8"),
                    custom_id="click",
                ),
            ),
        ]
        row_of_buttons1 = [
            ActionRow(
                Button(
                    style=ButtonStyle.blurple,
                    label="Click",
                    # emoji=discord.PartialEmoji(name="\U0001faa8"),
                    custom_id="click1",
                ),
            ),
        ]
        row_of_buttons2 = [
            ActionRow(
                Button(
                    style=ButtonStyle.blurple,
                    label="Click",
                    # emoji=discord.PartialEmoji(name="\U0001faa8"),
                    custom_id="click2",
                ),
            ),
        ]
        msg = await ctx.reply(
            "Button test thing",
            components=row_of_buttons,
            mention_author=False
        )

        on_click = msg.create_click_listener(timeout=60)
        
        @on_click.matching_id("click", cancel_others=True)
        async def buttonclick1(inter):
            await inter.reply(type=ResponseType.DeferredUpdateMessage)
            await msg.edit(
                content=f"You clicked the button, well done. I'm so proud.",
                components=row_of_buttons1,
            )

        @on_click.matching_id("click1", cancel_others=True)
        async def buttonclick2(inter):
            await inter.reply(type=ResponseType.DeferredUpdateMessage)
            await msg.edit(
                content=f"Why did you click the button again? Stop it.",
                components=row_of_buttons2,
            )

        @on_click.matching_id("click2", cancel_others=True)
        async def buttonclick2(inter):
            await inter.reply(type=ResponseType.DeferredUpdateMessage)
            await msg.edit(
                content=f"Stop, just stop.",
                components=None,
            )