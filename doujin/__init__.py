from .doujin import Doujin


async def setup(bot):
    await bot.add_cog(Doujin(bot))
