def image(input=None, input_list=None):
	import discord
	try:
		return discord.File('image_enhance/test_image.jpg')
	except Exception as problem:
		return "Error at image: " + str(problem)

# from image_enhance.cv2_super_res import super_res

# def image_enhance(input_list):
 
#   img = open('image_enhance/test_image.jpg')
#   sr_img = super_res(img)
  
  
#   return sr_img
#   # return discord.File(img, "result.png")