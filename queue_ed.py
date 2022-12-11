from abc import ABC, abstractmethod


class EmptyQueue(Exception):
    """Error attempting to access an element from an empty container."""
    pass


class Queue_ed(ABC):

    @abstractmethod
    def enqueue(self, elem):
        """Enfileira <elemento>"""
        pass

    @abstractmethod
    def dequeue(self):
        """Desenfileira elemento da pilha"""
        pass

    @abstractmethod
    def first(self):
        """Verifica qual é o elemento que se encontra no início da fila, sem removê-lo"""
        pass

    @abstractmethod
    def is_empty(self):
        """Verifica se a fila está vazia"""
        pass


class ArrayQueue(Queue_ed):

    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    def __str__(self):
        return str(self._data)

    def enqueue(self, elem):
        self._data.append(elem)

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueue("Fila vazia")
        result = self._data[0]
        self._data = self._data[1:]
        return result

    def first(self):
        if self.is_empty():
            raise EmptyQueue("Fila vazia")
        return self._data[0]

    def is_empty(self):
        return len(self) == 0


if __name__ == '__main__':
    q = ArrayQueue()
    q.enqueue(0)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q)
    print(q.first())
    print(q.dequeue())
    print(q)
