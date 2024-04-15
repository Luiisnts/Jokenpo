import os
import random


def clrscr():
  os.system('clear')


#-------------------------------------------------------------------------------#


def JXJ():
  pontosP1 = 0
  pontosP2 = 0
  placar = {'Jogador 1': pontosP1, 'Jogador 2': pontosP2}

  while True:
    clrscr()
    escolhaP1 = input(
        "Jogador 1 escolha entre pedra, papel ou tesoura: ").strip().lower()
    escolhaP2 = input(
        "Jogador 2 escolha entre pedra, papel ou tesoura: ").strip().lower()

    if escolhaP1 not in ["pedra", "papel", "tesoura"
                         ] or escolhaP2 not in ["pedra", "papel", "tesoura"]:
      print(
          "Escolha inválida. Por favor, escolha entre pedra, papel ou tesoura."
      )
      input("Pressione Enter para continuar...")
    else:
      if escolhaP1 == escolhaP2:
        resultado = "Empate"
      elif (escolhaP1 == "pedra" and escolhaP2 == "tesoura") or \
           (escolhaP1 == "papel" and escolhaP2 == "pedra") or \
           (escolhaP1 == "tesoura" and escolhaP2 == "papel"):
        pontosP1 += 1
        resultado = "Jogador 1 venceu"
      else:
        pontosP2 += 1
        resultado = "Jogador 2 venceu"

      placar['Jogador 1'] = pontosP1
      placar['Jogador 2'] = pontosP2

      print(resultado)
      print("Placar:")
      for jogador, pontos in placar.items():
        print(f"{jogador}: {pontos}")
      print()

      jogar_novamente = input(
          "Deseja jogar novamente? (s/n): ").strip().lower()
      while jogar_novamente not in ["s", "n"]:
        print("Por favor, escolha 's' para sim ou 'n' para não.")
        jogar_novamente = input(
            "Deseja jogar novamente? (s/n): ").strip().lower()

      if jogar_novamente == 'n':
        clrscr()
        print("Placar final:", placar)
        break


#-------------------------------------------------------------------------------#


def JXM():
  pontosP1 = 0
  pontosMaquina = 0
  placar = {'Jogador': pontosP1, 'Máquina': pontosMaquina}

  while True:
    clrscr()
    maquina = random.choice(["pedra", "papel", "tesoura"])
    escolhaP1 = input(
        "Jogador 1 escolha entre pedra, papel ou tesoura: ").strip().lower()

    if escolhaP1 not in ["pedra", "papel", "tesoura"]:
      print(
          "Escolha inválida. Por favor, escolha entre pedra, papel ou tesoura."
      )
      input("Pressione Enter para continuar...")
    else:
      if escolhaP1 == maquina:
        resultado = "Empate"
      elif (escolhaP1 == "pedra" and maquina == "tesoura") or \
           (escolhaP1 == "papel" and maquina == "pedra") or \
           (escolhaP1 == "tesoura" and maquina == "papel"):
        pontosP1 += 1
        resultado = "Jogador 1 venceu"
      else:
        pontosMaquina += 1
        resultado = "Máquina venceu"

      placar['Jogador'] = pontosP1
      placar['Máquina'] = pontosMaquina

      print("Escolha do Jogador 1:", escolhaP1)
      print("Escolha da Máquina:", maquina)
      print(resultado)
      print("Placar:")
      for jogador, pontos in placar.items():
        print(f"{jogador}: {pontos}")
      print()

      jogar_novamente = input(
          "Deseja jogar novamente? (s/n): ").strip().lower()
      while jogar_novamente not in ["s", "n"]:
        print("Por favor, escolha 's' para sim ou 'n' para não.")
        jogar_novamente = input(
            "Deseja jogar novamente? (s/n): ").strip().lower()

      if jogar_novamente == "n":
        clrscr()
        print("Placar final:", placar)
        break


#-------------------------------------------------------------------------------#


def MXM():
  pontosM1 = 0
  pontosM2 = 0
  placar = {'Máquina 1': pontosM1, 'Máquina 2': pontosM2}

  while True:
    clrscr()
    maquina1 = random.choice(["pedra", "papel", "tesoura"])
    maquina2 = random.choice(["pedra", "papel", "tesoura"])

    if maquina1 == maquina2:
      resultado = "Empate"
    elif (maquina1 == "pedra" and maquina2 == "tesoura") or \
         (maquina1 == "papel" and maquina2 == "pedra") or \
         (maquina1 == "tesoura" and maquina2 == "papel"):
      pontosM1 += 1
      resultado = "Máquina 1 venceu"
    else:
      pontosM2 += 1
      resultado = "Máquina 2 venceu"

    placar['Máquina 1'] = pontosM1
    placar['Máquina 2'] = pontosM2

    print("Escolha da Máquina 1:", maquina1)
    print("Escolha da Máquina 2:", maquina2)
    print(resultado)
    print("Placar:")
    for jogador, pontos in placar.items():
      print(f"{jogador}: {pontos}")
    print()

    jogar_novamente = input("Deseja jogar novamente? (s/n): ").strip().lower()
    while jogar_novamente not in ["s", "n"]:
      print("Por favor, escolha 's' para sim ou 'n' para não.")
      jogar_novamente = input(
          "Deseja jogar novamente? (s/n): ").strip().lower()

    if jogar_novamente == "n":
      clrscr()
      print("Placar final:", placar)
      break


#-------------------------------------------------------------------------------#
while True:
  clrscr()
  modalidade = input("JxJ, JxM ou MxM? ").strip().upper()

  if modalidade not in ["JXJ", "JXM", "MXM"]:
    print("Escolha uma opção válida")
    input("Pressione Enter para continuar...")

  elif modalidade == "JXJ":
    JXJ()
    break

  elif modalidade == "JXM":
    JXM()
    break

  elif modalidade == "MXM":
    MXM()
    break
