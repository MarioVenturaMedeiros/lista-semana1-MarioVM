#  Se achar necessario, faça import de outras bibliotecas


# Crie a função que será avaliada no exercício aqui
#define uma lista que vai agrupar dentro todas as outras listas
lista_aninhada = []

def soma_dos_aninhados():
    #define a variável soma como 0 e faz o usuário digitar o numero de listas que ele deseja aninhar em uma só
    soma = 0
    num_listas = int(input("Digite o número de listas que deseja aninhar: "))
    #para cada número de listas que o usuário escolheu, ele vai digitar o número de elementos que ele deseja conter naquela lista
    for i in range(num_listas):
        n = int(input("Digite o número de elementos na lista " + str(i + 1) + ": "))
        #com base no numero de listas, cria-se uma lista interna em branco para adicionarmos os valores
        lista_interna = []
        #fazemos um loop com base o número de elementos da lista para o usuário de fato escrever os elementos da lista
        #esses elementos são adicionados a variável soma para ver no final a soma de todos os elementos da lista_aninhada
        for j in range(n):
            #faz o usuário digitar o número de tal posição da lista interna
            x = int(input("Digite o número de posição " + str(j + 1) + " na lista: "))
            soma += x
            #adiciona o valor que o usuário escreveu a lista interna
            lista_interna.append(x)
        #junta a lista interna a lista aninhada, sendo a lista interna só um elemento da lista aninhada agora
        lista_aninhada.append(lista_interna)
    #retorna a soma de todos os números da lista aninhada
    return soma

#guarda o retorno da função em uma variável
resultado = soma_dos_aninhados()
#mostra a lista aninhada inteira
print(lista_aninhada)
#mostra a soma de todos os valores da lista aninhada
print(resultado)

# Teste a sua função aqui (caso ache necessário)
