from redbot.core import commands
import discord
import requests
import random
import hashlib
import re

class HashDB(commands.Cog):
    @commands.command()
    async def hashdb(self, ctx, string, resourcetype: str="any"):
        async def reWriteString (res):
            newStr = res.split('.', 1)
            try:
              firstSection = newStr[0].upper()
              splitSecondSection = newStr[1].split(',', maxsplit=1)
              secondSection = splitSecondSection[0].upper()
              thirdSectionSplit = splitSecondSection[1].split('|')
              thirdSection = thirdSectionSplit[0]
            except:
              firstSection = ""
              secondSection = ""
              thirdSection = ""
    
            d = dict()
            d['firstSection'] = firstSection
            d['secondSection'] = secondSection
            d['thirdSection'] = thirdSection
            arrOfMessages.append(d)
            
            global embed
            embed = discord.Embed(title="Hash Lookup", color=0xC60000)
            for msg in arrOfMessages:
                embed.add_field(name=msg.get('firstSection') + '.' + msg.get('secondSection'), value="`" + msg.get('thirdSection') + "`", inline=False)
                embed.set_footer(text="Powered by https://hitmandb.notex.app")
        
        emoji = ["<:rocco:823028032012025906>", "<:RoccoPog:837680147729088532>", "<:peepoSSip:836956012974964767>", "<:nightmare_47_mk2:834782513083449354>", "<:ioimoment:828451959283384351>", "<:LUL:759564041965666356>", "<:KEK:837936832373194812>", "<:gigachad47_R:835110788560584735>", "<:gigachad47_L:835110791060652052>", "<:cursed_47:835098987991269376>", "<:47what:836242357426585691>", "<:47ohshit:836567510345187348>", "<:47angry:836567784766308352>", "<:GWseremePeepoLife:838766302263902219>", "<:mario_smug:836540135692697611>", "<:mario_47_cursed:836239391454134373>", "These are not the hashes you're looking for", "The hashes are in another castle!"]

        url = "https://hitmandb.notex.app/search"
        data = string
        data2 = resourcetype
        dataSub = ","
        if dataSub in data:
          string.split(',', maxsplit=1)
          data = string[0]
        else:
          data = string
        params = data + ",10," + data2.lower() + ",0"
        r = requests.post(url, data = params)
        if re.search(r'^10.*\|', r.text):
          embedNoResult = discord.Embed(title="Hash Lookup", color=0xC60000)
          embedNoResult.add_field(name="No Results", value=random.choice(emoji), inline=False)
          embedNoResult.set_footer(text="Powered by https://hitmandb.notex.app")
          await ctx.send(embed=embedNoResult)
        else:
          arrOfMessages = []
          multiStr = r.text.split('|')
          del multiStr[-1]
          del multiStr[-1]
          totalRes = len(multiStr)
          for i in multiStr:
            await reWriteString(i)
          await ctx.send(embed=embed)

    @commands.command()
    async def md5(self, ctx, string):
      if string:
        md5Result = hashlib.md5(string.encode('utf-8').lower()).hexdigest().upper()
        embedMD5 = discord.Embed(title="MD5 Hash", color=0xC60000)
        embedMD5.add_field(name=string.lower(), value="00" + md5Result[2:16], inline=False)
        await ctx.send(embed=embedMD5)
      else:
        embedNoString = discord.Embed(title="MD5 Hash", color=0xC60000)
        embedNoString.add_field(name="No string inputted", value="<:GWseremePeepoLife:838766302263902219>", inline=False)
        await ctx.send(embed=embedNoString)