# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário, 
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO split(): permite dividir o conteúdo da variável de acordo com as condições especificadas 
# em cada parâmetro da função ou com os valores predefinidos por padrão;

# Abaixo segue um exemplo de código que você pode ou não utilizar
salario = int(input()) 

# TODO:  Calcule o salário do funcionário e print o novo salário, bem como o valor de reajuste ganho e o índice reajustado (em porcentagem)
if (salario <= 600.00):
  s = salario * 1.17
  r = s - salario
  p = 17
elif (salario >= 600.01 and salario<= 900.00):
  s = salario * 1.13
  r = s - salario
  p = 13
elif (salario >= 900.01 and salario <= 1500.00):
  s = salario * 1.12
  r = s - salario
  p = 12
elif (salario >= 1500.01 and salario <= 2000.00):
  s = salario * 1.10
  r = s - salario
  p = 10
else:
  s = salario * 1.05
  r = s - salario
  p = 5

print(f"Novo salario: {s:.2f}")
print(f"Reajuste ganho: {r:.2f}")
print(f"Em percentual: {p} %")