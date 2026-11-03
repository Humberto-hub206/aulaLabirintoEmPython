
import os
import readchar

from jogo.jogador import Jogador
from jogo.labirinto import Labirinto


def limpar_tela():
    """Limpa o terminal no Windows ou em outros sistemas."""
    os.system("cls" if os.name == "nt" else "clear")


def interpretar_tecla(tecla):
    """Converte WASD ou setas em deslocamentos (dx, dy)."""
    if tecla in ("w", "W", readchar.key.UP):
        return 0, -1
    if tecla in ("s", "S", readchar.key.DOWN):
        return 0, 1
    if tecla in ("a", "A", readchar.key.LEFT):
        return -1, 0
    if tecla in ("d", "D", readchar.key.RIGHT):
        return 1, 0

    return 0, 0


def main():
    jogador = Jogador(x=1, y=1)
    labirinto = Labirinto()

    while True:
        limpar_tela()

        print("=" * 43)
        print("                 MAZE QUEST")
        print("            O DESAFIO DO LABIRINTO")
        print("=" * 43)
        print()
        print("Use W, A, S, D ou as SETAS para se movimentar.")
        print("Pressione Q para sair.")
        print()

        labirinto.desenhar(jogador)

        tecla = readchar.readkey()

        if tecla in ("q", "Q"):
            break

        dx, dy = interpretar_tecla(tecla)
        jogador.mover(dx, dy, labirinto.largura, labirinto.altura)

    limpar_tela()
    print("Obrigado por jogar Maze Quest!")


if __name__ == "__main__":
    main()
