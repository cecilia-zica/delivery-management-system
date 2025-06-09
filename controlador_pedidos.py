from pedido_duplicado_exception import PedidoDuplicadoException
from pedido import Pedido


class ControladorPedidos():
    def __init__(self, pedidos: list):
        self.__pedidos = pedidos

    @property
    def pedidos(self):
        return self.__pedidos

    @pedidos.setter
    def pedidos(self, pedidos: list):
        if isinstance(pedidos, list):
            self.__pedidos = pedidos

    '''
    Busca pedido pelo numero.
    Se o pedido nao existir, deve retornar None
    Caso contrario, retorna o pedido.
    '''
    def busca_pedido_por_numero(self, numero):
        for pedido in self.__pedidos:
            if pedido.numero == numero:
                return pedido
        return None

    '''
    Incluir pedido na lista.
    Tratar os casos de instancias incorretas e pedido duplicado.
    Caso o pedido já exista na lista, gerar a excecao: 
    PedidoDuplicadoException
    '''
    def incluir_pedido(self, pedido):
        if not isinstance(pedido, Pedido):
            return None

        for pedido_existente in self.__pedidos:
            if pedido_existente.numero == pedido.numero:
                raise PedidoDuplicadoException()

        self.__pedidos.append(pedido)

        # --- OR ---
        # if isinstance(pedido, Pedido):
        #     for pedido_na_lista in self.__pedidos:
        #         if pedido_na_lista == pedido.numero:
        #             raise PedidoDuplicadoException
        #
        # self.__pedidos.append(pedido)
        # return pedido

    '''
    Exclui pedido pelo numero.
    Se o pedido nao existir, deve retornar None
    Caso contrario, retorna o pedido excluido
    '''
    def excluir_pedido(self, numero):
        pedido = self.busca_pedido_por_numero(numero)

        if not isinstance(pedido, Pedido):
             return None

        self.__pedidos.remove(pedido)
        return pedido

    '''
    Deve calcular o total do faturamento para todos os
    itens pedidos por um CPF. 
    Recebe como parametro:
    distancia: um float que corresponde a distancia percorrida
    cpf: uma string representando o CPF do Cliente a ser faturado
    '''
    def calcular_faturamento_pedidos(self, distancia, cpf):
        faturamento_total = 0

        for pedido_na_lista in self.__pedidos:
            if pedido_na_lista.cliente.cpf == cpf:

                valor_pedido = pedido_na_lista.calcula_valor_pedido(distancia)
                faturamento_total += valor_pedido

        return faturamento_total


