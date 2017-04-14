import discord
import datetime
import asyncio
import logging
from credentials import token
import RoleManagement

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as ')
    print(client.user.name)
    print(client.user.id)
    print(datetime.datetime.now())
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('+!'):
        RoleManagement.assign_role(message)

client.run(token())