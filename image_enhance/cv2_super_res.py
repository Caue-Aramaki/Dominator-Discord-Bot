import cv2
import numpy as np
from PIL import Image

sr = cv2.dnn_superres.DnnSuperResImpl_create()

sr.readModel("image_enhance/LapSRN_x8.pb")
sr.setModel("lapsrn",8)

def super_res(input_image):
  # img = np.array(input_image)
  image = Image.open("image_enhance/test_image.jpg")   
  img = cv2.cvtColor(np.asarray(image),cv2.COLOR_RGB2BGR) 
  return sr.upsample(img)
