import os
import aiohttp
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = commands.Bot(command_prefix="!")


@bot.command(name="bgame", help="returns a description about a given boardgame")
async def game_description(ctx, *args: str):
    client_id = "4SJkTSHGOB"
    game = " ".join(args)
    url = f"https://www.boardgameatlas.com/api/search?name={game}&client_id={client_id}&fuzzy_match=true"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            try:
                cont = await resp.json()
                if cont["games"]:
                    text = cont["games"][0]["description_preview"]
                    await ctx.send(f"```{text}```")
                else:
                    raise KeyError
            except KeyError:
                await ctx.send("```game not found...```")


@bot.command(name="bgame_info", help="returns information about a given boardgame")
async def game_info(ctx, *args: str):
    client_id = "4SJkTSHGOB"
    game = " ".join(args)
    url = f"https://www.boardgameatlas.com/api/search?name={game}&client_id={client_id}&fuzzy_match=true"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            try:
                cont = await resp.json()
                if cont["games"]:
                    min_p = cont["games"][0]["min_players"]
                    max_p = cont["games"][0]["max_players"]
                    min_play = cont["games"][0]["min_playtime"]
                    max_play = cont["games"][0]["max_playtime"]
                    rules = cont["games"][0]["rules_url"]
                    await ctx.send(f"```players: {min_p} to {max_p}\nplaytime: {min_play} to {max_play} minutes\nrules: ```{rules}")
                else:
                    raise KeyError
            except KeyError:
                await ctx.send("```game not found...```")

bot.run(TOKEN)
