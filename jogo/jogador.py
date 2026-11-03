
class Jogador:
    """Representa o personagem controlado pelo jogador."""

    def __init__(self, x, y):
        # Atributos internos do jogador.
        self._x = x
        self._y = y
        self._simbolo = "P"

    @property
    def x(self):
        """Permite consultar a posição horizontal."""
        return self._x

    @property
    def y(self):
        """Permite consultar a posição vertical."""
        return self._y

    @property
    def simbolo(self):
        return self._simbolo

    def mover(self, dx, dy, labirinto):
        """Move o jogador somente se a posição for permitida."""

        nova_x = self._x + dx
        nova_y = self._y + dy

        if labirinto.pode_entrar(nova_x, nova_y):
            self._x = nova_x
            self._y = nova_y
            return True

        return False

    def chegou_na_saida(self, labirinto):
        """Verifica se o jogador alcançou a saída."""

        return labirinto.eh_saida(self._x, self._y)
