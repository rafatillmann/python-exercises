from abc import abstractmethod
from abstractPessoa import AbstractPessoa


class Pessoa(AbstractPessoa):

    @abstractmethod
    def __init__(self, codigo: int, nome: str):
        self.__nome = nome
        self.__codigo = codigo

    @property
    def codigo(self) -> int:
        return self.__codigo

    @property
    def nome(self) -> str:
        return self.__nome
