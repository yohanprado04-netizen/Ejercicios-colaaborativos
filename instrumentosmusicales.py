class Instrumento:
  def tocar():
    pass

class Guitarra(Instrumento):
  def tocar(self):
    print("Sonido de guitarra")


class Tambor(Instrumento):
  def tocar(self):
    print("Sonido de tambor")

guitarra = Guitarra()
tambor = Tambor()

print("Probando la guitarra:")
guitarra.tocar()

print("\nProbando el tambor:")
tambor.tocar()