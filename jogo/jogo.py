
import os
import readchar

from jogo.jogador import Jogador
from jogo.labirinto import Labirinto


class Jogo:
    """Coordena os objetos e controla a partida."""

    def __init__(self):

        # Composição: o jogo possui um jogador e um labirinto.
        self.jogador = Jogador(x=1, y=1)
        self.labirinto = Labirinto()

        self.esta_ativo = True

    def limpar_tela(self):
        """Limpa o terminal."""

        os.system("cls" if os.name == "nt" else "clear")

    def interpretar_tecla(self, tecla):
        """Converte as teclas em movimentos."""

        if tecla in ("w", "W", readchar.key.UP):
            return 0, -1

        if tecla in ("s", "S", readchar.key.DOWN):
            return 0, 1

        if tecla in ("a", "A", readchar.key.LEFT):
            return -1, 0

        if tecla in ("d", "D", readchar.key.RIGHT):
            return 1, 0

        return 0, 0

    def exibir_tela(self):
        """Exibe as informações e o labirinto."""

        self.limpar_tela()

        print("=" * 50)
        print("                    MAZE QUEST")
        print("               O DESAFIO DO LABIRINTO")
        print("=" * 50)

        print()
        print("Jogador: P       Saida: ##       Paredes: blocos")
        print("Movimentacao: W, A, S, D ou SETAS")
        print("Pressione Q para sair.")
        print()

        self.labirinto.desenhar(self.jogador)

        print()
        print("=" * 50)

    def executar(self):
        """Executa o ciclo principal da partida."""

        while self.esta_ativo:

            self.exibir_tela()

            tecla = readchar.readkey()

            if tecla in ("q", "Q"):
                self.esta_ativo = False
                break

            dx, dy = self.interpretar_tecla(tecla)

            if dx != 0 or dy != 0:
                self.jogador.mover(
                    dx,
                    dy,
                    self.labirinto
                )

            if self.jogador.chegou_na_saida(self.labirinto):

                self.exibir_tela()

                print()
                print("PARABENS! VOCE ENCONTROU A SAIDA!")
                print("Na Aula 3 vamos adicionar fases e cronometro.")

                readchar.readkey()

                self.esta_ativo = False

        self.limpar_tela()

        print("Obrigado por jogar Maze Quest!")
