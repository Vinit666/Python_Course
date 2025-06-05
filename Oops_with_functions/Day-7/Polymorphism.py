# polymorphism-->many forms of a thing
class animal:
    def sound(self):
        print("Animal Sound")


class dog(animal):
    def sound(self):
        print("Bhaw Bhaw Bhaw")


class cat(animal):
    def sound(self):
        print("Meuw meuw meuw")


class cow(animal):
    def sound(self):
        print("Mehh Mehh Mehh")


c1 = cat()
c1.sound()  # here it will override the sound () of animal class and first if cat class have the sound then it will run that ().
d1 = dog()
d1.sound()
