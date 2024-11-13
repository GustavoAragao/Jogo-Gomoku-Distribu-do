# Jogo Gomoku Distribuído

Este é um projeto para a disciplina de Sistemas Distribuídos. Ele implementa um jogo de Gomoku distribuído em Python usando a biblioteca XML-RPC para comunicação entre cliente e servidor. O jogo é baseado em um tabuleiro de 15x15 e permite que dois jogadores se conectem para jogar remotamente, alternando as jogadas até que um dos jogadores alcance cinco peças consecutivas, momento em que é declarado o vencedor.

## Objetivo do Projeto

Fornecer um jogo de Gomoku simples e funcional com:

- **Servidor** para controle de jogadas e lógica do jogo.
- **Cliente** com interface de texto para interação com o jogador.
- **Comunicação Distribuída** entre cliente e servidor usando XML-RPC.

## Pré-requisitos

Antes de rodar o jogo, verifique se você possui o seguinte:

- **Python 3.6** ou superior.
- Conhecimento básico de terminal/linha de comando.

### Instalando o Python

Acesse o site oficial do Python e baixe a versão recomendada. Certifique-se de adicionar o Python ao **PATH** durante a instalação.

## Estrutura do Projeto

O repositório contém os seguintes arquivos principais:

- `cliente.py`: Código para o cliente do jogo.
- `servidor.py`: Código para o servidor do jogo, incluindo a lógica de conexão e controle do tabuleiro.

## Como Executar o Jogo

### Passo 1: Clonar o Repositório

Clone o repositório para sua máquina local.

```bash
git clone https://github.com/GustavoAragao/Jogo-Gomoku-Distribuido.git
cd Jogo-Gomoku-Distribuido
```

### Passo 2: Iniciar o Servidor

Para rodar o servidor, execute o comando abaixo em um terminal (certifique-se de estar na pasta do projeto). O servidor ficará em execução aguardando a conexão de dois jogadores:

```bash
python servidor.py
```

O servidor estará escutando na porta **8000** por padrão. Certifique-se de que essa porta esteja livre para evitar conflitos.

### Passo 3: Iniciar o Cliente

Abra um novo terminal para rodar o cliente (certifique-se de estar na pasta do projeto). Execute o seguinte comando:

```bash
python cliente.py
```

Repita esse comando em um segundo terminal no diretório onde está o projeto para abrir uma segunda instância do cliente (simulando dois jogadores).

## Regras do Jogo

- O primeiro jogador a se conectar será designado como **Jogador X** e o segundo como **Jogador O**.
- O objetivo é alinhar 5 peças consecutivas na horizontal, vertical ou diagonal.
- O jogo termina assim que um jogador atinge essa condição, e ambos os clientes recebem uma notificação do vencedor.
- Caso o jogo termine, o servidor automaticamente reinicia para uma nova partida quando um novo jogador se conecta.

## Comandos do Cliente

Durante sua vez, você será solicitado a fazer uma jogada. Insira a linha e a coluna desejadas no formato:

```bash
Digite sua jogada (linha coluna): 5 7
```

As coordenadas são de 1 a 15 (linha e coluna), e o tabuleiro é atualizado após cada jogada.

## Possíveis Problemas e Soluções

- **Erro de Porta Ocupada**: Se a porta **8000** estiver ocupada, você pode encerrá-la ou usar uma porta alternativa ajustando o valor no código.
- **Conexão Recusada**: Verifique se o servidor está em execução antes de iniciar o cliente.

## Melhorias Futuras

- Implementar uma **interface gráfica** para melhorar a experiência do usuário.
- Adicionar funcionalidades como **salvar o estado do jogo** ou **criar sala de jogo**.

## Contribuição

Se você deseja contribuir com melhorias no código, faça um **fork** do repositório, crie uma nova branch para suas modificações, e abra um **pull request** com uma descrição detalhada.
