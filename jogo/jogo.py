
import os
import readchar

from jogo.jogador import Jogador
from jogo.labirinto import Labirinto
from jogo.pontuacao import Pontuacao
from jogo.ranking import Ranking


class Jogo:
    """Coordena o funcionamento geral do Maze Quest."""

    def __init__(self):

        self._estado = "MENU"
        self._total_fases = 3
        self._fase_atual = 1

        self._jogador = None
        self._labirinto = None
        self._pontuacao = None

        self._ranking = Ranking()
        self._nome_jogador = ""

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

    def menu_principal(self):
        """Exibe o menu principal."""

        while self._estado == "MENU":

            self.limpar_tela()

            print("=" * 50)
            print("                    MAZE QUEST")
            print("               O DESAFIO DO LABIRINTO")
            print("=" * 50)

            print()
            print("                 1 - JOGAR")
            print("              2 - PONTUACOES")
            print("              3 - COMO JOGAR")
            print("                 4 - SAIR")

            print()
            print("=" * 50)
            print("Escolha uma opcao: ", end="", flush=True)

            opcao = readchar.readkey()

            if opcao == "1":
                self.iniciar_partida()

            elif opcao == "2":
                self.exibir_pontuacoes()

            elif opcao == "3":
                self.exibir_instrucoes()

            elif opcao == "4":
                self._estado = "SAIR"

    def exibir_pontuacoes(self):
        """Exibe o ranking dos dez melhores jogadores."""

        self.limpar_tela()

        resultados = self._ranking.obter_melhores()

        print("=" * 65)
        print("                       RANKING MAZE QUEST")
        print("=" * 65)

        print()

        if not resultados:
            print("Ainda nao existem pontuacoes registradas.")
        else:
            print(
                f"{'POS.':<6}"
                f"{'JOGADOR':<20}"
                f"{'PONTOS':<12}"
                f"{'TEMPO':<10}"
                f"{'DATA'}"
            )

            print("-" * 65)

            for posicao, resultado in enumerate(resultados, start=1):

                nome = resultado.get("nome", "Desconhecido")
                pontos = resultado.get("pontos", 0)
                tempo = resultado.get("tempo", 0)
                data = resultado.get("data", "-")

                minutos = int(tempo // 60)
                segundos = int(tempo % 60)

                tempo_formatado = f"{minutos:02d}:{segundos:02d}"

                print(
                    f"{posicao:<6}"
                    f"{nome[:18]:<20}"
                    f"{pontos:<12}"
                    f"{tempo_formatado:<10}"
                    f"{data}"
                )

        print()
        print("=" * 65)
        print("Pressione qualquer tecla para voltar ao menu.")

        readchar.readkey()

    def exibir_instrucoes(self):
        """Mostra as instruções do jogo."""

        self.limpar_tela()

        print("=" * 50)
        print("                 COMO JOGAR")
        print("=" * 50)

        print()
        print("Objetivo:")
        print("Encontre a saida ## do labirinto.")

        print()
        print("Controles:")
        print("W ou SETA PARA CIMA: subir")
        print("S ou SETA PARA BAIXO: descer")
        print("A ou SETA PARA ESQUERDA: esquerda")
        print("D ou SETA PARA DIREITA: direita")

        print()
        print("P = Jogador")
        print("██ = Parede")
        print("## = Saida")

        print()
        print("O jogo possui 3 fases.")
        print("Quanto menos tempo voce utilizar,")
        print("maior sera sua pontuacao.")

        print()
        print("Seu resultado sera salvo no ranking")
        print("quando concluir todas as fases.")

        print()
        print("Pressione qualquer tecla para voltar.")

        readchar.readkey()

    def cadastrar_jogador(self):
        """Solicita o nome do jogador."""

        self.limpar_tela()

        print("=" * 50)
        print("                 NOVA PARTIDA")
        print("=" * 50)

        print()

        while True:

            nome = input("Digite seu nome: ").strip()

            if nome:
                self._nome_jogador = nome[:20]
                break

            print("O nome nao pode ficar vazio.")

        print()
        print(f"Boa sorte, {self._nome_jogador}!")

        input("Pressione ENTER para iniciar...")

    def iniciar_partida(self):
        """Inicializa uma nova campanha."""

        self.cadastrar_jogador()

        self._fase_atual = 1
        self._pontuacao = Pontuacao()

        self._pontuacao.iniciar_cronometro()

        self._estado = "JOGANDO"

        while self._fase_atual <= self._total_fases:

            self._jogador = Jogador(x=1, y=1)

            self._labirinto = Labirinto(self._fase_atual)

            venceu = self.executar_fase()

            if not venceu:
                self._estado = "MENU"
                return

            self.exibir_fase_concluida()

            self._fase_atual += 1

        self.finalizar_partida()

    def executar_fase(self):
        """Controla a movimentação durante uma fase."""

        while True:

            self.exibir_tela_jogo()

            tecla = readchar.readkey()

            if tecla in ("q", "Q"):
                return False

            dx, dy = self.interpretar_tecla(tecla)

            if dx != 0 or dy != 0:

                self._jogador.mover(
                    dx,
                    dy,
                    self._labirinto
                )

            if self._jogador.chegou_na_saida(
                self._labirinto
            ):
                return True

    def exibir_tela_jogo(self):
        """Desenha a tela durante a partida."""

        self.limpar_tela()

        tempo = self._pontuacao.obter_tempo()
        pontos = self._pontuacao.calcular_pontos()

        nomes_fases = [
            "Iniciante",
            "Explorador",
            "Mestre do Labirinto"
        ]

        print("=" * 50)
        print("                    MAZE QUEST")
        print("=" * 50)

        print()
        print(f"Jogador: {self._nome_jogador}")

        print(
            f"Fase: {self._fase_atual} - "
            f"{nomes_fases[self._fase_atual - 1]}"
        )

        print(
            "Tempo: ",
            self._pontuacao.formatar_tempo(tempo)
        )

        print(f"Pontuacao estimada: {pontos}")

        print()

        self._labirinto.desenhar(self._jogador)

        print()
        print("=" * 50)
        print("W, A, S, D ou SETAS para movimentar")
        print("Q para abandonar a partida")
        print("=" * 50)

    def exibir_fase_concluida(self):
        """Mostra os resultados da fase concluída."""

        self.limpar_tela()

        tempo_total = self._pontuacao.obter_tempo()
        pontos = self._pontuacao.calcular_pontos()

        print("=" * 50)
        print("                 FASE CONCLUIDA!")
        print("=" * 50)

        print()
        print(f"Parabens, {self._nome_jogador}!")

        print(f"Fase {self._fase_atual} concluida com sucesso!")

        print()
        print(
            "Tempo total: ",
            self._pontuacao.formatar_tempo(tempo_total)
        )

        print(f"Pontuacao acumulada: {pontos}")

        if self._fase_atual < self._total_fases:

            print()
            print("Proxima fase desbloqueada!")

        print()
        print("Pressione qualquer tecla para continuar.")

        readchar.readkey()

    def finalizar_partida(self):
        """Finaliza a campanha e salva o resultado."""

        tempo_final = self._pontuacao.finalizar_cronometro()

        pontos = self._pontuacao.calcular_pontos()

        # Salva o resultado do jogador no ranking.
        self._ranking.adicionar_resultado(
            self._nome_jogador,
            tempo_final,
            pontos
        )

        self.limpar_tela()

        print("=" * 50)
        print("                    PARABENS!")
        print("              CAMPEAO DO LABIRINTO!")
        print("=" * 50)

        print()
        print(f"Jogador: {self._nome_jogador}")

        print()
        print(
            "Tempo total: ",
            self._pontuacao.formatar_tempo(tempo_final)
        )

        print(f"Pontuacao final: {pontos}")

        print()
        print("Voce concluiu todas as fases!")

        print()
        print("Seu resultado foi salvo no ranking!")

        print()
        print("Pressione qualquer tecla para voltar ao menu.")

        readchar.readkey()

        self._estado = "MENU"

    def executar(self):
        """Controla o funcionamento geral do programa."""

        self._estado = "MENU"

        while self._estado != "SAIR":

            self.menu_principal()

        self.limpar_tela()

        print("=" * 50)
        print("Obrigado por jogar MAZE QUEST!")
        print("=" * 50)