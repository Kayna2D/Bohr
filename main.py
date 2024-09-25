import math
from  decimal import Decimal

# Constantes
c = 3 * 10**8  # Velocidade da luz em m/s
epsilon_0 = 8.85 * 10**-12  # Permissividade do vácuo em F/m
Z_0 = 377  # Impedância do vácuo em ohms

def menu():
  while True:
    print("1 - Propriedades do atomo de H")
    print("2 - Emissao/absorcao de foton")
    print("3 - Nivel inicial ou final na absorcao de um foton")
    print("4 - Nivel inicial ou final na emissao de um foton")
    print("5 - Elementos do foton")
    print("0- Sair\n")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
      propriedades()
      print()
    elif opcao == 2:
      emissao_absorcao()
      print()
    elif opcao == 3:
      absorcao()
      print()
    elif opcao == 4:
      emissao()
      print()
    elif opcao == 5:
      foton()
      print()
    elif opcao == 0:
      print("Saindo...")
      break