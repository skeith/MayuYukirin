# Simple avatar URL fetch by Yukirin#0048

# Discord
import discord

# Red
from redbot.core import commands

# Libs
import re


def process_avatar(url):
    if ".gif" in url:
        new_url = re.sub("\?size\=\d+.*", "", url)
        return new_url
    else:
        new_url = url.replace('.webp', '.png')
        return new_url


class Avatar:
    """Get user's avatar URL."""

    @commands.command()
    async def avatar(self, ctx, *, user: discord.Member=None):
        """Returns user avatar URL."""
        author = ctx.author

        if not user:
            user = author

        u = user.avatar_url
        url = process_avatar(u)
        await ctx.send("{}'s Avatar URL : {}".format(user.name, url))
