import discord
import os
from dotenv import load_dotenv
from neuralintents import GenericAssistant

client = discord.Client()
load_dotenv()
TOKEN = os.getenv('TOKEN')

@client.envt
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith("#aibot"):
        pass

client.run(TOKEN)