# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário, 
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO ord(): Retorna o valor  ASCII de cada letra ou símbolo do teclado;
letra = input() 

# TODO: De acordo com a entrada, imprima a posição dessa letra no Alfabeto; 
lista = [chr(i) for i in range(ord('A')-1,ord('Z')+1)]
print (lista.index(letra))