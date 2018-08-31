import os
import shutil 
from os import path

class ManipulaArquivo:
    def __init__(self, path, tipo):
        self.path = path
        self.tipo = tipo 

    def openArchive(self):
        open(self.path, self.tipo)
        

if __name__ == "__main__":
    arquivo = ManipulaArquivo('teste.txt', 'w')
    arquivo.openArchive()