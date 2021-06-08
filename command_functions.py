
import os
import discord
import numpy as np
from PIL import Image


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
  try:
    if input is not None:
      return np.sin(float(input))
    else:
      return np.sin(float(input_list[0]))

  except Exception as problem:
    return "Error at sin: " + str(problem)



def log_history(last_n=None, input_list=None):

  try:
    if last_n is not None:
      number = int(last_n)
    else:
      number = int(input_list[0])
      
    history_string = open("history.txt", 'r').read()

    log_list = history_string.split('\n')
    log_string = ''

    length = len(log_list)

    for i in range(length - int(number), length):
      log_string = log_string + "\n" + log_list[i]

    return "```" + log_string + "```"
  
  except Exception as problem:
    return "Error at log_history: " + str(problem)



def hi(input=None, input_list=None):
  try:
    return "Hello!"
  except Exception as problem:
    return "Oh boi, error at hi: " + str(problem)
  


def list_commands(input=None, input_list=None):
    
  try:
    text_output = ""

    for item in key_list:
      text_output = text_output + item[0] + "\t"

    return "```" + text_output + "```"
  
  except Exception as problem:
    return "Error at list_commands: " + str(problem)



def image(input=None, input_list=None):
  try:
    return discord.File('image_enhance/test_image.jpg')
  except Exception as problem:
    return "Error at image: " + str(problem)



def convert_base(input_1=None, input_2=None, input_3=None, input_list=None):
  try:
    from custom_packages.convert_bases import convert_num_from_x_to_y
    if input_1 is not None:
      return convert_num_from_x_to_y(int(input_1), int(input_2), int(input_3))
    else:
      return convert_num_from_x_to_y(int(input_list[0]), int(input_list[1]), int(input_list[2]))
  except Exception as problem:
    return "Error at convert_base: " + str(problem)


def wish_rate_genshin(input=None, input_list=None):
  try:
    from custom_packages.genshin_package.wish_rate import calculate_constellation_rate

    if input is not None:
      return calculate_constellation_rate(float(input))
    else:
      return calculate_constellation_rate(float(input_list[0]))

  except Exception as problem:
    return "Error at wish_rate_genshin: " + str(problem)

from parse_find_package.linear import linear

# from image_enhance.cv2_super_res import super_res

# def image_enhance(input_list):
 
#   img = open('image_enhance/test_image.jpg')
#   sr_img = super_res(img)
  
  
#   return sr_img
#   # return discord.File(img, "result.png")

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