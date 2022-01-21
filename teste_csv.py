# Importando a biblioteca para trabalhar com arquivos CSV
import csv

# Fazendo um link do arquivo com uma variável. Esse link é uma forma de representar o arquivo no código
arquivo = open('ramais.csv')

# Usando a biblioteca CSV para ler o conteúdo do arquivo usando o link associado anteriormente
tabela = csv.reader(arquivo)

# Esse trecho é gambiarra. Como a primeira linha do arquivo ramais.csv contém apenas os nomes das colunas.
# Manipulacao de arquivos tem um conceito importante que chamamos de cursor (ou ponteiro). 
# Toda linguagem lê uma sequencia de bytes a partir do cursor para manipular.
# Essa sequencia de bytes pode ser determinada de 
#   * forma fixa
#       > muitas vezes determinada pelo tamanho de uma variável de usada de máscara para leitura
#   * forma variável
#       > usando algum delimitador dentro do arquivo, como um caratere especial, uma quebra de linha
# Com o comando next, o python usa a quebra de linha para determinar quantos bytes está lendo.
# Ou seja, se eu usar várias vezes o comando next estará lendo o arquivo `linha-a-linha`.
# O comando next retorna a linha lida pelo comando.
cabecalho = next(tabela)

# Como o comando acima, desloquei o cursor para a segunda linha. Agora uso um loop foreach para percorrer as linhas do csv
for linha in tabela :
    # Como eh um arquivo CSV, a linha retornada eh um array onde cada indice representa uma coluna
    print("Nome: " + linha[0] + " - Ramal: " + linha[1])

# Apos uso, desfaco o link para liberar o arquivo
arquivo.close()