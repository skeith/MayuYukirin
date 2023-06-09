from .animal import Animal


async def setup(bot):
    await bot.add_cog(Animal(bot))
