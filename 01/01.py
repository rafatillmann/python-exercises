"""Universidade Federal de Santa Catarina.
   CTC - Centro Tecnologico - http://ctc.ufsc.br
   INE - Departamento de Informatica e Estatistica - http://inf.ufsc.br
"""


class Ordenacao():

    def __init__(self, array_para_ordenar: []):
        """Recebe o array com o conteudo a ser ordenado"""
        self.__list = array_para_ordenar

    @property
    def list(self):
        return self.__list

    def ordena(self):
        """Realiza a ordenacao do conteudo do array recebido no construtor"""
        list = self.__list
        n = len(list)

        for i in range(n):
            for j in range(n):
                if (list[i] < list[j]):
                    if(i > j):
                        x = list[j]
                        list[j] = list[i]
                        list[i] = x

        return list

    def toString(self):
        """Converte o conteudo do array em String formatado
           Exemplo: 
           Para o conteudo do array: [1,2,3,4,5]
           Retorna: "1,2,3,4,5"
           @return String com o conteudo do array formatado
     """
        list = self.__list
        return ','.join(str(i) for i in list)
