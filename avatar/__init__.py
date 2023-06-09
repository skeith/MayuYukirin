from .avatar import Avatar


async def setup(bot):
    await bot.add_cog(Avatar())
