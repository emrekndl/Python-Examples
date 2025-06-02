# Creational
"""
Sınıfları bir interface yada sınıftan türeterek oluşturma işlemidir.
Genişletilebilir.
Sınıf sayısının çok olduğu durumda kullanışlıdır.
"""


class Person():
    def __init__(self):
        self.name = None
        self.gender = None

    def getName(self):
        return self.name

    def getGender(self):
        return self.gender


class Male(Person):
    def __init__(self, name):
        print(f"Hello Mr. {name}")


class Female(Person):
    def __init__(self, name):
        print(f"Hello Miss. {name}")


class Factory():
    def getPerson(self, name, gender):
        if gender == "M":
            return Male(name)
        if gender == "F":
            return Female(name)


if __name__ == '__main__':
    factory = Factory()
    liste = [['Ahmet', 'M'], ['Zuhal', 'F'], ['Veli', 'M']]
    for i in liste:
        person = factory.getPerson(i[0], i[1])
