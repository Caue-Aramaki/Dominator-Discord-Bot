
def my_embed(input=None, input_list=None):
	import discord
	try:

		# Adds embed, and sets Title / Desc
		embedVar = discord.Embed(title="Title", description="Desc", color=0x00ff00)
		
		# Authors
		embedVar.set_author(name="Mugen, Lord of Coffee", icon_url="https://media.discordapp.net/attachments/583813659625521165/853718307316039691/ee307c1232e84a2cb05e9cf5a3d6e2b2.png")

		# Thumbnail
		embedVar.set_thumbnail(url="https://media.discordapp.net/attachments/583813659625521165/853719990661677095/360.png")

		# Fields
		embedVar.add_field(name="Field1", value="hi", inline=False)
		
		embedVar.add_field(name="Field2", value="hi2", inline=True)

		embedVar.add_field(name="Field3", value="hi3", inline=True)

		# Footer
		embedVar.set_footer(text="Footing", icon_url="https://media.discordapp.net/attachments/583813659625521165/853721090961309706/9k.png")

		# Return
		return embedVar


	except Exception as problem:
		return "Error at my_embed: " + str(problem)