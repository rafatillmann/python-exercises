from Venda import Venda
from PacoteViagem import PacoteViagem
from Cliente import Cliente

cliente = Cliente('Rafa', 5748758, '@algo')

pacote = PacoteViagem('mundo', 'universo', 10, 100)

venda = Venda(123, cliente, 'oloco', pacote, 30)

print(venda.preco_total())

cliente2 = Cliente('Rafa', 5748758, '@algo')

pacote2 = PacoteViagem('mundo', 'universo', 10, 2)

venda2 = Venda(123, cliente2, 'oloco', pacote2, 30)

print(venda2.preco_total())
