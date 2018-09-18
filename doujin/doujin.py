# Post random doujin pics by Eslyium#1949 & Yukirin#0048

# Discord
import discord

# Red
from redbot.core import commands

# Libs
import aiohttp


class Doujin:
    """Doujin commands."""

    def __init__(self, bot):
        self.session = aiohttp.ClientSession()

    @commands.group()
    async def doujin(self, ctx):
        """Doujin commands"""
        pass

    @doujin.command(no_pm=True)
    async def nhentai(self, ctx):
        """Sends a random doujin"""

        channel_nsfw = await self.is_nsfw(ctx.message.channel)
        if not channel_nsfw:
            return
        else:
            url = "http://nhentai.net/random/"
            async with self.session.get(url) as r:
                await ctx.send(r.url)
			
    @doujin.command(no_pm=True)
    async def tsumino(self, ctx):
        """Sends a random doujin"""

        channel_nsfw = await self.is_nsfw(ctx.message.channel)
        if not channel_nsfw:
            return
        else:
            url = "http://www.tsumino.com/Browse/Random"
            async with self.session.get(url) as r:
                await ctx.send(r.url)
			
    @doujin.command(no_pm=True)
    async def hbrowse(self, ctx):
        """Sends a random doujin"""

        channel_nsfw = await self.is_nsfw(ctx.message.channel)
        if not channel_nsfw:
            return
        else:
            url = "http://www.hbrowse.com/random"
            async with self.session.get(url) as r:
                await ctx.send(r.url)

    async def is_nsfw(self, channel: discord.abc.GuildChannel):
        try:
            _gid = channel.guild.id
        except AttributeError:
            return False
        data = await self.bot.http.request(
            discord.http.Route(
                'GET', '/guilds/{guild_id}/channels', guild_id=_gid))
        channeldata = [d for d in data if d['id'] == channel.id][0]
        return channeldata['nsfw']
