import cv2
import pytesseract
import numpy as np
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

image = cv2.imread(r'C:\Users\raque\Documents\GitHub\spotify-seeded.jpg')


image = cv2.resize(image, None, fx = 1, fy = 1, interpolation = cv2.INTER_CUBIC)

img_grayScale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_grayScale, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

binimagem = Image.fromarray(thresh) 
cv2.imshow('Gray image', img_grayScale)

print(pytesseract.image_to_string(binimagem, lang='por'))
data = pytesseract.image_to_data(binimagem, output_type=pytesseract.Output.DICT,lang='por')
print(data)

print(pytesseract.image_to_boxes(binimagem, lang='por'))

cv2.waitKey(0)
cv2.destroyAllWindows()
