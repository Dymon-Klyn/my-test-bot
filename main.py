import os
import aiohttp
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = commands.Bot(command_prefix="!")


@bot.command(name="info")

async def info(ctx, *args: str):
    client_id = "4SJkTSHGOB"
    game = " ".join(args)
    url = f"https://www.boardgameatlas.com/api/search?name={game}&client_id={client_id}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            cont = await resp.json()
            await ctx.send(cont["games"][0]["description"])

bot.run(TOKEN)
