from os import replace
from typing import TypedDict
import cv2
import csv
import pytesseract
import numpy as np
from PIL import Image

silabasDict = {}
divisaoSilabica = ''

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

image = cv2.imread('ellipsis.png')

img_grayScale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_grayScale, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

binimagem = Image.fromarray(thresh)

#print(pytesseract.image_to_string(binimagem, lang='por'))

textoImg = pytesseract.image_to_string(binimagem, lang='por')

#convertendo a string retornada em uma lista de palavras
print(textoImg)

textoImg = textoImg.replace('\n',' ')
textoImg = list(textoImg.split(' '))
print(textoImg)

badWord = []
for elemento in textoImg:
    if '...' in elemento:
        badWord.append(elemento)

print(badWord)

noEllipsis = []
for elemento in badWord:
    noEllipsis.append(elemento.replace('...',''))

print(noEllipsis)

def list_contains(List1, List2): 
    set1 = set(List1) 
    set2 = set(List2) 
    if set1.intersection(set2): 
        return True 
    else: 
        return False

badWords = ['cu', 'foda', 'droga','porra']

for i in noEllipsis:
    if i in badWords:
        print("A palavra '{}' é uma bad word em português".format(i))
    else:
        print("Nenhuma bad word encontrada")