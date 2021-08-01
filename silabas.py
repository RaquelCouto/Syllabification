from os import replace
import cv2
import pytesseract
import numpy as np
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

image = cv2.imread('spotify4.png')



img_grayScale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_grayScale, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

binimagem = Image.fromarray(thresh)

#print(pytesseract.image_to_string(binimagem, lang='por'))

textoImg = pytesseract.image_to_string(binimagem, lang='por')

#convertendo a string retornada em uma lista de palavras
print(textoImg)
textoImag = textoImg.replace('\n',' ')
print(textoImag)
#textoImag = textoImg.strip('\n')
li = list(textoImag.split(" "))
print(li)

cv2.waitKey(0)
cv2.destroyAllWindows()
