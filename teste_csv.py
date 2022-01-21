import csv
arquivo = open('ramais.csv')
tabela = csv.reader(arquivo)
cabecalho = next(tabela)
for linha in tabela :
    print("Nome: " + linha[0] + " - Ramal: " +linha[1])
arquivo.close()