from pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, codigo: str, nome: int):
        super().__init__(codigo, nome)
