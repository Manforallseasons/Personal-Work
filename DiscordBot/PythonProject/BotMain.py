import discord
import random
from datetime import datetime

from GetResponses import parse_message
from GetInterjections import random_interjection

phase = int


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    time = datetime.now()

    if time.hour < 12:
        phase = 1
    elif time.hour < 15:
        phase = 2
    elif time.hour < 19:
        phase = 3
    else:
        phase = 4

    if client.user in message.mentions:
        response = parse_message(message, phase)
        if response:
            await message.reply(response)
    else:
        if random.randint(0, 100) < 5:
            await message.reply(random_interjection(phase))

client.run('')