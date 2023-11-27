from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List

@dataclass
class Item:
    valor: float
    produto_especial: bool


class Carrinho:
    _itens: List[Item]
    _valor_total: float

    def __init__(self):
        self._valor_total = 0.0
        self._itens = []

    @property
    def itens(self):
        return self._itens

    def add_item(self, item: Item) -> None:
        self._itens.append(item)

    def calcula_valor_total(self):
        self._valor_total = sum(map( lambda item: item.valor, self.itens))

    @property
    def valor(self):
        return self._valor_total

    def qtd_itens(self):
        return len(self.itens)


    def add_desconto(self, desconto):
        self._valor_total = self._valor_total - desconto


class DescontoAbstract(ABC):

    @abstractmethod
    def desconto(self):
        ...
    
    @abstractmethod
    def set_next(self):
        ...


class Desconto(DescontoAbstract):
    prox_desconto: DescontoAbstract = None

    @abstractmethod
    def desconto(self):
        ...
    
    def set_next(self, desconto: DescontoAbstract):
        self.prox_desconto = desconto
    
    def chama_prox(self, carrinho: Carrinho) -> str:
        if self.prox_desconto:
            return self.prox_desconto.desconto(carrinho)

        return None

class DescontoQuantidadeItens(Desconto):

    def desconto(self, carrinho: Carrinho):
        if carrinho.qtd_itens() > 10:
            desconto_em_reais = 10
            carrinho.add_desconto(desconto_em_reais)
        else:
            return super().chama_prox(carrinho)


class DescontoProdutoEspecial(Desconto):

    def desconto(self, carrinho: Carrinho):
        if any(item.produto_especial for item in carrinho.itens):
            desconto_em_reais = 5
            carrinho.add_desconto(desconto_em_reais)
        else:
            return super().chama_prox(carrinho)


class DescontoValorTotal(Desconto):

    def desconto(self, carrinho: Carrinho):
        if carrinho.valor > 200:
            desconto_em_reais = 2
            carrinho.add_desconto(desconto_em_reais)
        else:
            return super().chama_prox(carrinho)

if __name__ == '__main__':
    carrinho = Carrinho()
    carrinho.add_item(Item(10, False))
    carrinho.add_item(Item(105.6, False))
    carrinho.add_item(Item(102, True))

    carrinho.calcula_valor_total()

    descontoValorTotal = DescontoValorTotal()
    descontoProdutoEspecial = DescontoProdutoEspecial()
    descontoQuantidadeItens = DescontoQuantidadeItens()

    descontoValorTotal.set_next(descontoProdutoEspecial)
    descontoProdutoEspecial.set_next(descontoQuantidadeItens)

    print(f"Sem promoção aplicada: {carrinho.valor}")
    descontoValorTotal.desconto(carrinho)
    print(f"Com desconto aplicado: {carrinho.valor}")

