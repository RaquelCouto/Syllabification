import csv

lista = []

with open('palavras.csv', newline='') as csvfile:
    dicionario = csv.reader(csvfile, delimiter=';')#, quotechar='|')
     
    print(type(dicionario))
    for linha in dicionario:
        lista.append(linha)
    print(lista[1000])
#     for row in spamreader:
#                  print(', '.join(row))

def linear_search(values, search_for):
    search_at = 0
    search_res = False
# Match the value with each data element	
    while search_at < len(values) and search_res is False:
        #if values[search_at][0] == search_for:
        if values[search_at][0].startswith(search_for):
            print('valor encontrado: %s na posição %d'%(values[search_at],search_at))
            search_res = True
        else:
            search_at = search_at + 1
    return search_res

def main():
    print(linear_search(lista,'seman'))

if __name__ == "__main__":
    main()