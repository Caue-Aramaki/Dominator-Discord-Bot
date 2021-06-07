def convert_num_from_x_to_y(num, base_x=10, base_y=2):
  try:
    import math
    import numpy as np

    base_x = int(base_x)
    base_y = int(base_y)

    x_bases = str(num)
    decimal_value = 0
    x_len = len(x_bases)

    for digit_index in range(0, x_len):
      decimal_value += int(x_bases[digit_index]) * (base_x ** (x_len - digit_index - 1))
    
    value = decimal_value
    converted = ""

    exp = int(np.round(math.log(value, base_y)))

    for exp_index in range(0, exp + 1):

      temp = base_y ** (exp - exp_index)
      
      for coef_index in range(0, base_y + 1):

        if (temp * coef_index) > value:
          value = value - temp * (coef_index - 1)
          converted += str(coef_index - 1)
          break
    return int(converted)
  except:
    return "Error in convert_num_from_x_to_y"