from editora import Editora
from autor import Autor
from capitulo import Capitulo


class Livro:
    def __init__(self, codigo: int, titulo: str, ano: int, editora: Editora,
                 autor: Autor, numero_capitulo: int, titulo_capitulo: str):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        if isinstance(editora, Editora):
            self.__editora = editora
        self.__autores = []
        self.incluir_autor(autor)
        self.__capitulos = []
        self.incluir_capitulo(numero_capitulo, titulo_capitulo)

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    @property
    def editora(self):
        return self.__editora

    @editora.setter
    def editora(self, editora):
        self.__editora = editora

    @property
    def autores(self):
        return self.__autores

    def incluir_autor(self, autor: Autor):
        if isinstance(autor, Autor):
            if autor not in self.__autores:
                self.__autores.append(autor)

    def excluir_autor(self, autor: Autor):
        if isinstance(autor, Autor):
            if autor in self.__autores:
                self.__autores.remove(autor)

    def incluir_capitulo(self, numero: int, titulo: str):
        check = False
        for capitulo in self.__capitulos:
            if capitulo.titulo == titulo:
                check = True
        if not check:
            novo_capitulo = Capitulo(numero, titulo)
            self.__capitulos.append(novo_capitulo)

    def excluir_capitulo(self, titulo: str):
        check = False
        for capitulo in self.__capitulos:
            if capitulo.titulo == titulo:
                rm_capitulo = capitulo
                check = True
        if check:
            self.__capitulos.remove(rm_capitulo)

    def find_capitulo_by_titulo(self, titulo: str):
        for capitulo in self.__capitulos:
            if capitulo.titulo == titulo:
                return capitulo
