# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário, 
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO split(): permite dividir o conteúdo da variável de acordo com as condições especificadas 
# em cada parâmetro da função ou com os valores predefinidos por padrão;
# while True significa que, enquanto houver entradas, o código após o try continuará sendo executado


while True: 
    try: 
           # TODO:  Programe aqui dentro as condições necessárias para satisfazer o problema
           # e imprima a saída de acordo com a situação das pernas do papagaio
        n= input()
        if n == 'esquerda':
            print('ingles')
        if n == 'direita':
            print('frances')
        if n == 'nenhuma':
            print('portugues')
        if n == 'ambas':
            print('caiu')
        print()
    
    except EOFError: 
        break