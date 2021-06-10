import discord
import os

from discord.ext import commands, tasks
from itertools import cycle

from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Hello. I am alive!"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()


my_secret = os.environ['TOKEN']
client = discord.Client()

status = cycle(['I am dominator','Try `$ hi(none)` on my DM'])


@client.event
async def on_ready():
    change_status.start()
    print('We have logged in as {0.user}'.format(client))

@tasks.loop(seconds=360)
async def change_status():
  await client.change_presence(activity=discord.Game(next(status)))



@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$'):
        # prepares the input commands
        command_line = message.content
        command_line = command_line.replace('$', "").replace(" ", "").replace("()", "(none)")

        from parse_find_package.parse_func import parse_functions
        from parse_find_package.find_com import find_command

        parsed_tree = parse_functions(command_line) # parses command
        
        from commands_package import command_functions as cf

        result_list = [] # creates raw output

        for item in parsed_tree:
          if type(item) == list:
            result_list.append(find_command("linear", [item], cf.key_list))
          else:
            result_list.append(item) 
        
        output = ""
        file_list = [] # outputs

        for item in result_list: # creates the outputs
          output += str(item) + "\n"
          if type(item) == discord.file.File:
            file_list.append(item) 


        await message.channel.send(output) # send the text

        for file_item in file_list: # send the files
          await message.channel.send(file=file_item)
      
    if len(message.mentions) > 0:
        
        for item in message.mentions:
          if item.id == client.user.id:
            await message.channel.send("Try: ```$ commands(none)```")
      
    # else:
    #   # history = open('history.txt', 'a')
    #   # history.write('\n' + message.content + '\t' + message.author.name + '\t' + str(message.author.id))
    #   # history.close()
    #   print(message.content)

      



keep_alive()

client.run(os.getenv('TOKEN'))