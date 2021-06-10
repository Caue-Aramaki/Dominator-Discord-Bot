
import discord

# math functions
from parse_find_package.linear  import linear
from commands_package.math_comm import add
from commands_package.math_comm import multiply
from commands_package.math_comm import sin
from commands_package.math_comm import convert_base

# logging functions
from commands_package.log_comm import log_history

# miscellaneous functions
from commands_package.misc_comm import hi
from commands_package.misc_comm import wish_rate_genshin
  
# image functions
from commands_package.image_comm import image

# information functions
def list_commands(input=None, input_list=None):
    
  try:
    text_output = ""

    for item in key_list:
      text_output = text_output + "|" + item[0] + "|    "

    return "```" + text_output + "```"
  
  except Exception as problem:
    return "Error at list_commands: " + str(problem)
def info_help(input_string=None, input_list=None):
  try:
    if input_string is not None:  
      found = "Command not found. Try $commands(none)"
      for key_item in key_list:
        if key_item[0] == input_string:
          found = key_item[2]

      return found

    else:
      found = "Command not found. Try $commands(none)"
      for key_item in key_list:
        if key_item[0] == input_list[0]:
          found = key_item[2]
      
      return found

  except Exception as problem:
    return "Error at info_help: " + str(problem)


key_list = [["sin", sin, "```Outputs sin(x). sin(x)```"], 

            ["add", add, "```Add two numbers. add(x, y) = x + y```"],

            ["mult", multiply, "```Multiply two numbers. mult(x, y) = x * y```"],

            ["logh", log_history, "```Display history, logh(x)    NOT WORKING```"],

            ["hi", hi, "```Outputs \"Hello!\". hi(none)```"],

            ["commands", list_commands, "```Lists commands. commands(none)```"],

            ["image", image, "```Sends an image. image(none)```"],

            ["convert_base", convert_base, "```Converts a number N in base X to a number in base Y. convert_base(N, X, Y)```"],

            ["con_rate", wish_rate_genshin, "```Displays the chart of constellations given X primogems. con_rate(X)```"],

            ["linear", linear, "```Produces the input, unmodified. linear(x) = x```"],

            ["info", info_help, "```Descripts command info. info(command name)```"]
            ]