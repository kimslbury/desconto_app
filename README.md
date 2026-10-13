# desconto_app

Sistema de pedidos para aplicar diferentes tipos de desconto.

## Estrutura

- `src/app/entities`: entidades e regras essenciais do negócio.
- `src/app/use_cases`: casos de uso da aplicação.
- `src/app/gateways`: contratos para salvar e listar pedidos.
- `src/app/adapters`: controllers e implementações de repositórios.
- `src/app/frameworks/database`: armazenamento em memória.
- `src/app/dtos` e `src/app/presenters`: entrada e apresentação dos dados.
- `src_antigo`: implementação anterior em arquitetura de camadas.

## Executar

```bash
python main.py
```

