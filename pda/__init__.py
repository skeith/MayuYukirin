from .pda import PDA


async def setup(bot):
    await bot.add_cog(PDA(bot))
