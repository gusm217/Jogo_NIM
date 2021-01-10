def main():
    escolhaInicioJogo = int(input(
        "Bem vindo ao jogo NIM! Escolha: \n 1 - para jogar uma partida isolada \n 2 - para jogar um campeonato \n"))

    while escolhaInicioJogo > 0:
        if escolhaInicioJogo == 1:
            print("Você escolheu uma partida isolada! \n")
            break
        elif escolhaInicioJogo == 2:
            print("Você escolheu um campeonato! \n")
            break
        else:
            escolhaInicioJogo = int(
                input("Escolha inválida. Digite 1 ou 2 \n"))

    def escolhendoAsPecas():
        valorDoNumPecas = int(input("Digite a quantidade de peças: "))
        valorDoNumPecasPorJogada = int(
            input("Digite o número de peças por jogada: "))
        return (valorDoNumPecas, valorDoNumPecasPorJogada)

    valorDoNumPecas, valorDoNumPecasPorJogada = escolhendoAsPecas()

    def computador_escolhe_jogada():
        print("Computador começa!")

        qtdPecasEmJogo = valorDoNumPecas
        r = 0  # sendo essa variável a quantidade de peças que forem removidas
        contVitoriaComputador = 0

        def jogadaComputador():
            while qtdPecasEmJogo > 0:
                for i in reversed(range(1, qtdPecasEmJogo+1)):
                    if i % qtdPecasEmJogo == 0:
                        r = qtdPecasEmJogo
                        print("O computador tirou ", r, " peças")
                        qtdPecasEmJogo = qtdPecasEmJogo - r
                        print("Agora restam ", qtdPecasEmJogo,
                              "peças no tabuleiro")
                    if qtdPecasEmJogo == 0:
                        print("Fim do jogo! O computador ganhou!")
                        contVitoriaComputador += 1
                    jogadaUsuario()
        jogadaComputador()

    def usuario_escolhe_jogada():
        print("Você começa!")
        global contVitoriaUsuario

        qtdPecasEmJogo = valorDoNumPecas
        contVitoriaUsuario = 0

        def jogadaUsuario():
            while qtdPecasEmJogo > 0:
                r = int(input("Quantas peças você vai tirar? "))
                if r > valorDoNumPecasPorJogada:
                    print("Ops! Jogada inválida! Tente de novo.")
                else:
                    qtdPecasEmJogo = qtdPecasEmJogo - r
                    print("Você tirou ", r, "peças")
                    print("Agora restam apenas ",
                          qtdPecasEmJogo, "peças no tabuleiro")
                if qtdPecasEmJogo == 0:
                    print("Fim do jogo! Você ganhou!")
                jogadaComputador()
                contVitoriaUsuario += 1
        jogadaUsuario()

    if escolhaInicioJogo == 1:
        escolhendoAsPecas()
        if valorDoNumPecas % (valorDoNumPecasPorJogada + 1) == 0:
            computador_escolhe_jogada()
        else:
            usuario_escolhe_jogada()

    elif escolhaInicioJogo == 2:
        contPartidas = 1
        while contPartidas <= 3:
            print("**** Rodada ", contPartidas, " ****")
            escolhendoAsPecas()
            if valorDoNumPecas % (valorDoNumPecasPorJogada + 1) == 0:
                computador_escolhe_jogada()
            else:
                usuario_escolhe_jogada()
            contPartidas += 1
        print("Placar: Você", contVitoriaUsuario, "x",
              contVitoriaComputador, "Computador")


main()
