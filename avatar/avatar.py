# Simple avatar URL fetch by Yukirin#0048

# Discord
import discord

# Red
from redbot.core import commands


class Avatar(commands.Cog):
    """Get user's avatar URL."""

    @commands.command()
    async def avatar(self, ctx, *, user: discord.Member=None):
        """Returns user avatar URL.

        User argument can be user mention, nickname, username, user ID.
        Default to yourself when no argument is supplied.
        """
        author = ctx.author

        if not user:
            user = author

        url = user.avatar.with_static_format("png")

        await ctx.send(f"{user}'s Avatar URL : {url}")
