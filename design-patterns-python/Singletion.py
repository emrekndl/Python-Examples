# Creational pattern
# Bir nesneden sadece bir tane oluşturulmasını garanti etmeye yarar

class Singleton:
    __instance = None
    @staticmethod
    def getInstance():
        """ Static access method. """
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Singleton.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self


s = Singleton()
print(s)

s1 = Singleton.getInstance()
print(s1)

s2 = Singleton.getInstance()
print(s2)

m = Singleton()
print(m)
