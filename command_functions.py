
# import os
# import discord
# import numpy as np
# from PIL import Image


# keys_list = []



# def find_command(input_text):
#   try:
#     found = False

#     for bucket in keys_list:
#       if bucket[0] == input_text:
#         found = bucket[1]
    
#     return found
  
#   except Exception as problem:
#     return "Error in find_command: " + str(problem)



# # def recursion_execute(input_list, input_function):

# #   if(len(input_list) == 1):
    
# #     return input_function(input_list[0]) 

# #   else:
# #     command_list = input_list
    
# #     command = find_command(command_list[0])
# #     command_list.pop(0)
    
# #     return input_function(command(command_list))



# def sum_one(input_list):

#   try:
#     if(len(input_list) == 1):
      
#       return float(input_list[0]) + 1

#     else:
#       command_list = input_list
      
#       command = find_command(command_list[0])
#       command_list.pop(0)
      
#       return float(command(command_list)) + 1
  
#   except Exception as problem:
#     return "Error at sum_one: " + str(problem)



# def sin(input_list):
#   try:
#     if(len(input_list) == 1):
      
#       return np.sin(float(input_list[0]))

#     else:
#       command_list = input_list
      
#       command = find_command(command_list[0])
#       command_list.pop(0)
      
#       return np.sin(float(command(command_list)))

#   except Exception as problem:
#     return "Error at sin: " + str(problem)



# def log_history(last_n):

#   try:
#     history_string = open("history.txt", 'r').read()

#     log_list = history_string.split('\n')
#     log_string = ''

#     length = len(log_list)

#     for i in range(length - int(last_n[0]), length):
#       log_string = log_string + "\n" + log_list[i]

#     return "```" + log_string + "```"
  
#   except Exception as problem:
#     return "Error at log_history: " + str(problem)



# def hi(input_list):
#   try:
#     return "Hello!"
#   except Exception as problem:
#     return "Oh boi, error at hi: " + str(problem)
  


# def list_commands(input_list):
    
#   try:
#     text_output = ""

#     for item in keys_list:
#       text_output = text_output + item[0] + "\t"

#     return "```" + text_output + "```"
  
#   except Exception as problem:
#     return "Error at list_commands: " + str(problem)



# def image(input_list):
#   try:
#     return discord.File('image_enhance/test_image.jpg')
#   except Exception as problem:
#     return "Error at image: " + str(problem)



# def convert_base(input_list):

#   try:
#     from custom_packages.convert_bases import convert_num_from_x_to_y
#     return convert_num_from_x_to_y(input_list[0], input_list[1], input_list[2])
  
#   except Exception as problem:
#     return "Error at convert_base: " + str(problem)


# def wish_rate_genshin(input_list):
#   try:
#     from custom_packages.genshin_package.wish_rate import calculate_constellation_rate

#     if(len(input_list) == 1):
      
#       return calculate_constellation_rate(float(input_list[0]))

#     else:
#       command_list = input_list
      
#       command = find_command(command_list[0])
#       command_list.pop(0)
      
#       return calculate_constellation_rate(float(command(command_list)))
#   except Exception as problem:
#     return "Error at wish_rate_genshin: " + str(problem)


# # from image_enhance.cv2_super_res import super_res

# # def image_enhance(input_list):
 
# #   img = open('image_enhance/test_image.jpg')
# #   sr_img = super_res(img)
  
  
# #   return sr_img
# #   # return discord.File(img, "result.png")


# keys_list = [["sin", sin], 
#             ["sum_one", sum_one],
#             ["logh", log_history],
#             ["hi", hi],
#             ["commands", list_commands],
#             ["image", image],
#             ["convert_base", convert_base],
#             ["con_rate", wish_rate_genshin]
#             ]