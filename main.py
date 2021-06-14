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
  app.run(host='0.0.0.0', port=8080)


def keep_alive():
  t = Thread(target=run)
  t.start()


my_secret = os.environ['TOKEN']
client = commands.Bot(command_prefix="d")

status = cycle(['I am dominator', 'Try `$ hi(none)` on my DM'])


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

		parsed_tree = parse_functions(command_line)  # parses command

		from commands_package import command_functions as cf

		result_list = []  # creates raw output

		for item in parsed_tree:
			if type(item) == list:
				result_list.append(find_command("linear", [item],	cf.key_list))
			else:
				result_list.append(item)

		output = ""
		file_list = []  # outputs
		embed_list = []

		for item in result_list:  # creates the outputs, based on what type of objects we will receive
			output += '```\n' + str(item) + '\n```' + "\n"

			if type(item) == discord.file.File:
				file_list.append(item)

			if type(item) == discord.Embed:
				embed_list.append(item)
			


		if len(output) > 0:
			await message.channel.send(output)  # send the text

		for file_item in file_list:  # send the files
			await message.channel.send(file=file_item)

		for embed_item in embed_list:
			await message.channel.send(embed = embed_item)

	if len(message.mentions) > 0:
		for item in message.mentions:
			if item.id == client.user.id:
				await message.channel.send("Try: ```$ commands(none), or d!help```")

	await client.process_commands(message) # since custom parsing and discord supported commands do not go along well, this command needs to be used. it basically detects if the message has the command prefix. we also use different prefixes.

    # else:
    #   # history = open('history.txt', 'a')
    #   # history.write('\n' + message.content + '\t' + message.author.name + '\t' + str(message.author.id))
    #   # history.close()
    #   print(message.content)

@client.command(
	name = "ping"
)
async def ping(ctx, *args):
	try:
		text = ""

		for item in args:
			text += item + " "

		await ctx.channel.send(text)
	except Exception as problem:
		await ctx.channel.send(str(problem))

@client.command(
	name = "join"
)
async def join_voice_channel(ctx):
	try:	
		channel = ctx.author.voice.channel
		await channel.connect()
		await ctx.channel.send("Connected!")
	except Exception as problem:
		await ctx.channel.send(str(problem))


@client.command(
	name = "leave"
)
async def leave_voice_channel(ctx):
	try:
		await ctx.voice_client.disconnect()
	except Exception as problem:
		await ctx.channel.send(str(problem))


@client.command(
	name="tts"
)
async def play_speech(ctx, *args):
	try:
		# joins the arguments into one text variable
		speech_text = ""
		for item in args:
			speech_text += item + " "

		guild = ctx.guild 
		
		voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)

		try:
			# detects which language
			from langdetect import detect_langs
			lang = str(max(detect_langs(speech_text)))[0:2]

			# creates a mp3 value with the speech
			from gtts import gTTS
			speech = gTTS(text=speech_text, lang=lang)
		except:
			# handles, in case there are no features or supported languages.
			from gtts import gTTS
			speech = gTTS(text=speech_text, lang='en')


		speech.save("custom_packages/text_to_speech/speech.mp3")
		
		# plays the mp3 file
		audio_source = discord.FFmpegPCMAudio("custom_packages/text_to_speech/speech.mp3")

		if not voice_client.is_playing():
			voice_client.play(audio_source, after=None)
	
	except Exception as problem:
		await ctx.channel.send(str(problem))


keep_alive()

client.run(os.getenv('TOKEN'))
