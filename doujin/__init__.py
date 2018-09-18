from .doujin import Doujin


def setup(bot):
    bot.add_cog(Doujin(bot))
