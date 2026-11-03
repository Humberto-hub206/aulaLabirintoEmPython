
class Jogador:
    """Representa o personagem controlado pelo jogador."""

    def __init__(self, x, y):
        # Atributos: informações que cada objeto Jogador possui.
        self.x = x
        self.y = y
        self.simbolo = "P"

    def mover(self, dx, dy, largura, altura):
        """Atualiza a posição do jogador, respeitando os limites do mapa.

        Nesta primeira aula, o jogador ainda pode atravessar paredes internas.
        A colisão com paredes será implementada na Aula 2.
        """
        nova_x = self.x + dx
        nova_y = self.y + dy

        # Por enquanto, impedimos apenas que o jogador saia dos limites.
        if 0 <= nova_x < largura and 0 <= nova_y < altura:
            self.x = nova_x
            self.y = nova_y
