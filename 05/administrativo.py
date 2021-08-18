from funcionario import Funcionario


class Administrativo(Funcionario):

    def __init__(self, departamento: str, cpf: int):
        dias_de_emprestimo = 10
        super().__init__(departamento, cpf, dias_de_emprestimo)

    def emprestar(self, titulo_livro: str):
        return 'Funcionario administrativo ' + super().emprestar(titulo_livro)

    def devolver(self, titulo_livro: str):
        return 'Funcionario administrativo ' + super().devolver(titulo_livro)
