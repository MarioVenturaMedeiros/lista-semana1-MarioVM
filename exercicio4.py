#  Se achar necessario, faça import de outras bibliotecas


# Crie a função que será avaliada no exercício aqui
# define a função, e cria uma lista vazia
def tem_duplicados():
    lista = []
    # define o número de elementos da lista com base no que o usuário digitar
    n = int(input("Escreva o número de elementos na lista: "))
    # faz um loop que repete baseado no número de elementos que o usuário escreveu, que estão guardados na variavel a cima
    for i in range(n):
        # coleta o número escrito pelo usuário em uma variável
        y = float(input("Escreva um número: "))
        # adiciona o número escrito na lista
        lista.append(y)
    # cria um loop que repete baseado no tamanho da lista
    for i in range(len(lista)):
        # 0 count serve para verificar quantas vezes qualquer elemento foi repitido na lista.
        # se o  count for maior que 1, ou seja, existir mais de um elemento igual o retorno será verdadeiro
        if lista.count(lista[i]) > 1:
            return True
    # se o count for 1 quer dizer que só há um elemento de cada na função, retornando false por não haver duplicados
    return False


# guarda o retorno da função em uma variável
resultado = tem_duplicados()
# printa a variável que seria o retorno da função
print(resultado)

# Teste a sua função aqui (caso ache necessário)
