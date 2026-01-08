import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("Bot Online!")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🏓")

TOKEN = os.getenv("TOKEN")

if not TOKEN:
    print("TOKEN not found")
else:
    bot.run(TOKEN)
