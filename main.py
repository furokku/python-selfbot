#!/usr/bin/env python3
import discord

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        if message.content == 'start.spam':
            response = 'your message here'
            while 3 < 4:
                await message.channel.send(response)
                
                
TOKEN = 'paste-here'
client.run(TOKEN, bot=False)
