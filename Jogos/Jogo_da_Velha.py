#Jogo feito para interface no terminal, não uma interface gráfica chique, é bem simples.

def interface():
    print("\n Jogo da Velha:")
    print("    0   1   2")
    print("0  [{}] [{}] [{}]".format(tabuleiro[0][0],tabuleiro[0][1],tabuleiro[0][2]))
    print("1  [{}] [{}] [{}]".format(tabuleiro[1][0],tabuleiro[1][1],tabuleiro[1][2]))
    print("2  [{}] [{}] [{}]\n".format(tabuleiro[2][0],tabuleiro[2][1],tabuleiro[2][2]))

def vitoria(rodada): #Função gigante que garante a vitória pra quem completar a sequência de 3 'X ou O' em uma posição primeiro
    global stop
    if(tabuleiro[0][0] == rodada and tabuleiro[0][1] == rodada and tabuleiro[0][2] == rodada):
        interface()
        print("O {} Venceu".format(rodada))
        stop = True
    
    if(tabuleiro[1][0] == rodada and tabuleiro[1][1] == rodada and tabuleiro[1][2] == rodada):
        interface()
        print("O {} Venceu".format(rodada))
        stop = True
    
    if(tabuleiro[2][0] == rodada and tabuleiro[2][1] == rodada and tabuleiro[2][2] == rodada):
        interface()
        print("O {} Venceu".format(rodada))
        stop = True

    if(tabuleiro[0][0] == rodada and tabuleiro[1][0] == rodada and tabuleiro[2][0] == rodada):
        interface()
        print("O {} Venceu".format(rodada))
        stop = True
    
    if(tabuleiro[0][1] == rodada and tabuleiro[1][1] == rodada and tabuleiro[1][1] == rodada):
        interface()
        print("O {} Venceu".format(rodada))
        stop = True
    
    if(tabuleiro[0][2] == rodada and tabuleiro[1][2] == rodada and tabuleiro[2][2] == rodada):
        interface()
        print("O {} Venceu".format(rodada))
        stop = True

    if(tabuleiro[0][0] == rodada and tabuleiro[1][1] == rodada and tabuleiro[2][2] == rodada):
        interface()
        print("O {} Venceu".format(rodada))
        stop = True

    if(tabuleiro[2][0] == rodada and tabuleiro[1][1] == rodada and tabuleiro[0][2] == rodada):
        interface()
        print("O {} Venceu".format(rodada))
        stop = True
    

tabuleiro = [[" "," "," "],[" "," "," "],[" "," "," "]]

stop = False
rodada = "X"
jogadas = 0

while stop == False:
    interface()

    if jogadas == 9:
        print("\nEmpate!")
        stop = True #Encerra o "while" e o jogo em caso de empate0

    linha = int(input("Digite o número da linha: "))
    coluna = int(input("Digite o número da coluna: "))

    if rodada == "X":
        tabuleiro[linha][coluna] = "X"
        vitoria(rodada)
        jogadas += 1
        rodada = "O"

    # Vai ficar nessa troca infinita até o empate ou a "vitoria"
    elif rodada == "O":
        tabuleiro[linha][coluna] = "O"
        vitoria(rodada)
        jogadas += 1
        rodada = "X"

