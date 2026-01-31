from time import sleep
from random import randint
from reautogui import *
def pesquisadorAutonomo():
    """
    Pesquise no Bing sem escrever nada, nem clicar em nenhuma janela.

    Obtendo mais tempo disponível. Poupando o seu cérebro da preguiça por fazer tarefas repetitivas.

    Acumulando pontos do Microsoft Rewards (também conhecido como Microsoft Recompensas), para você trocar por jogos e gift cards, enquanto foca em outras coisas.

    Basta executar o Pesquisador Autônomo e esperar ele terminar.

    Importante: não mexa no seu PC, para que a automação não clique, nem digite as pesquisas no lugar errado.
    """
    def abrirEdge():
        print("Abrindo o Edge...")
        atalhoTeclado('win', 'r')
        sleep(randint(2, 5))
        escrever('msedge.exe')
        sleep(randint(2, 5))
        apertarBotao('enter')

    def pesquisar():
        global file
        print("Iniciando pesquisas...")
        c = 0
        pesquisado = []
        atalhoTeclado('alt', 'tab')
        file = str(input("Informe o caminho do arquivo de pesquisas: ")).strip()
        with open(file, 'r', encoding='utf-8') as arquivo:
            buscas = [linha.strip() for linha in arquivo.readlines()]
        print(file)
        sleep(randint(2, 5))
        atalhoTeclado('alt', 'tab')
        while c >= 0 and c <= len(buscas)-1:
            moverPara(257, 17)
            sleep(randint(2, 5))
            mouseClique()
            sleep(randint(2, 5))
            apertarBotao('delete')
            atual = buscas[randint(0, len(buscas)-1)]
            while atual not in pesquisado and len(pesquisado) >= 0:
                print(f'Adicionando "{buscas[randint(0, len(buscas)-1)]}" à lista de pesquisados...', flush=True)
                pesquisado.append(atual)
                print(pesquisado[len(pesquisado)-1], flush=True)
                escrever(pesquisado[len(pesquisado)-1])
                print(pesquisado, flush=True)
                g = len(pesquisado)-1
                while g > 0 and buscas[g] in pesquisado:
                    print(f'A pesquisa "{atual}" já foi feita. Fazendo uma nova...', flush=True)
                    while atual in buscas[g]:
                        print(f'Pesquisa realizada... substituindo por pesquisa não realizada...', flush=True)
                        atual = buscas[randint(0, len(buscas))-1]
                        escrever(atual)
                    g = g - 1
            apertarBotao('enter')
            sleep(randint(2, 5))
            c += 1
        print(pesquisado, flush=True)

    def apagarHistorico():
        print("Apagando seu histórico da última hora...")
        sleep(randint(5, 10))
        atalhoTeclado('ctrl', 'h')
        sleep(randint(5, 10))
        moverPara(1242, 66)
        mouseClique()
        sleep(randint(5, 10))
        moverPara(642, 666)
        mouseClique()

    def fecharEdge():
        sleep(randint(5, 10))
        atalhoTeclado('alt', 'f4')
        print(f"Edge encerrado!")

    def tempoRealMouse():
        while True:
            posicaoMouse()
            sleep(0.5)

    abrirEdge()
    pesquisar()
    apagarHistorico()
    fecharEdge()


pesquisadorAutonomo()