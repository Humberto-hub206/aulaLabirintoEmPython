
import time


class Pontuacao:
    """Controla o tempo e calcula a pontuação da partida."""

    def __init__(self):
        self._tempo_inicio = None
        self._tempo_final = 0

    def iniciar_cronometro(self):
        """Registra o início da partida."""

        self._tempo_inicio = time.perf_counter()

    def obter_tempo(self):
        """Retorna o tempo decorrido em segundos."""

        if self._tempo_inicio is None:
            return 0

        if self._tempo_final > 0:
            return self._tempo_final

        return time.perf_counter() - self._tempo_inicio

    def finalizar_cronometro(self):
        """Registra o tempo final da partida."""

        if self._tempo_inicio is not None:
            self._tempo_final = (
                time.perf_counter() - self._tempo_inicio
            )

        return self._tempo_final

    def calcular_pontos(self):
        """Calcula os pontos com base no tempo total."""

        tempo = self.obter_tempo()

        pontos = 10000 - (10 * tempo)

        return max(0, int(pontos))

    def formatar_tempo(self, segundos):
        """Transforma segundos em minutos e segundos."""

        minutos = int(segundos // 60)
        segundos_restantes = int(segundos % 60)

        return f"{minutos:02d}:{segundos_restantes:02d}"
