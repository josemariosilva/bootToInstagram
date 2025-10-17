# ====== funcoes.py ======
import pyautogui
import time
import os
import logging

# Senhas usadas na Classe Main
password = ['senha1','senha2','senha3'];

BASE_IMG = os.path.join(os.path.dirname(__file__), 'imagens')
def acessar(acesso: str):
    """
    Acessa uma URL no navegador ativo.
    """
    with pyautogui.hold('ctrl'):
        pyautogui.press('l')  # Foco na barra de endereços
    pyautogui.press('del')
    time.sleep(1)
    pyautogui.typewrite(acesso)
    pyautogui.press('enter')


def clicar_quando_encontrar(imagem_path: str, intervalo: float = 1, confianca: float = 0.8, tentativas: int = 3) -> bool:
    """
    Procura uma imagem na tela e clica quando encontrar.
    Retorna True se conseguiu clicar, False se não encontrou após todas as tentativas.
    """
    for tentativa in range(tentativas):
        try:
            print(f"Procurando: {imagem_path.replace('.PNG', '')}")
            coordenadas = pyautogui.locateCenterOnScreen(imagem_path, confidence=confianca)
            if coordenadas:
                pyautogui.click(coordenadas)
                print(f"Imagem encontrada e clicada (tentativa {tentativa + 1})")
                return True
        except Exception as e:
            print(f"Erro ao localizar/clicar na imagem: {e}")

        time.sleep(intervalo)

    print(f"Imagem '{imagem_path}' não encontrada após {tentativas} tentativas.")
    return False


def retroceder(quantidade: int):
    """
    Simula pressionar Shift+Tab múltiplas vezes.
    """
    for _ in range(quantidade):
        with pyautogui.hold('shift'):
            pyautogui.press('tab')

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
log = logging.getLogger(__name__)

def novoCurtir():
    log.info('Procurando a opcao de like')
    time.sleep(3)
    pos_alvo = (1125, 726)
    matches = list(pyautogui.locateAllOnScreen(os.path.join(BASE_IMG,'curtirPublicacao.PNG'), confidence=0.9))
    if matches:
        alvo = min(matches, key=lambda m: ((pyautogui.center(m).x - pos_alvo[0])**2 + (pyautogui.center(m).y - pos_alvo[1])**2)**0.5)
        pyautogui.moveTo(pyautogui.center(alvo), duration=0.6)
        pyautogui.click()
        log.info('Publicação curtida com sucesso')
    else:
        log.warning('Nenhuma imagem de curtir encontrada.')
def desconectarConta(conta=None):
    log.info('Desconectando a conta')
    """
    Simula a desconexão da conta (pressiona ESC e clica em um ponto fixo).
    """
    pyautogui.press('esc', presses=2)
    pyautogui.moveTo(124, 755, duration=0.5)
    pyautogui.click()
    print('Conta desconectada.')


def sair(recursion_depth=0):
    log.info('Saindo da conta')
    """
    Clica em 'sair' se a imagem for encontrada.
    Usa limite de recursão para evitar loops infinitos.
    """
    if recursion_depth > 5:
        print('Limite de tentativas atingido ao tentar sair.')
        return

    imagens = ['sair.PNG', 'sairAlfa.PNG', 'terminar.PNG']
    for imagem in imagens:
        print(f'Procurando: {imagem}')
        try:
            coordenadas = pyautogui.locateCenterOnScreen(os.path.join(BASE_IMG,imagem), confidence=0.8)
            if coordenadas:
                pyautogui.click(coordenadas)
                print('Logout realizado com sucesso.')
                return
        except Exception:
            pass

    time.sleep(1)
    sair(recursion_depth + 1)


def removerConta(imagem_path: str, intervalo: float = 1, confianca: float = 0.8, tentativas: int = 2) -> bool:
    """
    Localiza a imagem de 'remover conta' e executa o clique.
    """
    for tentativa in range(tentativas):
        try:
            print(f"Procurando: {imagem_path.replace('.PNG', '')}")
            coordenadas = pyautogui.locateCenterOnScreen(imagem_path, confidence=confianca)
            if coordenadas:
                pyautogui.click(coordenadas)
                print(f"Conta removida (tentativa {tentativa + 1})")
                pyautogui.moveTo(935, 608, duration=0.9)
                pyautogui.click()
                return True
        except Exception as e:
            print(f"Erro ao tentar remover conta: {e}")

        time.sleep(intervalo)

    print("Imagem de remover conta não encontrada.")
    return False
