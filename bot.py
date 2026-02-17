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
    if not TOKEN or TOKEN == 'YOUR_BOT_TOKEN_HERE':
        print("Error: DISCORD_TOKEN is missing or not set in .env file.")
    else:
        try:
            bot.run(TOKEN)
        except discord.errors.PrivilegedIntentsRequired:
            print("\n--- ERROR: PRIVILEGED INTENTS REQUIRED ---")
            print("Sizning botingizda 'Message Content Intent' yoqilmagan.")
            print("Iltimos, Discord Developer Portal (https://discord.com/developers/applications/) ga kiring:")
            print("1. Bot menyusini tanlang.")
            print("2. 'Privileged Gateway Intents' bo'limiga tushing.")
            print("3. 'Message Content Intent' ni YOQING (Switch on).")
            print("4. O'zgarishlarni saqlang (Save Changes) va botni qayta ishga tushiring.\n")
