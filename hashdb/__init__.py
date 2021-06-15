from .hashdb import HashDB


def setup(bot):
    bot.add_cog(HashDB())