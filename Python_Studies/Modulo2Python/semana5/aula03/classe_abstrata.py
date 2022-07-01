from abc import ABC, abstractmethod


class Pagamento(ABC):

    @abstractmethod
    def pagar(self):
        print("Pagamento ...")


class PagamentoCartao(Pagamento):

    def pagar():
        print("Pagamento Cartão...")


class PagamentoBoleto(Pagamento):

    def pagar():
        print("Pagamento Boleto...")


class PagamentoPix(Pagamento):

    def pagar():
        print("Pagamento Pix... R$1000")


PagamentoBoleto.pagar()
PagamentoCartao.pagar()
PagamentoPix.pagar()
