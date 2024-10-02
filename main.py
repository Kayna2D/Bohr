import math
from  decimal import Decimal

# Constantes
c = 3 * 10**8  # Velocidade da luz em m/s
h = 6.626 * 10**(-34)  # Constante de Planck em J*s
h_ev = 4.136E-15  # Constante de Planck em eV*s
m = 9.11 * 10**(-31)  # Massa do eletron em kg
conversor = 1.602E-19 # Conversor entre eV e J

def menu():
  while True:
    print("1 - Propriedades de H")
    print("2 - Propriedades do foton na emissao/absorcao")
    print("3 - Nivel inicial ou final na absorcao de um foton")
    print("4 - Nivel inicial ou final na emissao de um foton")
    print("5 - Propriedades do foton")
    print("0- Sair\n")
    opcao = int(input("Digite a opcao desejada: "))

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

def propriedades():
  print("Entre com o nivel de energia: ")
  n = float(input())

  raio = n**2 * 5.29E-11
  v = 2.187E6/n
  ec = 13.6/n**2
  ep = -27.2/n**2
  e = -13.6/n**2
  comprimento = h/(m*v)

  print() 
  print(f'Raio da órbita: {Decimal(raio):.2E} m')
  print(f'Velocidade: {Decimal(v):.2E} m/s')
  print(f'Energia cinetica: {Decimal(ec):.2E} eV')
  print(f'Energia potencial: {Decimal(ep):.2E} eV')
  print(f'Energia total: {Decimal(e):.2E} eV')
  print(f'Comprimento de onda: {Decimal(comprimento):.2E} m')

def emissao_absorcao():
  print("Entre com o nivel inicial de energia: ")
  ni = 13.6 / float(input())**2
  print("Entre com o nivel final de energia: ")
  nf = 13.6 / float(input())**2

  ef = ni-nf
  if ef < 0:
    ef = -ef
  l = h*c/(ef*conversor)
  f = ef*conversor/h

  print()
  print(f'Energia: {Decimal(ef):.2E} eV')
  print(f'Comprimento: {Decimal(l):.2E} m')
  print(f'Frequencia: {Decimal(f):.2E} Hz')

def absorcao():
  print("1 - Nivel inicial")
  print("2 - Nivel final")
  opcao = int(input("Digite a opção que deseja calcular: "))
  print("1 - Frequencia (Hz)")
  print("2 - Comprimento (m)")
  opcao2 = int(input("Digite a propriedade de entrada: "))

  if opcao == 1:
    print("Entre com o nivel final de energia: ")
    nf = -13.6 / float(input())**2

    if opcao2 == 1:
      print("Entre com a Frequencia (Hz): ")
      f = float(input())
      ef = h_ev * f
    else:
      print("Entre com o comprimento (m): ")
      l = float(input())
      ef = h_ev*c/l

    ei = nf - ef
    ni = math.sqrt(nf/ei)

    print(f'Nivel inicial: {Decimal(ni):.2E}')

  else:
    print("Entre com o nivel inicial de energia: ")
    ni = -13.6 / float(input())**2

    if opcao2 == 1:
      print("Entre com a Frequencia (Hz): ")
      f = float(input())
      ef = h_ev * f
    else:
      print("Entre com o comprimento (m): ")
      l = float(input())
      ef = h_ev*c/l

    efinal = ni + ef
    nf = math.sqrt(-13.6/efinal)

    print(f'Nivel final: {Decimal(nf):.2E}')

def emissao():
  print("1 - Nivel inicial")
  print("2 - Nivel final")
  opcao = int(input("Digite a opção que deseja calcular: "))
  print("1 - Frequencia (Hz)")
  print("2 - Comprimento (m)")
  opcao2 = int(input("Digite a propriedade de entrada: "))

  if opcao == 1:
    print("Entre com o nivel final de energia: ")
    nf = -13.6 / float(input())**2

    if opcao2 == 1:
      print("Entre com a Frequencia (Hz): ")
      f = float(input())
      ef = h_ev * f
    else:
      print("Entre com o comprimento (m): ")
      l = float(input())
      ef = h_ev*c/l
      
    ei = ef + nf
    ni = math.sqrt(-13.6/ei)
    print(f'Nivel inicial: {Decimal(ni):.2E}')
    
  else:
    print("Entre com o nivel inicial de energia: ")
    ni = -13.6 / float(input())**2

    if opcao2 == 1:
      print("Entre com a Frequencia (Hz): ")
      f = float(input())
      ef = h_ev * f
    else:
      print("Entre com o comprimento (m): ")
      l = float(input())
      ef = h_ev*c/l

    efinal = ni - ef
    nf = math.sqrt(-13.6/efinal)
    print(f'Nivel final: {Decimal(nf):.2E}')

    print("Nivel final na emissao de um foton")

def foton():
  print("1 - Comprimento (m)")
  print("2 - Frequencia (Hz)")
  print("3 - Energia (J)")
  print("4 - Energia (eV)")
  opcao = int(input("Digite a propriedade de entrada: "))

  if opcao == 1:
    print("Entre com o comprimento (m): ")
    l = float(input())

    e_j = h*c/l
    e_ev = e_j / 1.602E-19

    print(f'Energia em J: {Decimal(e_j):.2E}')
    print(f'Energia em eV: {Decimal(e_ev):.2E}')

  elif opcao == 2:
    print("Entre com a Frequencia (Hz): ")
    f = float(input())

    e_j = h*f
    e_ev = e_j / 1.602E-19

    print(f'Energia em J: {Decimal(e_j):.2E}')
    print(f'Energia em eV: {Decimal(e_ev):.2E}')

  elif opcao == 3:
    print("Entre com a Energia (J): ")
    e = float(input())

    l = h*c/e
    f = e / h

    print(f'Comprimento: {Decimal(l):.2E} m')
    print(f'Frequencia: {Decimal(f):.2E} Hz')

  else:
    print("Entre com a Energia (eV): ")
    e = float(input())

    l = h_ev*c/e
    f = e / h_ev

    print(f'Comprimento: {Decimal(l):.2E} m')
    print(f'Frequencia: {Decimal(f):.2E} Hz')

print("Autores:")
print("Kayna de Deus Ferreira da Silva")
print("Mario Eugenio Silva")
print()
print("------------------------------------------------------------------------------------")
print()
print("Atomo de Bohr e Quantizacao")
print("Programa que realiza as operacoes relevantes a quantizacao e ao atomo de Bohr")
print("No modelo de Bohr, os elétrons orbitam o nucleo em niveis de energia, transicao que ocorre quando o eletron absorve ou emite energia em formato de fotons")
print("O programa realiza os seguintes calculos:")
print("Propriedades do eletron do atomo de hidrogenio")
print("Niveis e outras propriedades no processo de emissao/absorcao")
print("Propriedades do foton")
print()
print("------------------------------------------------------------------------------------")
print()
menu()

