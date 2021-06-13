

def calculate_constellation_rate(input):
	try:
		import numpy

		value = int(numpy.round(int(input)/160)) 

		value = min(value, 1259)
		with open("custom_packages/genshin_package/Statistics.csv") as excel_file:
			content = excel_file.read().split("\n")
			excel_file.close()

		content = content[value+1].split(",")
		
		import discord

		# Adds embed, and sets Title / Desc
		embedVar = discord.Embed(title="Constellation Rate Calculation", description=f"Calculates the constellations probabilities based on simulation data. As input, the number of primogems.\n\n*Hint: you can do the command like this:*\n`$con_rate(mult({content[0]}, 160))`", color=0x1ABC9C)
		
		# Authors
		embedVar.set_author(name="Mugen, Lord of Coffee", icon_url="https://media.discordapp.net/attachments/583813659625521165/853718307316039691/ee307c1232e84a2cb05e9cf5a3d6e2b2.png")

		# Thumbnail
		embedVar.set_thumbnail(url="https://media.discordapp.net/attachments/583813659625521165/853719990661677095/360.png")

		# Fields
		embedVar.add_field(name="Requested Inputs", value=f"Rolls:   {content[0]}\nPrimogems:   {int(input)}", inline=False)
		
		embedVar.add_field(name="No Limited", value=f"{float(content[1])*100:.2f}%", inline=True)

		embedVar.add_field(name="C0", value=f"{float(content[2])*100:.2f}%", inline=True)

		embedVar.add_field(name="C1", value=f"{float(content[3])*100:.2f}%", inline=True)

		embedVar.add_field(name="C2", value=f"{float(content[4])*100:.2f}%", inline=True)

		embedVar.add_field(name="C3", value=f"{float(content[5])*100:.2f}%", inline=True)

		embedVar.add_field(name="C4", value=f"{float(content[6])*100:.2f}%", inline=True)

		embedVar.add_field(name="C5", value=f"{float(content[7])*100:.2f}%", inline=True)

		embedVar.add_field(name="C6 or more", value=f"{float(content[8])*100:.2f}%", inline=True)

		# Footer
		embedVar.set_footer(text="Note: the percentages have a pessimistic bias, which means your real chances are slightly better. The reason for this is that our models do not account for glitter exchange.", icon_url="https://media.discordapp.net/attachments/583813659625521165/853724477317840906/846151055104016394.png")

		# Return
		return embedVar

	except Exception as problem:
		return f"Error in calculate_constellation_rate: {str(problem)}"