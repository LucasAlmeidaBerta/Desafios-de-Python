def notas(*nota, sit=False):
    """
    -> Função para ler Multiplas notas,
       mostrar o total de notas inseridas
       mostrar a maior nota
       mostrar a menor nota
       mostrar a situação
       param *nota: Recebe ínumeras notas.
       param sit: Parâmetro opcional, quando Verdadeiro
                  retorna a situação.
       return: retorna um dicionário com todas as informações.
    """
    dic = dict()
    dic['total'] = len(nota)
    dic['maior'] = max(nota)
    dic['menor'] = min(nota)
    dic['media'] = sum(nota) / len(nota)
    if sit:
        if dic['media'] >= 7:
            dic['situacao'] = 'Boa'
        elif dic['media'] >= 5:
            dic['situacao'] = 'Razoável'
        else:
            dic['situacao'] = 'Ruim'
    return dic


# Main
resp = notas(9, 8, 5, 10, sit=True)
print(resp)
