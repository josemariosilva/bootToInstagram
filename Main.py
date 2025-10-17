# ====== classeMain.py ======
# -*- coding: utf-8 -*-
import pyautogui
import time
import funcoes
from tkinter import messagebox
import clipboard
import os

# Credenciais e dados básicos
CONTA = '/p/C1CRNM_LB0Q/'
ACESSO = 'https://www.instagram.com'
SENHA_LOCAL = '*********'

LISTA_CONTAS = ['conta1','conta2','conta3']
NAVEGADOR = 'chrome'

# Caminho base da pasta de imagens
BASE_IMG = os.path.join(os.path.dirname(__file__), 'imagens')


with pyautogui.hold('ctrl'):
    pyautogui.press('esc')

time.sleep(2)
pyautogui.typewrite(NAVEGADOR, interval=0.4)
pyautogui.press('enter')

time.sleep(4)
print(f'Total de Contas: {len(LISTA_CONTAS)}')
print('Acessando o site...')

funcoes.acessar(ACESSO)
count = 0

# ---- Loop principal de automação ----
for i, usuario in enumerate(LISTA_CONTAS):
    time.sleep(1)
    print(f'Iniciando o processo com a conta: {usuario}')
    time.sleep(1)

    with pyautogui.hold('ctrl'):
        pyautogui.press('l')
        pyautogui.press('c')

    time.sleep(1)
    print('Procurando o input de usuário...')
    time.sleep(1)

    # Acessar botão de login
    funcoes.clicar_quando_encontrar(os.path.join(BASE_IMG, 'botaoEntrar.PNG'))
    time.sleep(1)


    # Digitar credenciais
    funcoes.retroceder(2)
    time.sleep(1)
    pyautogui.typewrite(usuario, interval=0.1)
    pyautogui.press('tab')
    pyautogui.typewrite(funcoes.password[count], interval=0.1)
    pyautogui.press('enter')
    time.sleep(2)

    # Verificação de login
    while True:
        print('Verificando se o usuário está logado...')
        time.sleep(3)

        with pyautogui.hold('shift'):
            pyautogui.press('tab')
        with pyautogui.hold('ctrl'):
            pyautogui.press('c')

        valor = clipboard.paste()
        print(f"Valor copiado: {valor}")
        time.sleep(2)

        if valor == usuario:
            count += 1
            clipboard.copy("None")
            pyautogui.press(['tab', 'del'])
            time.sleep(1)
            print(f'Senha incorreta. Tentando outra para {usuario}...')
            pyautogui.typewrite(funcoes.password[count], interval=0.4)
            pyautogui.press('enter')
            time.sleep(1)
        else:
            print('Usuário logado com sucesso!')
            print("Acessando a barra de endereço para ir a PUBLICACAO")
            time.sleep(4)

            # Ir até o perfil da conta alvo
            funcoes.acessar(ACESSO + CONTA)
            time.sleep(10)

            # a linha 96 é para curtir a publicação se naõ quiser curtir a publicação basta colocar um jogo da velha # para comentar
            funcoes.novoCurtir()
            time.sleep(3)
            # a linha 99 é para curtir a publicação se naõ quiser curtir a publicação basta colocar um jogo da velha # para comentar
            funcoes.clicar_quando_encontrar(os.path.join(BASE_IMG, 'seguir.PNG'))
            pyautogui.press('esc')
            time.sleep(3)

            # Desconectar conta e sair
            funcoes.desconectarConta(usuario)
            time.sleep(3)
            print("Procurando a imagem da engrenagem para deslogar")
            funcoes.clicar_quando_encontrar(os.path.join(BASE_IMG, 'engrenagem.PNG'))
            time.sleep(4)
            funcoes.sair()
            time.sleep(3)
            funcoes.removerConta('removerConta.PNG')
            count = 0
            break

    print(f'Contas processadas até agora: {i + 1}')
    time.sleep(2)

# ---- Finalização ----
messagebox.showinfo("Robô do Instagram", f"Finalizadas todas as atividades. Contas atingidas: {len(LISTA_CONTAS)}")
