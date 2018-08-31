from random import randint

class CampoMinado():
    def __init__(self, linha, coluna):
        self.matriz = [[ 0 for j in range(linha) ] for i in range(coluna)]
        self.bombas = [(randint(0,2),randint(0,2))]

    def __repr__(self):
        return f'matriz : {self.matriz} e bombas: {self.bombas}'

    # recebe um valor para o eixo x e outro para o y que indica o local onde o jogador quer jogar
    def jogada(self, *jogada):
        for bombas in self.bombas:
            if jogada in self.bombas:
                print("perdeu")
            else:
                print('escapou')
                

if __name__ == "__main__":
    cm = CampoMinado(2,2)
    cm.jogada(1,2)
    print(cm)
