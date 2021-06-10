

def add(input_1=None, input_2=None, input_list=None):
  try:
    if input_1 is not None:
      return float(input_1) + float(input_2) 
    else:
      return float(input_list[0]) + float(input_list[1])
  
  except Exception as problem:
    return "Error at sum_one: " + str(problem)

def multiply(input_1=None, input_2=None, input_list=None):
  try:
    if input_1 is not None:
      return float(input_1) * float(input_2) 
    else:
      return float(input_list[0]) * float(input_list[1])
  
  except Exception as problem:
    return "Error at sum_one: " + str(problem)

def sin(input=None, input_list=None):
	import numpy as np
	try:
		if input is not None:
			return np.sin(float(input))
		else:
			return np.sin(float(input_list[0]))

	except Exception as problem:
		return "Error at sin: " + str(problem)

def convert_base(input_1=None, input_2=None, input_3=None, input_list=None):
  try:
    from custom_packages.convert_bases import convert_num_from_x_to_y
    if input_1 is not None:
      return convert_num_from_x_to_y(int(input_1), int(input_2), int(input_3))
    else:
      return convert_num_from_x_to_y(int(input_list[0]), int(input_list[1]), int(input_list[2]))
  except Exception as problem:
    return "Error at convert_base: " + str(problem)