def formatação(x):
    x = x.replace('\r','')
    x = x.replace(' ', '')
    x = x.replace('\t', '')
    x = x.replace('\n', '')
    x = x.replace('<d>', '')
    x = x.replace('<r>', '')
    x = x.replace('<div>', '')
    x = x.replace('</div>', '')
    x = x.replace('<td>', ';')
    x = x.replace('</td>', '')
    x = x.replace('<tr>', '')
    x = x.replace('</tr>', '\n')
    x = x.replace('<tbody>', '')
    x = x.replace('<th>', ';')
    x = x.replace('</thead>', '')
    x = x.replace('</tbody>', '')
    x = x.replace('</th>', '')
    x = x.replace('<table>', '')

    x.split(';')

    return x

def main():
    relatorio = open('Relatorio.Customizado.GUID.9.xls', encoding="ISO-8859-1")
    resultado = open('resultados.csv', 'w')
    lista_linhas = []
    
    for linha in relatorio.readlines():
          lista_linhas.append(formatação(linha))
    relatorio.close()

    while True:
        if lista_linhas[0] == '<thead>':
            del(lista_linhas[0])
            break
        else:
            del(lista_linhas[0])

    while True:
        if lista_linhas[-1] == '</table>':
            del(lista_linhas[-1])
            break
        else:
            del(lista_linhas[-1])

    for y in lista_linhas:
        resultado.write(y)
    resultado.close()
    

'''
lista = []

for x in txt.readlines():
       lista.append(formatação(x))


for y in lista:
    resultado.write(y)

resultado.close()
txt.close()

resul_formatado = open('resultados.txt','w')


print(lista)
i = 0
while True:
    if lista[i] == '<thead>':
        break

    else:
        lista[i] = ''
        i += 1

print(lista)
for x in lista:
        resul_formatado.write(x)'''

if __name__ == '__main__':
    main()
