token = "NTU0MjUxNjU3Mjc0MzI3MDUx.D2Z79g.RhHoP-Shd0P9ACLm88Wz6ZkuRg8"
prefix = "b"

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Botove i Servere"))
    print('Bot je spreman | Bot Developers')

@bot.command()
@commands.has_permissions(administrator=True)
async def say(ctx, *, content:str):
    await ctx.send(content)

bot.run(token)
