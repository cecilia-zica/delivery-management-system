# main.py
from cliente import Cliente
from cliente_fidelidade import ClienteFidelidade
from tipo_pedido import TipoPedido
from pedido import Pedido
from controlador_pedidos import ControladorPedidos
from pedido_duplicado_exception import PedidoDuplicadoException


def run_demonstration():
    """
    Creates instances of classes and demonstrates the system's features.
    """
    print("--- Delivery Management System ---")

    # 1. Setup: Creating clients and order types
    regular_client = Cliente("111.111.111-11", "John Smith", "123 A Street", "9999-8888")
    loyalty_client = ClienteFidelidade("222.222.222-22", "Mary Jane", "456 B Street", "8888-7777", 101,
                                       0.10)  # 10% discount

    standard_type = TipoPedido("Standard", 1.5)  # $1.50 per km
    fragile_type = TipoPedido("Fragile", 3.0)  # $3.00 per km

    # 2. Creating orders and adding items
    order1 = Pedido(101, regular_client, standard_type)
    order1.inclui_item_pedido(1, "The Lord of the Rings (Book)", 25.50)
    order1.inclui_item_pedido(2, "Notebook", 5.00)

    order2 = Pedido(102, loyalty_client, fragile_type)
    order2.inclui_item_pedido(3, "Ceramic Vase", 120.00)

    # 3. Calculating order values
    distance = 10.0
    order1_value = order1.calcula_valor_pedido(distance)
    order2_value = order2.calcula_valor_pedido(distance)

    print(f"\nCalculating order values for a delivery distance of {distance}km...")
    print(f" > Order 1 ({regular_client.nome}): ${order1_value:.2f}")
    print(f" > Order 2 ({loyalty_client.nome} with {loyalty_client.desconto * 100}% discount): ${order2_value:.2f}")

    # 4. Using the controller
    controller = ControladorPedidos()
    controller.incluir_pedido(order1)
    controller.incluir_pedido(order2)
    print("\nOrders 101 and 102 successfully added to the controller.")

    # 5. Testing exception handling
    try:
        print("Attempting to add a duplicate order (101)...")
        duplicate_order = Pedido(101, regular_client, standard_type)
        controller.incluir_pedido(duplicate_order)
    except PedidoDuplicadoException as e:
        print(f"Successfully caught expected error: {e}")

    # 6. Calculating total revenue for a client
    total_revenue = controller.calcular_faturamento_pedidos(distance, loyalty_client.cpf)
    print(f"\nTotal revenue for client {loyalty_client.nome} (CPF: {loyalty_client.cpf}): ${total_revenue:.2f}")

    # 7. Testing search and delete
    found_order = controller.busca_pedido_por_numero(101)
    if found_order:
        print(f"\nSuccessfully found order {found_order.numero}.")

    deleted_order = controller.excluir_pedido(101)
    if deleted_order:
        print(f"Successfully deleted order {deleted_order.numero}.")

    not_found_order = controller.busca_pedido_por_numero(101)
    if not not_found_order:
        print("Order 101 not found after deletion, as expected.")


if __name__ == "__main__":
    run_demonstration()