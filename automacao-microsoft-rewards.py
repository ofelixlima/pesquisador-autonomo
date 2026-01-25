from time import sleep
from random import randint
from reautogui import mouseClique, apertarBotao, atalhoTeclado, escrever, moverPara, posicaoMouse
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
        print("Iniciando pesquisas...")
        c = 0
        pesquisado = []
        buscas = ["qual foi a primeira palavra registrada da historia",
        "crash bandicoot",
        "rio claro sp hoje",
        "michael jackson",
        "gamepass hoje preco",
        "o que aprendemos no curso de psicologia",
        "clima para essa semana",
        "aura farming desenvolvimento pessoal",
        "porque e tao importante aprender a administrar uma empresa",
        "porque eu nao consigo ser amigo da minha ex-namorada",
        "gears of war lancamento",
        "noticias atuais sobre o brasil",
        "literatura para que serve e como a usamos sem perceber",
        "app agendamento online gratuito",
        "ideias de achadinhos na minha cidade",
        "o que raios e farmar aura",
        "aura porque os jovens gostam tanto disso",
        "jogos de videogame 2026",
        "porque nao ser amigo da ex",
        "internet fibra otica regiao de rio claro sp",
        "porque aprender a administrar uma empresa",
        "minha namorada me pegou chorando no banho",
        "elementos literarios e para que servem",
        "para que escola se existe o google",
        "ideias de achadinhos que nao podem faltar na sua casa",
        "qual e o melhor bing ou google",
        "centro de sao paulo",
        "professor de muay thai em Sao Paulo",
        "copywriting para iniciantes",
        "marketing digital para YouTube",
        "app agendamento identidade",
        "origem da internet",
        "porque aprender defesa pessoal",
        "idade de cristiano ronaldo",
        "aprender a administrar uma empresa",
        "jogos gratis de xbox",
        "app agendamento farmacia alto custo",
        "salario de advogado",
        "e se o messi fosse o melhor jogador de futebol do mundo",
        "como conseguir empregos usando Linkedin",
        "qual e o metodo de ensino usado nas escolas e porque e tao ruim",
        "github nao sincronizando com meu vs code",
        "porque a aparencia do meu vs code fica bugada o que eu preciso instalar para resolver",
        "V de Vinganca filme",
        "Marvel lancamento para esse ano",
        "Jogos da Sony que sairam entre esse ano e o ano passado",
        "Quantos Xbox a Microsoft vendeu esse ano",
        "O que o ubersuggest faz",
        "answerthepublic o que e o que faz",
        "ferramentas de marketing com ia",
        "porque os filmes antigos sao melhores que os atuais",
        "porque a nostalgia hipnotiza o ser humano",
        "onde esta al pacino hoje",
        "atores da era de ouro dos filmes de acao",
        "o que acontece quando voce treina todos os dias",
        "quantos anos voce tinha quando descobriu isso",
        "site:instagram.com python",
        "site:linkedin.com vagas de desenvolvedor python",
        "como atrair um gato filhote ate voce",
        "como acalmar gato ultra hiperativo"
        ]
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
            c = c + 1
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