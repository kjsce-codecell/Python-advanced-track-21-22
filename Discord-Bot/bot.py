import os
import random
import requests

from dotenv import load_dotenv
import discord
from discord.ext import commands
load_dotenv()

TOKEN = os.getenv("TOKEN")

bot = commands.Bot(command_prefix=("C ","c "),case_insensitive=True)

# toss
@bot.command(name="toss",help="tossing a coin")
async def toss(ctx,*args):
    await ctx.send("Coin landed on "+random.choice(["Head","Tail"]))

# pokedex
@bot.command(name="pokemon",aliases=["pok"],help="shows pokemon stats")
async def pokemon(ctx,name=None,*args):
    
    if name == None:
        await ctx.send("gimme pokemon name")
        return
    name=name.lower()
    r = requests.get("https://pokeapi.co/api/v2/pokemon/"+name)
    if r.status_code == 200:
        data = r.json()
        pokemon = {
            i["stat"]["name"]:str(i["base_stat"]) for i in data["stats"]
        }
        pokemon["types"] = ", ".join(map(lambda x:x["type"]["name"],data["types"]))
        pokemon["abilities"] = ", ".join(map(lambda x:x["ability"]["name"],data["abilities"]))
        des = "\n".join(k+" : "+v for k,v in pokemon.items())
        embed = discord.Embed(title=name,description=des,color=discord.Colour.random())
        embed.set_thumbnail(url=data["sprites"]["front_default"])
        await ctx.send(embed=embed)
    else:
        await ctx.send("that pokemon doesnt exist")

bot.run(TOKEN)

