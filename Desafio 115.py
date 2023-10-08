from desafio115.lib.interface import *
from desafio115.lib.arquivo import *
arq = 'file.txt'
if not arquivoexiste(arq):
    criararquivo(arq)
cabecalho('Sistema de cadastros de pessoas')
while True:
    resposta = menu(['Cadastrar Pessoas', 'Listar Pessoas', 'Sair do Programa'])
    if resposta == 2:
        lerarquivo(arq)
    elif resposta == 1:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do programa')
        break
    else:
        print('ERRO! Digite uma opção válida!')
