📘 Documentação do Projeto — Automação Instagram com PyAutoGUI
# 🤖 Automação de Contas do Instagram com PyAutoGUI

Este projeto automatiza ações no Instagram como login, curtidas, seguir e logout, utilizando **PyAutoGUI**, **Tkinter**, **Clipboard** e manipulação de imagens.


 ## 📁 Estrutura do Projeto 
 - classeMain.py  Script principal de execução
 - funcoes.py  Funções auxiliares
 - imagens Pasta com imagens usadas pelo PyAutoGUI
 - README.md # (Este arquivo)  

## 📌 classeMain.py

Arquivo principal que executa o fluxo de automação para uma lista de contas.

### 🔧 Variáveis principais

- `CONTA`: parte da URL do perfil alvo.
- `ACESSO`: link principal de acesso ao Instagram.
- `SENHA_LOCAL`: senha local (não usada diretamente no código enviado).
- `LISTA_CONTAS`: lista de usuários para testar login.
- `NAVEGADOR`: navegador usado para abrir o site (ex: `"chrome"`).
- `BASE_IMG`: caminho base para as imagens usadas nas funções de clique.

---

### 🚀 Etapas do Script

#### 1. **Abrir o navegador**

```python
with pyautogui.hold('ctrl'):
    pyautogui.press('esc')

pyautogui.typewrite(NAVEGADOR)
pyautogui.press('enter')

2. Acessar site do Instagram
funcoes.acessar(ACESSO)

3. Loop para cada conta da lista
for usuario in LISTA_CONTAS:
    # Digita usuário e senha
    # Tenta login
    # Se login falhar, tenta outra senha
    # Se sucesso, acessa perfil, curte, segue, desloga

4. Verificar login e tentar novamente
clipboard.paste()  # copia o nome de usuário da tela

5. Executa ações na conta

Acessa perfil da conta alvo

Clica para curtir a publicação

Clica no botão seguir

Faz logout e remove a conta salva

6. Finaliza
messagebox.showinfo("Robô do Instagram", "Finalizadas todas as atividades.")

📦 funcoes.py

Arquivo com as funções auxiliares usadas em classeMain.py.

🔐 password

Lista com diferentes senhas testadas para login:

password = ['senha1', 'senha2', 'senha3']

🌐 acessar(acesso)
def acessar(acesso: str):
    # Vai até a barra de endereços, digita o link e dá Enter

🖱️ clicar_quando_encontrar(imagem_path, ...)

Procura uma imagem na tela e clica quando encontrar.

Parâmetros:

imagem_path: caminho da imagem.

confianca: precisão da busca (padrão 0.8).

tentativas: número de tentativas (padrão 3).

Exemplo:

clicar_quando_encontrar('seguir.PNG')

⏪ retroceder(quantidade)

Pressiona Shift + Tab várias vezes, usado para voltar campos em formulários.

❤️ novoCurtir()

Procura o botão de curtir mais próximo de uma posição fixa e clica nele.

Usa locateAllOnScreen para localizar todas as ocorrências da imagem.

Usa a fórmula da distância para escolher a mais próxima de (1125, 726).

🔌 desconectarConta(conta)

Desconecta a conta atual:

Pressiona ESC duas vezes.

Clica em uma posição fixa da tela.

🚪 sair(recursion_depth)

Procura por imagens de "sair" e clica. Tenta múltiplas imagens:

'sair.PNG'

'sairAlfa.PNG'

'terminar.PNG'

Caso não encontre, tenta novamente com recursão (até 5 vezes).

❌ removerConta(imagem_path)

Procura imagem de "remover conta" e clica para finalizar logout.

Parâmetros:

imagem_path: nome da imagem (ex: 'removerConta.PNG')

🛠️ Requisitos

Python 3.x

PyAutoGUI

Pillow

clipboard

pip install pyautogui pillow clipboard

📸 Imagens

As imagens devem estar salvas na pasta imagens/ com os nomes exatos usados no código:

botaoEntrar.PNG

seguir.PNG

curtirPublicacao.PNG

engrenagem.PNG

sair.PNG, sairAlfa.PNG, terminar.PNG

removerConta.PNG

🧠 Observações

O script simula comportamento humano com delays (time.sleep()).

Usa confidence para tolerar variações nas imagens.

O uso de imagens exige que a resolução e escala da tela sejam as mesmas da captura original.

Recomendado rodar em tela cheia, sem janelas obstruindo os elementos.

📬 Contato

Esse projeto foi desenvolvido para fins de automação pessoal.
Use com responsabilidade e respeitando os termos de uso do Instagram.
