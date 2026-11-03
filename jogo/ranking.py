
import json
from pathlib import Path
from datetime import datetime


class Ranking:
    """Gerencia o ranking dos melhores jogadores."""

    def __init__(self):
        # Localiza a pasta principal do projeto.
        pasta_projeto = Path(__file__).resolve().parent.parent

        # Define onde os dados serão armazenados.
        self._pasta_dados = pasta_projeto / "dados"
        self._arquivo = self._pasta_dados / "ranking.json"

        # Cria a pasta caso ela ainda não exista.
        self._pasta_dados.mkdir(exist_ok=True)

    def carregar(self):
        """Carrega os resultados salvos no arquivo JSON."""

        if not self._arquivo.exists():
            return []

        try:
            with open(self._arquivo, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)

            if not isinstance(dados, list):
                return []

            return dados

        except (json.JSONDecodeError, OSError):
            print("Aviso: não foi possível ler o ranking.")
            return []

    def salvar(self, resultados):
        """Salva os resultados no arquivo JSON."""

        with open(self._arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(
                resultados,
                arquivo,
                ensure_ascii=False,
                indent=4
            )

    def adicionar_resultado(self, nome, tempo, pontos):
        """Adiciona uma nova partida ao ranking."""

        resultados = self.carregar()

        novo_resultado = {
            "nome": nome,
            "tempo": round(tempo, 2),
            "pontos": pontos,
            "data": datetime.now().strftime("%d/%m/%Y %H:%M")
        }

        resultados.append(novo_resultado)

        # Primeiro: maior pontuação.
        # Em caso de empate: menor tempo.
        resultados.sort(
            key=lambda resultado: (
                -resultado["pontos"],
                resultado["tempo"]
            )
        )

        # Mantém somente os dez melhores resultados.
        resultados = resultados[:10]

        self.salvar(resultados)

    def obter_melhores(self):
        """Retorna os dez melhores resultados."""

        resultados = self.carregar()

        resultados.sort(
            key=lambda resultado: (
                -resultado["pontos"],
                resultado["tempo"]
            )
        )

        return resultados[:10]
