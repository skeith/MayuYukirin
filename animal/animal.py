# Post animal pics by Eslyium#1949 & Yukirin#0048

# Discord
import discord

# Red
from redbot.core import commands

# Libs
import aiohttp

cat = "http://random.cat/meow"
dog = "https://dog.ceo/api/breeds/image/random"
fox = "http://wohlsoft.ru/images/foxybot/randomfox.php"
pug = "http://pugme.herokuapp.com/random"

BaseCog = getattr(commands, "Cog", object)

class Animal(BaseCog):
    """Animal commands."""

    def __init__(self, bot):
        self.session = aiohttp.ClientSession()
        self.cat = cat
        self.dog = dog
        self.fox = fox
        self.pug = pug

    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.guild)
    async def cat(self):
        """Shows a cat"""
        try:
            async with self.session.get(self.cat) as r:
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
                async with self.session.get(self.cat) as r:
                    api_result = await r.json()
                    results.append(api_result['file'])
            await ctx.send("\n".join(results))
        except:
            await ctx.send("API Error")

    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.guild)
    async def dog(self):
        """Shows a dog"""
        try:
            async with self.session.get(self.dog) as r:
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
                async with self.session.get(self.dog) as r:
                    api_result = await r.json()
                    results.append(api_result['message'])
            await ctx.send("\n".join(results))
        except:
            await ctx.send("API Error")

    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.guild)
    async def fox(self):
        """Shows a fox"""
        try:
            async with self.session.get(self.fox) as r:
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
                async with self.session.get(self.fox) as r:
                    api_result = await r.json()
                    results.append(api_result['file'])
            await ctx.send("\n".join(results))
        except:
            await ctx.send("API Error")

    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.guild)
    async def pug(self):
        """Shows a pug"""
        try:
            async with self.session.get(self.pug) as r:
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
                async with self.session.get(self.pug) as r:
                    api_result = await r.json()
                    results.append(api_result['pug'])
            await ctx.send("\n".join(results))
        except:
            await ctx.send("API Error")

