# Post animal pics by Eslyium#1949 & Yukirin#0048

# Discord
import discord

# Red
from redbot.core import commands

# Libs
import aiohttp

BaseCog = getattr(commands, "Cog", object)


class Animal(BaseCog):
    """Animal commands."""

    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession()
        self.catapi = "https://shibe.online/api/cats"
        self.dogapi = "https://dog.ceo/api/breeds/image/random"
        self.foxapi = "http://wohlsoft.ru/images/foxybot/randomfox.php"
        self.roarapi = "http://randombig.cat/roar.json"
        self.dog_breed_api = "https://dog.ceo/api/breed/{}/images/random"
        self.error_message = "An API error occured. Probably just a hiccup.\nIf this error persist for several days, please report it."

    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.guild)
    async def cat(self, ctx):
        """Shows a cat"""
        try:
            async with self.session.get(self.catapi) as r:
                result = await r.json()
            await ctx.send(result[0])
        except:
            await ctx.send(self.error_message)

    @commands.command()
    @commands.cooldown(1, 120, commands.BucketType.guild)
    async def cats(self, ctx, amount : int = 5):
        """Throws a cat bomb!

        Defaults to 5, max is 10"""
        results = []
        if amount > 10 or amount < 1:
            amount = 5
        try:
            for x in range(0,amount):
                async with self.session.get(self.catapi) as r:
                    api_result = await r.json()
                    results.append(api_result[0])
            await ctx.send("\n".join(results))
        except:
            await ctx.send(self.error_message)

    @commands.commands()
    @commands.cooldown(1, 60, commands.BucketType.guild)
    async def dog(self, ctx, breed: str):
        """Shows a breed of dog.
        
        Use the breed argument to display a specific breed of dog.
        You can provide random for a random breed.
        """
        if breed.lower() == "random":
            api = self.dogapi
        else:
            api = self.dog_breed_api.format(breed)
        try:
            async with self.session.get(api) as r:
                result = await r.json()
            await ctx.send(result['message'])
        except Exception:
            await ctx.send(self.error_message)

    @commands.command()
    @commands.cooldown(1, 120, commands.BucketType.guild)
    async def dogs(self, ctx, amount : int = 5):
        """Throws a dog bomb!

        Defaults to 5, max is 10"""
        results = []
        if amount > 10 or amount < 1:
            amount = 5
        try:
            for x in range(0,amount):
                async with self.session.get(self.dogapi) as r:
                    api_result = await r.json()
                    results.append(api_result['message'])
            await ctx.send("\n".join(results))
        except:
            await ctx.send(self.error_message)

    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.guild)
    async def fox(self, ctx):
        """Shows a fox"""
        try:
            async with self.session.get(self.foxapi) as r:
                result = await r.json()
            await ctx.send(result['file'])
        except:
            await ctx.send(self.error_message)

    @commands.command()
    @commands.cooldown(1, 120, commands.BucketType.guild)
    async def foxes(self, ctx, amount : int = 5):
        """Throws a fox bomb!

        Defaults to 5, max is 10"""
        results = []
        if amount > 10 or amount < 1:
            amount = 5
        try:
            for x in range(0,amount):
                async with self.session.get(self.foxapi) as r:
                    api_result = await r.json()
                    results.append(api_result['file'])
            await ctx.send("\n".join(results))
        except:
            await ctx.send(self.error_message)

    @commands.command()
    @commands.cooldown(1, 120, commands.BucketType.guild)
    async def pugs(self, ctx, amount : int = 5):
        """Throws a pugs bomb!

        Defaults to 5, max is 10"""
        results = []
        if amount > 10 or amount < 1:
            amount = 5
        try:
            for x in range(0,amount):
                async with self.session.get(self.pugapi) as r:
                    api_result = await r.json()
                    results.append(api_result['message'])
            await ctx.send("\n".join(results))
        except:
            await ctx.send(self.error_message)

    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.guild)
    async def bigcat(self, ctx):
        """Shows a bigcat"""
        try:
            async with self.session.get(self.roarapi) as r:
                result = await r.json()
            await ctx.send(result['url'])
        except:
            await ctx.send(self.error_message)

    @commands.command()
    @commands.cooldown(1, 120, commands.BucketType.guild)
    async def bigcats(self, ctx, amount : int = 5):
        """Throws a bigcats bomb!
        Defaults to 5, max is 10"""
        results = []
        if amount > 10 or amount < 1:
            amount = 5
        try:
            for x in range(0,amount):
                async with self.session.get(self.roarapi) as r:
                    api_result = await r.json()
                    results.append(api_result['url'])
            await ctx.send("\n".join(results))
        except:
            await ctx.send(self.error_message)

    def cog_unload(self):
        self.bot.loop.create_task(self.session.close())

    __del__ = cog_unload
