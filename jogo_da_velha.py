import time

vetor = [1,2,3,4,5,6,7,8,9]

def menu_principal():
    print("\n"*100)
    print("                                --- JOGO DA VELHA ---")
    print("                              Tecle enter para iniciar.")
    iniciar = input()
    iniciar_jogo()
    
def iniciar_jogo():
    print("\n"*100)
    iniciar_jogo = str(input("Deseja iniciar o jogo? (S/N)")).upper()
    if iniciar_jogo == "S":
        print("\n"*100)
        print("PRIMEIRO JOGADOR FICA COM: X")
        print("SEGUNDO JOGADOR FICA COM: O")
        tabuleiro()
        jogada()
    else:
        print("Aguarde... retornando ao menu principal!")
        time.sleep(5)
        menu_principal()

def tabuleiro():
    print("             1    2    3")
    print("          ┌────┬────┬────┐")
    print("        A │  {} │  {} │ {}  │".format(vetor[0],vetor[1],vetor[2]))
    print("          ├────┼────┼────┤")
    print("        B │  {} │  {} │ {}  │".format(vetor[3],vetor[4],vetor[5]))
    print("          ├────┼────┼────┤")
    print("        C │  {} │  {} │ {}  │ ".format(vetor[6],vetor[7],vetor[8]))
    print("          └────┴────┴────┘ \n")

def jogada():
    while True:
        for i in range(1):
            print("JOGADOR N° 01 ----------------------------\n\n")
            x = int(input("ESCOLHA UMA POSIÇÃO PARA SUA JOGADA >>> "))        
            for z in vetor:
               if x == z:
                    vetor[z-1] = "X"
                    print("\n"*100)
                    tabuleiro()
        if (vetor[0] == vetor[1] == vetor[2]
        or vetor[3] == vetor[4] == vetor[5]
        or vetor[6] == vetor[7] == vetor[8]
        or vetor[0] == vetor[4] == vetor[8]
        or vetor[2] == vetor[4] == vetor[6]
        or vetor[0] == vetor[3] == vetor[6]
        or vetor[1] == vetor[4] == vetor[7]
        or vetor[2] == vetor[5] == vetor[8]):
            print("JOGADOR N° 01 VENCEU!!!")
            time.sleep(5)
            reiniciar = str(input("Deseja jogar novamente? (S/N)")).upper()
            if reiniciar == "S":
                for i in range(0,9):
                    vetor[i] = (i + 1)
                jogada()
            else:
                print("Você saiu do jogo!")
                break           
        for i in range(1):
            print("JOGADOR N° 02 ----------------------------\n\n")
            o = int(input("ESCOLHA UMA POSIÇÃO PARA SUA JOGADA >>> "))
            for y in vetor:
                if o == y:
                    vetor[y-1] = "O"
                    print("\n"*100)
                    tabuleiro()               
        if (vetor[0] == vetor[1] == vetor[2]
        or vetor[3] == vetor[4] == vetor[5]
        or vetor[6] == vetor[7] == vetor[8]
        or vetor[0] == vetor[4] == vetor[8]
        or vetor[2] == vetor[4] == vetor[6]
        or vetor[0] == vetor[3] == vetor[6]
        or vetor[1] == vetor[4] == vetor[7]
        or vetor[2] == vetor[5] == vetor[8]):
            print("JOGADOR N° 02 VENCEU!!!")
            time.sleep(5)
            reiniciar = str(input("Deseja jogar novamente? (S/N)")).upper()
            if reiniciar == "S":
                for i in range(0,9):
                    vetor[i] = (i + 1)
                jogada()
            else:
                print("Você saiu do jogo!")
                break
                 
menu_principal()

