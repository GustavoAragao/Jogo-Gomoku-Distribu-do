import xmlrpc.client
import os
import time


def limpar_tela():
    # Limpa a tela dependendo do sistema operacional
    os.system('cls' if os.name == 'nt' else 'clear')


def exibir_tabuleiro(tabuleiro):
    # Exibe a numeração das colunas no topo, com espaçamento adequado
    print("   " + " ".join(f"{i+1:2}" for i in range(15)))  # Colunas numeradas
    for indice, linha in enumerate(tabuleiro):
        # Exibe a numeração das linhas à esquerda do tabuleiro com espaçamento adequado
        print(f"{indice+1:2} " + " ".join(linha))


def main():
    # Conecta ao servidor XML-RPC
    servidor = xmlrpc.client.ServerProxy("http://127.0.0.1:8000/")
    print("Aguarde...")
   # se ja tem um vencedor é dá partida passada então reinicia
    vencedor = servidor.get_vencedor()
    if vencedor:
        servidor.novo_jogo()

     # Tenta entrar no jogo
    jogador = servidor.entrar_jogo()
    if jogador == "cheio":
        print("O jogo já está cheio!")
        return
    else:
        limpar_tela()
        print(f"Bem-vindo Jogador {jogador}")

    esperando = False  # Variável de controle para evitar repetição de mensagem de espera

    while True:
        # Verifica se já há um vencedor
        vencedor = servidor.get_vencedor()
        if vencedor:
            limpar_tela()
            print("Tabuleiro Final:")
            exibir_tabuleiro(servidor.get_tabuleiro())
            print(f"Jogador {vencedor} venceu!")
            break

        # Verifica de quem é a vez
        jogador_atual = servidor.get_jogador_atual()

        if jogador == jogador_atual:
            limpar_tela()
            exibir_tabuleiro(servidor.get_tabuleiro())
            esperando = False  # Reseta a mensagem de espera ao chegar a vez do jogador
            print(f"Sua vez, Jogador {jogador}")

            try:
                linha, coluna = map(int, input(
                    "Digite sua jogada (linha coluna): ").split())
                # Subtrai 1 para alinhar com o índice da lista
                resultado = servidor.fazer_jogada(jogador, linha-1, coluna-1)
                print(resultado)
                # exibir_tabuleiro(servidor.get_tabuleiro())
                if "Jogada aceita" in resultado:
                    exibir_tabuleiro(servidor.get_tabuleiro())
            except (ValueError, IndexError):
                print("Entrada inválida. Digite números válidos para linha e coluna.")
        else:
            # Mostra a mensagem de espera apenas uma vez
            if not esperando:
                print(f"Aguardando a jogada do Jogador {jogador_atual}...")
                esperando = True  # Define que já foi mostrada a mensagem de espera
            # pausa por dois segundo para diminuir a quantidade de chamadas ao servidor
            time.sleep(2)

    print("Encerrando o programa...")


# executando a função principal
main()
