
from os import replace
import cv2
import csv
import pytesseract
import numpy as np
from PIL import Image

silabasDict = {}
divisaoSilabica = ''

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

image = cv2.imread('spotify-correto.png')

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
#filteredList.remove('PLAYLIST')
#filteredList.remove('rachelcouto')
#ListofWords = [x for x in ListofWords if not any(c.isdigit() for c in x)]
print(filteredList)

#
palavrasConcatenadas = []

print(len(filteredList))
for i in range(0,(len(filteredList)-1)):
    elemento = filteredList[i]+filteredList[i+1]
    palavrasConcatenadas.append([elemento,filteredList[i],filteredList[i+1]])

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

palavra = []

for elemento in palavrasConcatenadas:
    if elemento[0] in silabasDict:
        palavra = elemento
        divisaoSilabica = silabasDict[elemento[0]]
        print(palavra)
        print(divisaoSilabica);
        break

if divisaoSilabica == '':
    print('palavra não encontrada')

#operações para somar as silabas

silabas = []
silabasConcatenadas = []
silabas = divisaoSilabica.split('-')
print(silabas)



quebrasAceitaveis = []
aux = ''

for i in range(0,len(silabas)-1):
    variavel = silabas[i]
    aux = aux + variavel
    quebrasAceitaveis.append(aux)

#print(quebrasAceitaveis)
aux = ''

for i in range(len(silabas)-1,0,-1):
    variavel = silabas[i]
    aux = variavel + aux
    quebrasAceitaveis.append(aux)

print(quebrasAceitaveis)

# função para checar se uma lista está contida em outra
def list_contains(List1, List2): 
    set1 = set(List1) 
    set2 = set(List2) 
    if set1.intersection(set2): 
        return True 
    else: 
        return False

# checagem final

if list_contains(palavra,quebrasAceitaveis):
    print("A palavra {} foi separadas em silábas corretamente".format(palavra[0]))
else:
    print("A palavra {} foi separadas em silábas erroneamente".format(palavra[0]))