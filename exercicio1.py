#  Se achar necessario, faça import de outras bibliotecas


# Crie a função que será avaliada no exercício aqui
#define a função, expondo os seus parâmetros
def multiplas_operacoes(x, y):
    #soma os dois parâmetros
    soma = x + y
    #subtrai os dois parâmetros
    subtracao = x - y
    #multiplica os dois parâmetros
    multiplicacao = x * y
    #checka se o y é 0. Se for, o resultado da divisão também será 0
    if y == 0:
        divisao = 0
    #se y não for 0, ele efetua a divisão normalmente
    else:
        divisao = x / y
    #retorna os valores de cada operação
    return soma, subtracao, multiplicacao, divisao

#coleta os números que vao ser usados como parâmetros da função
a = float(input("Escreva o primeiro parâmetro: "))
b = float(input("Escreva o segundo parâmetro: "))
#chama a função com os devidos parâmetros e guarda seu retorno em uma váriavel
resultado = multiplas_operacoes(a, b)
#mostra o que foi retornado da função
print(resultado)


# Teste a sua função aqui (caso ache necessário)
