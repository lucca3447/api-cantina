from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from repositories.item_pedido_repository import ItemPedidoRepository
from repositories.pedido_repository import PedidoRepository
from repositories.produto_repository import ProdutoRepository
from schemas.item_pedido_schema import ItemPedidoCreate, ItemPedidoUpdate


class ItemPedidoService:
    def __init__(self, db: Session):
        self.repository = ItemPedidoRepository(db)
        self.produto_repository = ProdutoRepository(db)
        self.pedido_repository = PedidoRepository(db)

    def listar(self):
        return self.repository.listar()

    def buscar_por_id(self, id_item_pedido: int):
        item = self.repository.buscar_por_id(id_item_pedido)
        if not item:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Item de pedido nao encontrado"
            )

        return item

    def criar(self, item_pedido: ItemPedidoCreate):
        produto = self.produto_repository.buscar_por_id(item_pedido.id_produto)
        if not produto:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Produto nao encontrado"
            )

        pedido = self.pedido_repository.buscar_por_id(item_pedido.id_nota_fiscal)
        if not pedido:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Pedido nao encontrado"
            )

        return self.repository.criar(item_pedido)

    def atualizar(self, id_item_pedido: int, item_pedido: ItemPedidoUpdate):
        item_existente = self.repository.buscar_por_id(id_item_pedido)
        if not item_existente:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Item de pedido nao encontrado"
            )

        produto = self.produto_repository.buscar_por_id(item_pedido.id_produto)
        if not produto:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Produto nao encontrado"
            )

        pedido = self.pedido_repository.buscar_por_id(item_pedido.id_nota_fiscal)
        if not pedido:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Pedido nao encontrado"
            )

        return self.repository.atualizar(item_existente, item_pedido)

    def deletar(self, id_item_pedido: int):
        item = self.repository.buscar_por_id(id_item_pedido)
        if not item:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Item de pedido nao encontrado"
            )

        self.repository.deletar(item)
        return {"mensagem": "Item de pedido deletado com sucesso"}
