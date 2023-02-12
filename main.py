import discord
import os
from dotenv import load_dotenv
from neuralintents import GenericAssistant

# Train model on intents file
chatbot = GenericAssistant('intents.json')
chatbot.train_model()
chatbot.save_model()

print("AI Bot running...")

# Create discord client
client = discord.Client()

# Load bot token
load_dotenv()
TOKEN = os.getenv('TOKEN')

# Listen for incoming messages
@client.envt
async def on_message(message):
    if message.author == client.user:
        return
    
    # If message starts with '$aibot' then respond
    if message.content.startswith("$aibot"):
        # Cut off first 7 characters to ignore '$aibot ' 
        response  = chatbot.request(message.content[7:])
        await message.channel.send(response)

# Call that runs client
client.run(TOKEN)