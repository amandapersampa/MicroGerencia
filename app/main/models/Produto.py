# coding=utf-8
from sqlalchemy import update
from sqlalchemy.orm import relationship

from app import db

class Produto_dao(db.Model):
    __tablename__ = "produto"
    id_produto = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, unique=True)
    quantidade= db.Column(db.Integer)
    qtd_minima = db.Column(db.Integer)
    item_estoque_vld = db.Column(db.String)
    compra = relationship("Compra_dao", back_populates="produto", uselist=False)

    id_unidade_medida = db.Column(db.Integer, db.ForeignKey('unidademedida.id_unidade_medida'))
    unidade = relationship("Unidade_medida_dao", back_populates="produto")

    ingrediente = relationship("Item_cardapio_dao", back_populates="produto", uselist=False)

    def __init__(self, nome, unidade_medida, quantidade, qtd_minima, item_estoque_vld):
        self.nome = nome
        self.id_unidade_medida = unidade_medida
        self.quantidade = quantidade
        self.qtd_minima = qtd_minima
        self.item_estoque_vld = item_estoque_vld

    def salvar(self):
        print(self.quantidade)
        db.session.add(self)
        db.session.commit()

    def update(self):
        #db.session.query(self).update({"nome": 'coca-cola'})
        stmt = update(self).where("produto.id_produto" == self.id_produto). \
            values(nome='coca-cola')
        db.session.commit()


    @staticmethod
    def listar(id):
        print(Produto_dao.query.get(id).to_JSON)
        return Produto_dao.query.get(id)

    @staticmethod
    def findAll():
        return Produto_dao.query.all()

    @staticmethod
    def findById(id_produto):
        return Produto_dao.query.get(id_produto)

    @staticmethod
    def filter_nome(nome):
        return Produto_dao.query.filter_by(nome=nome).first()

    def __repr__(self):
        return str({"id_Produto": self.id_produto, "nome": self.nome, "quantidade": self.quantidade, "unidade": self.unidade.nome})


