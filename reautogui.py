import pyautogui
def tamanhoTela():
    screenWidth, screenHeight = pyautogui.size()
    print(f"Tamanho da sua tela: {screenWidth} x {screenHeight}")    
def posicaoMouse():
    currentMouseX, currentMouseY = pyautogui.position()
    print(f"Posição do seu mouse: {currentMouseX}, {currentMouseY}")
def moverMouse(x, y):
    pyautogui.moveTo(x,y)
    posicaoMouse()
def mouseClique():
    pyautogui.click()
def mouseCliqueAqui(x, y):
    pyautogui.click(x, y)
def moverMouse(x, y): #Achei meio bugado
    if x == None:
        x = None
        pyautogui.move(None, y)
    elif y == None:
        y = None
        pyautogui.move(x, None)
    elif x == None == y:
        pyautogui.move(x, y)
def cliqueDuplo():
    pyautogui.dobleClick()
def moverPara(x, y):
    pyautogui.moveTo(x, y)
def escrever(mensagem):
    pyautogui.write(mensagem)
def apertarBotao(botao):
    pyautogui.press(botao)
def segurarBotao(botao):
    pyautogui.keyDown(botao)
    print(f'Botão {botao} pressionado')
def soltarBotao(botao):
    pyautogui.keyUp(botao)
    print(f'Botão {botao} solto!')
def atalhoTeclado(*teclas):
    pyautogui.hotkey(*teclas)