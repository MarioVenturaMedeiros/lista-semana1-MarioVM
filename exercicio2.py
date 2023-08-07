#  Se achar necessario, faça import de outras bibliotecas


# Crie a função que será avaliada no exercício aqui
#cria a função, definindo duas listas que vão ser usadas
def cumulativo():
    lista = []
    lista2 = []
    #variavel que irá ser o resultado da soma de todos os números da lista
    x = 0
    #define o número de elementos que vão estar na lista
    n = int(input("Escreva o número de elementos na lista: "))
    #faz um loop para o usuário definir o número que irá ser colocado na lista. O loop roda com base no n coletado anteriormente
    for i in range(n):
        y = float(input("Escreva um número: "))
        #adiciona o número escrito na lista
        lista.append(y)
    #um loop que percorre a lista inteira
    for i in range(len(lista)):
        #soma a variável x a todos os números da lista, e enquanto isso vai adicionando os resultados em uma outra lista
        x += lista[i]
        lista2.append(x)
    #retorna a lista com todos os valores somados
    return lista2

#guarda o return da função como uma variável, e em seguida da print nessa variável, dando print na lista2
resultado = cumulativo()
print(resultado)


# Teste a sua função aqui (caso ache necessário)
