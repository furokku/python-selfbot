#!/usr/bin/env python3
import os
import discord

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        invite = 'your message here'
       
    if message.content == 'start.spam@self':
        response = message
        while 3 < 4:
            await message.channel.send(response)
TOKEN = 'paste-here'
client.run(TOKEN, bot=False)