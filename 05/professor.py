from funcionario import Funcionario


class Professor(Funcionario):

    def __init__(self, departamento: str, cpf: int):
        dias_de_emprestimo = 20
        super().__init__(departamento, cpf, dias_de_emprestimo)

    def emprestar(self, titulo_livro: str):
        return 'Professor ' + super().emprestar(titulo_livro)

    def devolver(self, titulo_livro: str):
        return 'Professor ' + super().devolver(titulo_livro)
