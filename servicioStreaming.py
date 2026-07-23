#crear una clase servicio de streaming, con un metodo llamado reproducir, y que tenga 2 clases hijas llamadas Netflix y Spotify.
#Cada clase hija debe implementar el método reproducir de manera diferente, mostrando un mensaje específico para cada servicio.
#
class ServicioStreaming:
    def reproducir(self):
        pass
    
    
class Netflix(ServicioStreaming):
    def reproducir(self):
        print("Reproduciendo contenido en Netflix... Disfruta de tus series y películas favoritas.")    

class Spotify(ServicioStreaming):
    def reproducir(self):
        print("Reproduciendo música en Spotify... Disfruta de tu lista de reproducción.")
        
reproductor_netflix = Netflix()
reproductor_spotify = Spotify() 

while True:
    def mostrar_menu():
        print("Bienvenido al servicio de streaming. Por favor, seleccione una opción:")
        print("1. Reproducir contenido en Netflix")
        print("2. Reproducir música en Spotify")
        print("3. Salir")
    mostrar_menu()
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        reproductor_netflix.reproducir()
    elif opcion == "2":
        reproductor_spotify.reproducir()
    elif opcion == "3":
        print("Saliendo del servicio de streaming. ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
        


    
