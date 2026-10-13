from dataclasses import dataclass


@dataclass(frozen=True)
class CriarPedidoInputDTO:
    cliente: str
    valor_original: float
    tipo_desconto: str

