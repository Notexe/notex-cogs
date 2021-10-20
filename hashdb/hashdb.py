from discord.ext.commands.help import Paginator
from redbot.core import commands
from random import randrange
import discord
import requests
import random
import hashlib
import crcengine
import json

class HashDB(commands.Cog):
    async def red_delete_data_for_user(self, **kwargs):
        """Nothing to delete"""
        return
    @commands.command()
    async def hashdb(self, ctx, string, resourcetype: str = "any"):

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
            embed.add_field(name="Error", value="No Results", inline=False)
        else:
            for y in range(len(entry['results'])):
                result = entry['results'][y]
                if not result['string']:
                    embed.add_field(name='{}.{}'.format(
                        result['hash'], result['type']), value="Unknown string", inline=False)
                else:
                    embed.add_field(name='{}.{}'.format(
                        result['hash'], result['type']), value="`" + '{}'.format(result['string']) + "`", inline=False)

        embed.set_footer(text="Powered by https://hitmandb.notex.app")
        await ctx.reply(embed=embed)

    @commands.command()
    async def md5(self, ctx, string):
        if string:
            md5Result = hashlib.md5(string.encode(
                'utf-8').lower()).hexdigest().upper()
            embedMD5 = discord.Embed(title="MD5 Hash", color=0xC60000)
            embedMD5.add_field(name=string.lower(),
                               value="00" + md5Result[2:16], inline=False)
            await ctx.reply(embed=embedMD5)
        else:
            embedNoString = discord.Embed(title="MD5 Hash", color=0xC60000)
            embedNoString.add_field(
                name="Error", value="Please enter a string", inline=False)
            await ctx.reply(embed=embedNoString)

    @commands.command()
    async def id(self, ctx: commands.Context, version=None):
        def random_with_N_digits(n):
            range_start = 10**(n-1)
            range_end = (10**n)-1
            return randrange(range_start, range_end)

        if not version:
            await ctx.reply("**Error:** ID version required\nAllowed versions: official or peacock")
            return
        try:
            version = str(version)
            if version not in ["official", "peacock"]:
                raise ValueError
        except (ValueError, TypeError):
            await ctx.reply(
                f"**Error:** Invalid version {version}." + " Allowed versions: official or peacock"
            )
            return
        if version == "official":
            await ctx.reply("ID: 1-" + str(random_with_N_digits(2)) + "-" + str(random_with_N_digits(6)) + "-" + str(random_with_N_digits(2)))
        if version == "peacock":
            await ctx.reply("ID: 0-" + str(random_with_N_digits(2)) + "-" + str(random_with_N_digits(6)) + "-" + str(random_with_N_digits(2)))

    @commands.command()
    async def crc32(self, ctx, string):
        if string:
            crc_algorithm = crcengine.new('crc32')
            crc32Result = crc_algorithm(string.encode('utf-8'))
            crc32ResultHex = hex(crc32Result)[2:].upper()
            embedCRC32 = discord.Embed(title="CRC32 Hash", color=0xC60000)
            embedCRC32.add_field(name="Decimal:", value=crc32Result, inline=False)
            embedCRC32.add_field(name="Hexadecimal:", value=crc32ResultHex, inline=False)
            await ctx.reply(embed=embedCRC32)
        else:
            embedNoString = discord.Embed(title="CRC32 Hash", color=0xC60000)
            embedNoString.add_field(
                name="Error", value="Please enter a string", inline=False)
            await ctx.reply(embed=embedNoString)