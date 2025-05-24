#!/home/minoid/discord-bot/bin/python3
# -*- coding: utf-8 -*-

import discord
from discord import option

import dice

from dotenv import load_dotenv
import os
import random

load_dotenv()
TOKEN=os.getenv("DISCORD-TOKEN")

bot = discord.Bot()

error_messages = [
    "боги приключений собрались, чтобы понять что ты хотел кинуть",
    "мир смотрит на тебя с призрением, напиши нормальную формулу",
    "хи-хи-хи, где ты видел такую формулу?"
]

print("Hall0!")

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name="roll", description="Кинь меня! :3")
@option("exp", description="Выражение в виде: 2d20+5")
async def roll(ctx: discord.ApplicationContext, exp:str):
    respond = dice.pretty_roll(exp)
    if respond == "Error":
        error_message = f"-# {random.choice(error_messages)}"
        await ctx.respond(error_message)
    else:
        respond_message = f"## {ctx.author.display_name} кидает кубики и получает: {respond[1]}!\n\n> Формула: {exp.replace(' ','')}\n> Кубы: {respond[0]} = {respond[1]}"
        await ctx.respond(respond_message)

bot.run(TOKEN) 
