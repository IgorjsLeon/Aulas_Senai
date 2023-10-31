class Animal:
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return "Au au"

class Gato(Animal):
    def emitir_som(self):
       return "Miau"

cachorro = Cachorro()
gato = Gato()

print(cachorro.emitir_som())
print(gato.emitir_som())