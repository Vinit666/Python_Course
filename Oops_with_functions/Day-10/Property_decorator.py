class student:
    def __init__(self, name, age, gender):
        self._name = name
        self._age = age
        self._gender = gender

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, newgender):
        self._gender = newgender


s1 = student("vinit", 19, "male")
print(s1._name)
print(s1._age)
print(s1._gender)
print()
s1._gender = "boy"
print(s1._name)
print(s1._age)
print(s1._gender)
