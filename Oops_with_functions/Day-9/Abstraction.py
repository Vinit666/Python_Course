from abc import ABC, abstractmethod


class car(ABC):
    def __init__(self):
        pass

    @abstractmethod  # in a abstract class if you initialize a abstract method then this method must be in the all inherited classes that inherit the abstarct class.
    def sound():
        print("Car sound.")


class audi(car):
    def __init__(self, model: str, engine: str):
        self.model = model
        self.engine = engine

    def sound():  # it is mendetory to initialize this here because of abstract method of ab class.
        print("Audi Sound")


a1 = audi("Audi AQ", "1200cc")
print(a1.model)
print(a1.engine)
