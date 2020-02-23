# Post random doujin pics by Eslyium#1949 & Yukirin#0048

# Discord
import discord

# Red
from redbot.core import commands

# Libs
import aiohttp

BaseCog = getattr(commands, "Cog", object)


class Doujin(BaseCog):
    """Doujin commands."""

    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession(loop=self.bot.loop)

    @commands.group(autohelp=True)
    @commands.guild_only()
    @commands.is_nsfw()
    async def doujin(self, ctx):
        """Doujin commands"""
        pass

    @doujin.command()
    async def nhentai(self, ctx):
        """Sends a random doujin"""

        url = "http://nhentai.net/random/"
        async with self.session.get(url) as r:
            await ctx.send(r.url)
			
    @doujin.command()
    async def tsumino(self, ctx):
        """Sends a random doujin"""

        url = "http://www.tsumino.com/Browse/Random"
        async with self.session.get(url) as r:
            await ctx.send(r.url)
			
    @doujin.command()
    async def hbrowse(self, ctx):
        """Sends a random doujin"""

        url = "http://www.hbrowse.com/random"
        async with self.session.get(url) as r:
            await ctx.send(r.url)

    def cog_unload(self):
        self.bot.loop.create_task(self.session.close())

    __del__ = cog_unload
