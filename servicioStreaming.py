#crear una clase servicio de streaming, con un metodo llamado reproducir, y que tenga 2 clases hijas llamadas Netflix y Spotify. Cada clase hija debe implementar el método reproducir de manera diferente, mostrando un mensaje específico para cada servicio.
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

reproductor_netflix.reproducir()
reproductor_spotify.reproducir()