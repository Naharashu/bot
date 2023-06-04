import disnake

from disnake.ext import commands

import json

import random

intents = disnake.Intents.all()

bot = commands.Bot(command_prefix="your_prefix", intents=intents)

@bot.event

async def on_ready():

  print("Bot is ready!")

@bot.slash_command(description="сказати від імені бота")

async def say(inter, message: str):

  await inter.response.send_message(message)

@bot.slash_command(description="аватар")

async def avatar(inter, user: disnake.User):

  await inter.response.send_message(user.display_avatar)

@bot.command()

async def say(ctx, *,message):

   await ctx.send(message)

@bot.slash_command(description="рандомайзер чисел")

async def rand(inter, arg1: int, arg2: int):

  await inter.response.send_message(random.randint(arg1, arg2))

@bot.slash_command()

async def ping(inter):

  await inter.response.send_message(f"{round(bot.latency * 1000)}ms")

@bot.slash_command(description="список команд")

async def help(inter):

  emb = disnake.Embed(title="Допомога", description="**Основні:** help, avatar, ping, rand, say")

  await inter.response.send_message(embed=emb)

	  bot.run("ваш токен")
