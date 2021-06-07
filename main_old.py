
# from command_functions import find_command

# import discord
# import os

# from discord.ext import commands, tasks
# from itertools import cycle

# from flask import Flask
# from threading import Thread

# app = Flask('')

# @app.route('/')
# def home():
#     return "Hello. I am alive!"

# def run():
#   app.run(host='0.0.0.0',port=8080)

# def keep_alive():
#     t = Thread(target=run)
#     t.start()


# my_secret = os.environ['TOKEN']
# client = discord.Client()

# status = cycle(['I am dominator','Try `$ hi` on my DM'])


# @client.event
# async def on_ready():
#     change_status.start()
#     print('We have logged in as {0.user}'.format(client))

# @tasks.loop(seconds=360)
# async def change_status():
#   await client.change_presence(activity=discord.Game(next(status)))



# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     if message.content.startswith('$ '):
        
#         command_parameter = message.content.split(" ")

#         command_parameter.remove('$')

#         command = find_command(command_parameter[0])
#         command_parameter.pop(0)
        
#         output = command(command_parameter)
        
#         if type(output) == discord.file.File:
#           await message.channel.send(file=output)
#         else:
#           await message.channel.send(output)
      
#     if len(message.mentions) > 0:
        
#         for item in message.mentions:
#           if item.id == client.user.id:
#             await message.channel.send("Try: ```$ hi```")
      
#     # else:
#     #   # history = open('history.txt', 'a')
#     #   # history.write('\n' + message.content + '\t' + message.author.name + '\t' + str(message.author.id))
#     #   # history.close()
#     #   print(message.content)

      



# keep_alive()

# client.run(os.getenv('TOKEN'))