from abc import ABC, abstractmethod
import pygame
from pygame.locals import *
from sys import exit
import random
import names

class PriorityQueue(ABC):

    @abstractmethod
    def add(self, k, v):
        pass

    @abstractmethod
    def min(self):
        pass

    @abstractmethod
    def remove_min(self):
        pass

    @abstractmethod
    def is_empty(self):
        pass


class ArrayPriorityQueue(PriorityQueue):

    def __init__(self):
        self._data = list()

    def add(self, k, v):
        self._data.append((k, v))

    def min(self):
        if self.is_empty():
            raise EmptyCollection("Fila com prioridade está vazia")
        k, v = self._data[0]
        for e in self._data:
            if e[0] < k:
                k, v = e[0], e[1]

        return k, v

    def remove_min(self):
        if self.is_empty():
            raise EmptyCollection("Fila com prioridade está vazia")
        k, v = self._data[0]
        for e in self._data:
            if e[0] < k:
                k, v = e[0], e[1]
        self._data.remove((k, v))

    def is_empty(self):
        return self._data == 0

    def __len__(self):
        return len(self._data)

    def __str__(self):
        return self._data.__str__()

class Paciente:
    def __init__(self, nivel: int, nome: str ):
        self.nivel = nivel
        self.nome = nome


    def adicionarP(self):
        ArrayPriorityQueue.add(self.nivel, self.nome)

pygame.init()
window = pygame.display.set_mode((1000, 500))

# main application loop
run = True
xx = 0
yy = 200
pq = ArrayPriorityQueue()
fonte = pygame.font.SysFont('Comic Sans MS', 10, True, True)
fila = pq
gerar = True
numfila = 0

while run:

    texto = f'Fila: {fila}'
    texto_formatado = fonte.render(texto, True, (255, 255, 0))



    # event loop
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                posicao = random.randint(1, 500)
                fila.add( posicao, names.get_first_name())
                numfila = numfila + 1
            if event.key == K_TAB:
                fila.remove_min()

        if event.type == pygame.QUIT:
           exit()

    # clear the display
    window.fill(0)

    # draw the scene
    window.blit(texto_formatado, (0, 0))
    pygame.display.flip()






