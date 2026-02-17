import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}!')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command()
async def salom(ctx):
    await ctx.send('Assalomu alaykum! Botimizga xush kelibsiz.')

if __name__ == '__main__':
    if TOKEN and TOKEN != 'YOUR_BOT_TOKEN_HERE':
        bot.run(TOKEN)
    else:
        print("Error: DISCORD_TOKEN is missing or not set in .env file.")
