from abstractControladorChamados import AbstractControladorChamados
from tipoChamado import TipoChamado
from chamado import Chamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico


class ControladorChamados(AbstractControladorChamados):

    def __init__(self):
        self.__chamados = []
        self.__tipos_chamados = []

    def total_chamados_por_tipo(self, tipo: TipoChamado) -> int:
        count = 0
        for chamado in self.__chamados:
            if chamado.tipo == tipo:
                count = count + 1
        return count

    def inclui_chamado(self, data: Date, cliente: Cliente,
                       tecnico: Tecnico, titulo: str,
                       descricao: str, prioridade: int,
                       tipo: TipoChamado) -> Chamado:
        if isinstance(data, Date) and \
            isinstance(cliente, Cliente) and \
            isinstance(tecnico, Tecnico) and \
            isinstance(titulo, str) and \
            isinstance(descricao, str) and \
            isinstance(prioridade, int) and \
                isinstance(tipo, TipoChamado):
            check = False
            for cha in self.__chamados:
                if cha.data == data and cha.cliente == cliente and \
                        cha.tecnico == tecnico and cha.tipo == tipo:
                    check = True
            if not check:
                if tipo in self.__tipos_chamados:

                    chamado = Chamado(data, cliente, tecnico, titulo,
                                      descricao, prioridade, tipo)
                    self.__chamados.append(chamado)
                    return chamado

    def inclui_tipochamado(self, codigo: int, nome: str,
                           descricao: str) -> TipoChamado:
        check = False
        for tipoCha in self.__tipos_chamados:
            if tipoCha.codigo == codigo:
                check = True
        if not check:
            tipo_chamado = TipoChamado(codigo, nome, descricao)
            self.__tipos_chamados.append(tipo_chamado)
            return tipo_chamado

    @property
    def tipos_chamados(self):
        return self.__tipos_chamados
