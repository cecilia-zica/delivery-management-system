

class PedidoDuplicadoException(Exception):
    def __init__(self):
        super().__init__("Pedido jah estah duplicado!")
