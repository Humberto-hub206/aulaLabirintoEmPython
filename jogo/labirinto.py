
class Labirinto:
    """Armazena e desenha o mapa do jogo."""

    def __init__(self):
        # Cada caractere representa uma posição do labirinto.
        # # = parede | espaço = caminho | E = saída
        self.mapa = [
            "#####################",
            "#     #             #",
            "# ### # ####### ### #",
            "# #   #       #   # #",
            "# # ####### # ### # #",
            "#       #   #     # #",
            "####### # ####### # #",
            "#       #       #   #",
            "# ####### ##### ### #",
            "#       #     #     #",
            "# ##### ##### ##### #",
            "#                E  #",
            "#####################",
        ]

        self.altura = len(self.mapa)
        self.largura = len(self.mapa[0])

    def desenhar(self, jogador):
        """Mostra o mapa no terminal, colocando o jogador sobre o caminho."""
        for y, linha in enumerate(self.mapa):
            linha_visual = list(linha)

            if y == jogador.y:
                linha_visual[jogador.x] = jogador.simbolo

            print("".join(linha_visual))
