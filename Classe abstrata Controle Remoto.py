from abc import ABC, abstractmethod


class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    def marca(self):
        pass
class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a tv...")
        print("A tv está ligada!")

    def desligar(self):
        print("Desligando a tv...")
        print("A tv foi desligada!")

    @property
    def marca(self):
        return "LG"
class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("BIIP")
        print("O Ar condicionado está ligado!")

    def desligar(self):
        print("Biip")
        print("O Ar condicionado está Desligado!")

    @property
    def marca(self):
        return "HYUNDAI"

controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)

controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)
