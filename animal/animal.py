# Post animal pics by Eslyium#1949 & Yukirin#0048

# Discord
import discord

# Red
from redbot.core import commands

# Libs
import aiohttp

catapi = "http://aws.random.cat/meow"
dogapi = "https://dog.ceo/api/breeds/image/random"
foxapi = "http://wohlsoft.ru/images/foxybot/randomfox.php"
pugapi = "http://pugme.herokuapp.com/random"

BaseCog = getattr(commands, "Cog", object)


class Animal(BaseCog):
    """Animal commands."""

    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession(loop=self.bot.loop)
        self.catapi = catapi
        self.dogapi = dogapi
        self.foxapi = foxapi
        self.pugapi = pugapi

    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.guild)
    async def cat(self, ctx):
        """Shows a cat"""
        try:
            async with self.session.get(self.catapi) as r:
                result = await r.json()
            await ctx.send(result['file'])
        except:
            await ctx.send("API Error")

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
                    results.append(api_result['file'])
            await ctx.send("\n".join(results))
        except:
            await ctx.send("API Error")

    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.guild)
    async def dog(self, ctx):
        """Shows a dog"""
        try:
            async with self.session.get(self.dogapi) as r:
                result = await r.json()
            await ctx.send(result['message'])
        except:
            await ctx.send("API Error")

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
            await ctx.send("API Error")

    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.guild)
    async def fox(self, ctx):
        """Shows a fox"""
        try:
            async with self.session.get(self.foxapi) as r:
                result = await r.json()
            await ctx.send(result['file'])
        except:
            await ctx.send("API Error")

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
            await ctx.send("API Error")

    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.guild)
    async def pug(self, ctx):
        """Shows a pug"""
        try:
            async with self.session.get(self.pugapi) as r:
                result = await r.json()
            await ctx.send(result['pug'])
        except:
            await ctx.send("API Error")

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
                    results.append(api_result['pug'])
            await ctx.send("\n".join(results))
        except:
            await ctx.send("API Error")

    def __unload(self):
        self.bot.loop.create_task(self.session.close())

    __del__ = __unload
