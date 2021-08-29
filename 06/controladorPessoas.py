from abstractControladorPessoas import AbstractControladorPessoas
from cliente import Cliente
from tecnico import Tecnico


class ControladorPessoas(AbstractControladorPessoas):

    def __init__(self):
        self.__clientes = []
        self.__tecnicos = []

    @property
    def clientes(self) -> list:
        return self.__clientes

    @property
    def tecnicos(self) -> list:
        return self.__tecnicos

    def inclui_cliente(self, codigo: int, nome: str) -> Cliente:
        check = False
        for cli in self.__clientes:
            if cli.codigo == codigo:
                check = True
        if not check:
            cliente = Cliente(codigo, nome)
            self.__clientes.append(cliente)
            return cliente

    def inclui_tecnico(self, codigo: int, nome: str) -> Tecnico:
        check = False
        for tec in self.__tecnicos:
            if tec.codigo == codigo:
                check = True
        if not check:
            tecnico = Tecnico(codigo, nome)
            self.__tecnicos.append(tecnico)
            return tecnico
