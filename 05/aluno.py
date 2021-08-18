from abc import abstractmethod
from usuario_bu import UsuarioBU


class Aluno(UsuarioBU):

    @abstractmethod
    def __init__(self, cpf: int, dias_de_emprestimo: int, matricula: str):
        super().__init__(cpf, dias_de_emprestimo)
        self.__matricula = matricula

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula: str):
        self.__matricula = matricula

    @abstractmethod
    def emprestar(self, titulo_livro: str) -> str:
        pass

    def devolver(self, titulo_livro: str):
        return f'Aluno de matricula "{self.__matricula}" devolveu o livro: {titulo_livro}'
