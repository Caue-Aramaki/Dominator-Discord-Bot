

def calculate_constellation_rate(input):
	try:
		import numpy

		value = int(numpy.round(int(input)/160)) 

		value = min(value, 1259)
		with open("custom_packages/genshin_package/Statistics.csv") as excel_file:
			content = excel_file.read().split("\n")
			excel_file.close()

		content = content[value+1].split(",")

		# for index in range(0, len(content)):
		# 	content[index] = '{0:.2f}'.format(content[index])

		my_message = f"Rate calculation:\n Number of Wishes: {content[0]} \n\tNo limited: {float(content[1])*100:.2f}% \t C0: {float(content[2])*100:.2f}% \n\tC1:\t\t {float(content[3])*100:.2f}% \t C2: {float(content[4])*100:.2f}% \n\tC3: \t\t{float(content[5])*100:.2f}% \t C4: {float(content[6])*100:.2f}% \n\tC5: \t\t{float(content[7])*100:.2f}% \t C6 or more: {float(content[8])*100:.2f}%"

		return my_message

	except Exception as problem:
		return f"Error in calculate_constellation_rate: {str(problem)}"