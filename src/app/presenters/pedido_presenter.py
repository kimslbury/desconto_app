from src.app.entities.pedido import Pedido


class PedidoPresenter:
    def apresentar(self, pedido: Pedido) -> str:
        return (
            f"Cliente: {pedido.cliente}\n"
            f"Valor final: {pedido.valor_final()}"
        )

