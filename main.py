import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = commands.Bot(command_prefix="!")


@bot.command(name="info")
async def info(ctx):
    await ctx.send("working on it...")

bot.run(TOKEN)
