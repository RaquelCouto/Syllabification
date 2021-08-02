
from os import replace
import cv2
import csv
import pytesseract
import numpy as np
from PIL import Image

silabasDict = {}
divisaoSilabica = ''

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
#print(textoImag)
#textoImag = textoImg.strip('\n')
ListofWords = list(textoImag.split(" "))
print(ListofWords)

# Removing from the list all elements that are not strings

ListofWords = list(filter(None, ListofWords))

filteredList = []
for palavra in ListofWords:
    palavra = palavra.replace('.','')
    palavra = palavra.replace(',','') 
    filteredList.append(palavra)
filteredList = [item for item in filteredList if item.isalpha()]

#As linhas seguintes são para evitar minha perda de tempo agora, removelas e implementar função de identificar entidades
filteredList.remove('PLAYLIST')
filteredList.remove('rachelcouto')
#ListofWords = [x for x in ListofWords if not any(c.isdigit() for c in x)]
print(filteredList)

#
palavrasConcatenadas = []

print(len(filteredList))
for i in range(0,(len(filteredList)-1)):
    elemento = filteredList[i]+filteredList[i+1]
    palavrasConcatenadas.append(elemento)

print(palavrasConcatenadas)

#aqui eu crio um dicionário com as palavras e divisão silábica
with open('palavras.csv', newline='') as csvfile:
    dicionario = csv.reader(csvfile)#, quotechar='|')

    for linha in dicionario:
        for elemento in linha:
            elemento = elemento.split(';')
            key = elemento[0]
            value = elemento[1]
        silabasDict[key] = value

#    print(silabasDict)


for elemento in palavrasConcatenadas:
    if elemento in silabasDict:
        divisaoSilabica = silabasDict[elemento]
        print(divisaoSilabica);
        break
    
if divisaoSilabica == '':
    print('palavra não encontrada')