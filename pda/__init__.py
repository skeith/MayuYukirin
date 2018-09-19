from .pda import PDA


def setup(bot):
    bot.add_cog(PDA(bot))
