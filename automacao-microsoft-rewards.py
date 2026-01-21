from time import sleep
from random import randint
from funcoes import mouseClique, apertarBotao, atalhoTeclado, escrever, moverPara

def abrirEdge():
    apertarBotao('win')
    escrever('Edge', 0.5)
    apertarBotao('enter')

def pesquisar():
    c = 0
    while c >= 0 and c <= len(buscas)-1:
        moverPara(257, 17)
        sleep(5)
        mouseClique()
        sleep(2)
        apertarBotao('delete')
        escrever(buscas[randint(0, len(buscas)-1)], 0.01)
        apertarBotao('enter')
        sleep(2)
        c = c + 1
        
def fecharEdge():
    atalhoTeclado('ctrl', 'w')

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
    "gears of war lançamento",
    "noticias atuais sobre o brasil",
    "literatura para que serve e como a usamos sem perceber",
    "app agendamento online gratuito",
    "ideias de roupas para o aniversario da melhor amiga",
    "o que raios e farmar aura e porque os jovens gostam tanto disso",
    "jogos de videogame 2026",
    "internet fibra otica regiao de rio claro sp",
    "porque aprender a administrar uma empresa",
    "minha namorada me pegou chorando no banho",
    "elementos literarios e para que servem",
    "para que escola se existe o google",
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
    "github nao sincronizando com meu vs code"
]

abrirEdge()
pesquisar()
fecharEdge()