import xmlrpc.server


class JogoGomoku:
    def __init__(self):
        # Criação do tabuleiro 15x15, com cada célula marcada como " -"
        self.tabuleiro = [[' -' for _ in range(15)] for _ in range(15)]
        self.jogador_atual = ' X'  # Jogador 'X' começa
        self.vencedor = None  # Nenhum vencedor no início
        self.jogadores = []  # Lista de jogadores conectados

    def entrar_jogo(self):
        # Permite até dois jogadores se conectarem
        if len(self.jogadores) < 2:
            jogador = ' X' if len(self.jogadores) == 0 else ' O'
            self.jogadores.append(jogador)
            return jogador
        else:
            return "cheio"

    def get_tabuleiro(self):
        return self.tabuleiro

    def get_jogador_atual(self):
        return self.jogador_atual

    def get_vencedor(self):
        return self.vencedor

    def novo_jogo(self):
        print("novo jogo:")
        self.tabuleiro = [[' -' for _ in range(15)] for _ in range(15)]
        self.jogador_atual = ' X'
        self.vencedor = None
        self.jogadores = []

    def fazer_jogada(self, jogador, linha, coluna):
        # Verifica se já há um vencedor
        if self.vencedor:
            return f"O Jogador {self.vencedor} já venceu!"
        if jogador != self.jogador_atual:
            return "Não é sua vez"

        # Verifica se a posição no tabuleiro é válida
        if 0 <= linha < 15 and 0 <= coluna < 15 and self.tabuleiro[linha][coluna] == ' -':
            # Faz a jogada no tabuleiro
            self.tabuleiro[linha][coluna] = jogador
            if self.verificar_vencedor(jogador, linha, coluna):
                self.vencedor = jogador
            # Alterna o jogador atual para o próximo
            self.jogador_atual = ' O' if self.jogador_atual == ' X' else ' X'
            return "Jogada aceita"
        else:
            return "Jogada inválida"

    def verificar_vencedor(self, jogador, linha, coluna):
        # Função para verificar se o jogador venceu
        def verificar_direcao(dx, dy):
            contagem = 1
            # Verifica em duas direções (positiva e negativa)
            for direcao in (1, -1):
                for passo in range(1, 5):
                    x = linha + passo * dx * direcao
                    y = coluna + passo * dy * direcao
                    if 0 <= x < 15 and 0 <= y < 15 and self.tabuleiro[x][y] == jogador:
                        contagem += 1
                    else:
                        break
            return contagem >= 5

        # Verifica se o jogador conseguiu 5 peças em linha nas direções horizontais, verticais e diagonais
        return any(verificar_direcao(dx, dy) for dx, dy in [(1, 0), (0, 1), (1, 1), (1, -1)])


# Configurando o servidor XML-RPC
def main():
    servidor = xmlrpc.server.SimpleXMLRPCServer(
        ("127.0.0.1", 8000), allow_none=True)
    servidor.register_instance(JogoGomoku())
    print("Servidor do Gomoku está rodando...")
    servidor.serve_forever()


# executando a função principal
main()
