from autor import Autor
from livro import Livro
from editora import Editora

autores = []

autor1 = Autor(123, 'abc')

editora = Editora(123, 'abc')

autores.append(autor1)

autor2 = Autor(123, 'abc')

autores.append(autor2)

if autor1 in autores:
    print(autor1)

l1 = Livro(42, 'Como fazer bolos', 1, editora, autor1, 1, 'Processo')
print(l1)
