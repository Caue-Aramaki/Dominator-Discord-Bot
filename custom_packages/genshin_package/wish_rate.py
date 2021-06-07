

def calculate_constellation_rate(input):
  try:
    import numpy

    value = int(numpy.round(int(input)/160)) 

    value = min(value, 1259)
    with open("custom_packages/genshin_package/Statistics.csv") as excel_file:
      content = excel_file.read().split("\n")
      excel_file.close()

    content = content[value+1].split(",")

    my_message = f"```Rate calculation:\n Number of Wishes: {content[0]} \n No limited: {float(content[1])*100}% \t C0: {float(content[2])*100}% \n C1: {float(content[3])*100}% \t\t C2: {float(content[4])*100}% \n C3: {float(content[5])*100}% \t\t C4: {float(content[6])*100}% \n C5: {float(content[7])*100}% \t\t C6 or more: {float(content[8])*100}%```"

    return my_message

  except Exception as problem:
    return f"Error in calculate_constellation_rate: {str(problem)}"