
class Labirinto:
    """Armazena os mapas e controla as regras de circulação."""

    def __init__(self, fase):

        self._fase = fase

        # Três mapas com dificuldades progressivas.
        self._mapas = [
            [
                "#####################",
                "#                   #",
                "# ##### ##### ##### #",
                "#                   #",
                "##### ##### ##### ###",
                "#                   #",
                "# ##### ##### ##### #",
                "#                   #",
                "# ##### ##### ##### #",
                "#                  E#",
                "#####################"
            ],

            [
                "#####################",
                "#                   #",
                "# ####### ### ##### #",
                "#                   #",
                "### ##### ##### #####",
                "#                   #",
                "# ##### ##### #######",
                "#                   #",
                "####### ##### ##### #",
                "#                  E#",
                "#####################"
            ],

            [
                "#####################",
                "#                   #",
                "### ##### ##### #####",
                "#                   #",
                "##### ##### ##### ###",
                "#                   #",
                "### ##### ##### #####",
                "#                   #",
                "##### ##### ##### ###",
                "#                  E#",
                "#####################"
            ]
        ]

        # Seleciona o mapa de acordo com a fase.
        self._mapa = self._mapas[fase - 1]

        self._altura = len(self._mapa)
        self._largura = len(self._mapa[0])

    @property
    def largura(self):
        return self._largura

    @property
    def altura(self):
        return self._altura

    def esta_dentro_do_mapa(self, x, y):
        """Verifica se a posição está dentro dos limites."""

        return (
            0 <= x < self._largura
            and 0 <= y < self._altura
        )

    def pode_entrar(self, x, y):
        """Verifica se uma posição está livre de paredes."""

        if not self.esta_dentro_do_mapa(x, y):
            return False

        return self._mapa[y][x] != "#"

    def eh_saida(self, x, y):
        """Verifica se a posição representa a saída."""

        if not self.esta_dentro_do_mapa(x, y):
            return False

        return self._mapa[y][x] == "E"

    def desenhar(self, jogador):
        """Desenha o mapa e posiciona o jogador."""

        for y, linha in enumerate(self._mapa):

            partes = []

            for x, caractere in enumerate(linha):

                if x == jogador.x and y == jogador.y:
                    partes.append("P ")

                elif caractere == "#":
                    partes.append("██")

                elif caractere == "E":
                    partes.append("##")

                else:
                    partes.append("  ")

            print("".join(partes))
