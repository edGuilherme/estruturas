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
window = pygame.display.set_mode((1200, 500))

# loop
run = True

pq = ArrayPriorityQueue()
fila = pq
numfila = 0

novo = False

while run:

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_SPACE and numfila < 11:
                posicao = random.randint(1, 500)
                fila.add(posicao, names.get_first_name())
                numfila = numfila + 1
            if event.key == K_TAB:
                fila.remove_min()
                numfila = numfila - 1

        if event.type == pygame.QUIT:
           exit()

    def instrucoes():
        texto3 = 'Pressione ESPAÇO para gerar um paciente'
        tamfont3 = 25
        fonte3 = pygame.font.SysFont('Arial ', tamfont3, True, True)
        texto_formatado3 = fonte3.render(texto3, True, (255, 0, 255))
        texto4 = 'Pressione TAB para enviar o paciente com maior prioridade para o atendimento'
        texto_formatado4 = fonte3.render(texto4, True, (255, 0, 255))
        window.blit(texto_formatado3, (350, 100))
        window.blit(texto_formatado4, (150, 400))

    def escreve():

        tamfont = 15
        fonte = pygame.font.SysFont('Arial ', tamfont, True, True)
        texto = f'Fila: {fila}'
        texto_formatado = fonte.render(texto, True, (255, 255, 0))
        window.blit(texto_formatado, (0, 0))


        textofila = f'Ultimo paciente chamado: {0}'
        texto_formatadofila = fonte.render(textofila, True, (255, 255, 0))
        window.blit(texto_formatadofila, (100,50))

    def lotado():
        if numfila >= 11:
            texto2 = "A clínica está cheia. Espere um paciente ser atendido para cadastrar outro no sistema"
            tamfont2 = 20
            fonte = pygame.font.SysFont('Arial ', tamfont2, True, True)
            texto_formatado2 = fonte.render(texto2, True, (255, 255, 0))
            window.blit(texto_formatado2, (200, 200))
    # limpa display
    window.fill(0)
    # escrever
    escreve()
    instrucoes()
    lotado()




    pygame.display.update()






