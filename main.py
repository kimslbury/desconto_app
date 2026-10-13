from src.app.adapters.controllers.pedido_controller import PedidoController
from src.app.adapters.repositories.pedido_repository import PedidoRepository
from src.app.dtos.criar_pedido_input_dto import CriarPedidoInputDTO
from src.app.frameworks.database.memory_database import MemoryDatabase
from src.app.presenters.pedido_presenter import PedidoPresenter
from src.app.use_cases.criar_pedido import CriarPedido


if __name__ == "__main__":
    database = MemoryDatabase()
    gateway = PedidoRepository(database)
    criar_pedido = CriarPedido(gateway)
    controller = PedidoController(criar_pedido)
    presenter = PedidoPresenter()

    pedidos = [
        CriarPedidoInputDTO("Cliente 1", 100.0, "normal"),
        CriarPedidoInputDTO("Cliente 2", 100.0, "vip"),
        CriarPedidoInputDTO("Cliente 3", 100.0, "premium"),
    ]

    for dados in pedidos:
        controller.criar(dados)

    for pedido in gateway.listar():
        print(presenter.apresentar(pedido))
