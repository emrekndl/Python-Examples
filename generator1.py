import  sys
import  cProfile

#  generator with generator expression
karesiListe = [i**2 for i in range(10000)]
karesiGenerator = (i**2 for i in range(10000))

print(f"Liste:{type(karesiListe)}") #  \n{karesiListe}")
print(f"Generator:{type(karesiGenerator)}\n{karesiGenerator}")

print(f"Liste boyutu: {sys.getsizeof(karesiListe)}")
print(f"Generator boyutu: {sys.getsizeof(karesiGenerator)}")

print(cProfile.run('sum([i * 2 for i in range(10000)])'))
print(cProfile.run('sum((i * 2 for i in range(10000)))'))

def coklu_yield():
    mYield =  "Bu ilk yazılacak"
    yield  mYield
    mYield = "Bu ikinci yazılacak"
    yield  mYield

cYield = coklu_yield()
print(next(cYield))
print(next(cYield))
print(next(cYield))
