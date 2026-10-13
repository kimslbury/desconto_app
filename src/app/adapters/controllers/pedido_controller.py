from src.app.dtos.criar_pedido_input_dto import CriarPedidoInputDTO
from src.app.entities.pedido import Pedido
from src.app.use_cases.criar_pedido import CriarPedido


class PedidoController:
    def __init__(self, criar_pedido: CriarPedido):
        self.criar_pedido = criar_pedido

    def criar(self, dados: CriarPedidoInputDTO) -> Pedido:
        return self.criar_pedido.executar(
            cliente=dados.cliente,
            valor_original=dados.valor_original,
            tipo_desconto=dados.tipo_desconto,
        )

