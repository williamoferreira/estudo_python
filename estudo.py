# Para escrever no console use o comando print
print("Hello world");

# if eh parecido com C e C# mas inicio do bloco sera o caractere :
if (5 > 2): 
    print ("Cinco eh maior que dois")

# Para criar arrays basta colocar o nome do array e uma atribuiacao seguida de colchetes.
# Preencher os colchetes faz o array vir preenchido com os elementos dos colchetes
# Use virgulas ',' para separar os elemetos 
stringNumbers = ["1", "2", "3", "4", "5"]

# Imprimindo todos os elementos do array
print(stringNumbers)

# Imprimindo o elemento de indice 2 (terceiro elemento, uma vez que o zero conta na lista)
print(stringNumbers[2])


numbers = [ 1, 3, 10, 25, 10, 2]
# Loop foreach no python
for number in numbers :
    # Concatenacao de strings e typecasting uma vez que a variavel number é do tipo int
    print("current number: " + str(number))