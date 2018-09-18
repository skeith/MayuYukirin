from .animal import Animal


def setup(bot):
    bot.add_cog(Animal(bot))
