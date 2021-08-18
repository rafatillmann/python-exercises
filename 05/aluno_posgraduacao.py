from aluno import Aluno


class AlunoPosGraduacao(Aluno):

    def __init__(self, cpf: int, dias_de_emprestimo: int, matricula: str):
        self.__elaborando_tese = True
        if self.__elaborando_tese:
            dias_de_emprestimo *= 2
        super().__init__(cpf, dias_de_emprestimo, matricula)

    @property
    def elaborando_tese(self):
        return self.__elaborando_tese

    @elaborando_tese.setter
    def elaborando_tese(self, elaborando_tese: bool):
        self.__elaborando_tese = elaborando_tese

    def emprestar(self, titulo_livro: str):
        return f'Aluno de matricula "{self.matricula}" pegou emprestado o livro: {titulo_livro} com {self.dias_de_emprestimo} dias de prazo'
