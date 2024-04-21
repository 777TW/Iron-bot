import discord
intents = discord.Intents.all()
intents.members = True
from discord.ext import commands
import json
import os
import asyncio


with open(r"C:\Users\happy_\OneDrive\桌面\iron-bot\json\settings.json", 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix='$', help_command=None, intents=intents, application_id = "1118424692680822835")

@bot.event
async def on_ready():
    print(">> Bot is online <<")
    game = discord.Game("變硬")
    await bot.change_presence(status=discord.Status.online, activity = game)
                              
async def loads():
    for filename in os.listdir(r"C:\Users\happy_\OneDrive\桌面\iron-bot\categories"):
        if filename.endswith('.py'):
            await bot.load_extension(f'categories.{filename[:-3]}')

async def main():
    await loads()
    if __name__ == "__main__":
        await bot.start(jdata['token'])

asyncio.run(main())