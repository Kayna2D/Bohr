import math
from  decimal import Decimal

# Constantes
c = 3 * 10**8  # Velocidade da luz em m/s
h = 6.626 * 10**(-34)  # Constante de Planck em J*s
h_ev = 4.136E-15  # Constante de Planck em eV*s
m = 9.11 * 10**(-31)  # Massa do eletron em kg

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
    print("Entre com o nível inicial de energia (n_i): ")
    ni = int(input())
    print("Entre com o nível final de energia (n_f): ")
    nf = int(input())

    # Calcula a energia do fóton
    E_foton = energia_foton(ni, nf)
    f_foton = frequencia(E_foton)  # Frequência do fóton
    lambda_foton = comprimento_onda(E_foton)  # Comprimento de onda do fóton

    print(f"\nEnergia do fóton: {Decimal(E_foton):.2E} eV")
    print(f"Frequência do fóton: {Decimal(f_foton):.2E} Hz")
    print(f"Comprimento de onda do fóton: {Decimal(lambda_foton):.2E} m")


def absorcao():
    print("1 - Calcular energia final")
    print("2 - Calcular energia inicial")
    opcao = int(input("Digite a opção que deseja calcular: "))
    
    if opcao == 1:
        # Entrada: energia inicial e frequência ou comprimento
        print("Entre com a energia inicial (eV): ")
        E_inicial = float(input())
        
        print("1 - Frequência (Hz)")
        print("2 - Comprimento (m)")
        opcao2 = int(input("Digite a propriedade de entrada: "))

        if opcao2 == 1:
            print("Entre com a Frequência (Hz): ")
            f = float(input())
            E_foton = h * f / 1.602E-19  # Converte energia de J para eV
            E_final = E_inicial + E_foton
            print(f"Energia final: {Decimal(E_final):.2E} eV")
        else:
            print("Entre com o comprimento (m): ")
            l = float(input())
            f = c / l
            E_foton = h * f / 1.602E-19  # Converte energia de J para eV
            E_final = E_inicial + E_foton
            print(f"Energia final: {Decimal(E_final):.2E} eV")

    else:
        # Entrada: energia final e frequência ou comprimento
        print("Entre com a energia final (eV): ")
        E_final = float(input())

        print("1 - Frequência (Hz)")
        print("2 - Comprimento (m)")
        opcao2 = int(input("Digite a propriedade de entrada: "))

        if opcao2 == 1:
            print("Entre com a Frequência (Hz): ")
            f = float(input())
            E_foton = h * f / 1.602E-19  # Converte energia de J para eV
            E_inicial = E_final - E_foton
            print(f"Energia inicial: {Decimal(E_inicial):.2E} eV")
        else:
            print("Entre com o comprimento (m): ")
            l = float(input())
            f = c / l
            E_foton = h * f / 1.602E-19  # Converte energia de J para eV
            E_inicial = E_final - E_foton
            print(f"Energia inicial: {Decimal(E_inicial):.2E} eV")

def emissao():
    print("1 - Calcular nível inicial")
    print("2 - Calcular nível final")
    opcao = int(input("Digite a opção que deseja calcular: "))
    print("1 - Frequência (Hz)")
    print("2 - Comprimento (m)")
    opcao2 = int(input("Digite a propriedade de entrada: "))

    if opcao == 1:
        print("Entre com o nível final (n_f): ")
        nf = int(input())

        if opcao2 == 1:
            print("Entre com a Frequência (Hz): ")
            f = float(input())
            ni = nivel_quatico_freq(f)
            print(f"Nível inicial (n_i): {ni}")
        else:
            print("Entre com o comprimento (m): ")
            l = float(input())
            f = c / l
            ni = nivel_quatico_freq(f)
            print(f"Nível inicial (n_i): {ni}")

    else:
        print("Entre com o nível inicial (n_i): ")
        ni = int(input())

        if opcao2 == 1:
            print("Entre com a Frequência (Hz): ")
            f = float(input())
            nf = nivel_quatico_freq(f)
            print(f"Nível final (n_f): {nf}")
        else:
            print("Entre com o comprimento (m): ")
            l = float(input())
            f = c / l
            nf = nivel_quatico_freq(f)
            print(f"Nível final (n_f): {nf}")


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

