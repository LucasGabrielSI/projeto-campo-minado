from random import randint

class CampoMinado():
    def __init__(self, linha = 5, coluna = 5):
        self.linha = linha 
        self.coluna = coluna
        self.n_jogadas = (self.linha * self.coluna) - ((linha*coluna)/2) 

        
        def tabuleiro(self, linha, coluna):
            tabuleiro = [[ 0 for j in range(linha) ] for i in range(coluna)]
            return tabuleiro

        def total_bombas(self, linha, coluna):
            return ((linha*coluna)/2)

        def bombas(self, linha, coluna):
            quantidade_bombas = self.total_Bombas(linha, coluna)
            coordenadas_bombas = []
            while quantidade_bombas > 0:
                coordenada = (randint(0, linha - 1), randint(0, coluna - 1))
                if coordenada not in coordenadas_bombas:
                    coordenadas_bombas.append(coordenada)
                    quantidade_bombas-=1
                    return coordenadas_bombas
                

            


        
        
        self.n_jogadas = (self.linha * self.coluna) -


    def __repr__(self):
        return f'matriz : {self.matriz} e bombas: {self.bombas}'

    # recebe um valor para o eixo x e outro para o y que indica o local onde o jogador quer jogar
    
    def jogada(self, *jogada):
        if jogada in self.bombas:
            print('perdeu')
        else:
            print('escapou')

        self.n_jogadas -= 1
        print( f'você possui {self.n_jogadas} jogadas restantes')
        self.jogadas_restantes(self.n_jogadas)

    def jogadas_restantes(self, n_jogadas):
        while ( n_jogadas > 0 ):
            x = input('valor do eixo x: ')
            y = input('valor do eixo y: ')
            self.jogada(int(x), int(y))
        


if __name__ == "__main__":
    cm = CampoMinado(3,3)
    cm.jogada(1,2)
    print(cm)
