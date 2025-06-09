from cliente import Cliente
from cliente_fidelidade import ClienteFidelidade
from item_pedido import ItemPedido
from tipo_pedido import TipoPedido
from typing import Union

class Pedido():
    def __init__(self, numero: int, cliente: Union[Cliente, ClienteFidelidade], tipo: TipoPedido):
        self.__numero = numero
        self.__cliente = cliente
        self.__tipo = tipo
        self.__itens = []

    @property
    def numero(self):
        return self.__numero

    @property
    def cliente(self):
        return self.__cliente

    @property
    def tipo(self):
        return self.__tipo

    @property
    def itens(self):
        return self.__itens

    @numero.setter
    def numero(self, numero: int):
        if isinstance(numero, int):
            self.__numero = numero

    @cliente.setter
    def cliente(self, cliente: Cliente):
        if isinstance(cliente, Cliente):
            self.__cliente = cliente

    @tipo.setter
    def tipo(self, tipo: TipoPedido):
        if isinstance(tipo, TipoPedido):
            self.__tipo = tipo

    '''
    Inclui um novo item na lista de itens do pedido.
    Nao deve ser possivel incluir itens duplicados (com o mesmo codigo).
    Retornar o item incluido em caso de sucesso e None em caso
    de item duplicado.
    '''
    def inclui_item_pedido(self, codigo, descricao, preco):
        for item in self.__itens:
            if item.codigo == codigo:
                return None
        novo_item = ItemPedido(codigo, descricao, preco)
        self.__itens.append(novo_item)
        return novo_item

    '''
    Exclui um item do pedido e retorna o item excluido
    Caso o item nao exista, retorne None
    '''
    def exclui_item_pedido(self, codigo):
        for item in self.__itens:
            if item.codigo == codigo:
                self.__itens.remove(item)
                return item

        return None


    '''
    Deve calcular o valor total do pedido, considerando um custo
    adicional pela distancia e fator por distancia percorrida. 
    O fator da distancia varia de acordo com o tipo de pedido.
    O fator_distancia do TipoPedido deve ser multiplicado pela distancia 
    e acrescido ao valor total dos itens. 
    Por exemplo, se o fator_distancia for 2 e a distancia for 5, 
    o total do pedido deve ser acrescido em 10. 
    Ainda, se o cliente for ClienteFidelidade, deve  diminuir o valor total 
    pelo percentual de desconto armazenado no atributo desconto do ClienteFidelidade. 
    Por exemplo, se o valor de desconto for 0.2 e o pedido custar 10, o desconto deve ser
    de 2 e o valor final 8.
    @return um float correspondente ao total do pedido
    '''
    def calcula_valor_pedido(self, distancia: float):
        valor_total = 0

        for item in self.__itens:
            valor_total += item.preco_unitario

        valor_total += self.__tipo.fator_distancia * distancia

        if isinstance(self.cliente, ClienteFidelidade):
            desconto = self.cliente.desconto
            valor_total = valor_total * (1 - desconto)

        return valor_total

