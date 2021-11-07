from redbot.core import commands
from redbot.core.bot import Red
from random import randrange

class ID(commands.Cog):
    def __init__(self, bot: Red):
        self.bot = bot

    async def red_delete_data_for_user(self, **kwargs):
        """Nothing to delete"""
        return

    @commands.command()
    async def id(self, ctx: commands.Context, version=None):
        def random_with_N_digits(n):
            range_start = 10 ** (n - 1)
            range_end = (10 ** n) - 1
            return randrange(range_start, range_end)

        if not version:
            await ctx.reply(
                "**Error:** ID version required\nAllowed versions: official or peacock"
            )
            return
        try:
            version = str(version)
            if version not in ["official", "peacock"]:
                raise ValueError
        except (ValueError, TypeError):
            await ctx.reply(
                f"**Error:** Invalid version {version}."
                + " Allowed versions: official or peacock"
            )
            return
        if version == "official":
            await ctx.reply(
                "ID: 1-"
                + str(random_with_N_digits(2))
                + "-"
                + str(random_with_N_digits(6))
                + "-"
                + str(random_with_N_digits(2))
            )
        if version == "peacock":
            await ctx.reply(
                "ID: 0-"
                + str(random_with_N_digits(2))
                + "-"
                + str(random_with_N_digits(6))
                + "-"
                + str(random_with_N_digits(2))
            )
