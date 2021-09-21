
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

image = cv2.imread('pt_BR2.jpeg')

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

filteredList = []
for palavra in textoImg:
    palavra = palavra.replace('.','')
    palavra = palavra.replace(',','')
    palavra = palavra.replace('(','')
    palavra = palavra.replace(')','')
    filteredList.append(palavra)
filteredList = [item for item in filteredList if item.isalpha()]

print(filteredList)

with open('palavras.csv', encoding="iso8859-1",newline='') as csvfile:
    dicionario = csv.reader(csvfile)#, quotechar='|')
    print("O dicionario aqui ó:::", dicionario)
    for linha in dicionario:
        for elemento in linha:
            elemento = elemento.split(';')
            key = elemento[0]
            value = elemento[1]
        silabasDict[key] = value

Checker = True

for palavra in filteredList:
    if palavra in silabasDict:
        Checker = True
    else:
        print("a palavra {} não faz parte da linguagem selecionada".format(palavra))