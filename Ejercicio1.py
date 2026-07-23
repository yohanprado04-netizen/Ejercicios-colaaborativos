#Crear una clase padre cultivo,con una atributo llamado consecha, un metodo llamado describir cuidado
#Clase hija: arroz, maiz, cada una debe describir su cuidados

class Cultivo:
    def __init__(self, cosecha):
        self.cosecha = cosecha
        
    def describir_cuidado(self):
        print(f"Cosecha esperada: {self.cosecha}.")
        print("Este cultivo requiere los cuidados generales de una planta.")

class Arroz(Cultivo):
    def __init__(self, cosecha):
        super().__init__(cosecha)
        
    def describir_cuidado(self):
        print(f"\n--- Cuidados para el cultivo de Arroz (Cosecha: {self.cosecha}) ---")
        print("- Requiere terrenos inundados o riego constante.")
        print("- Necesita control de malezas en etapas tempranas.")
        print("- Control de plagas (como barrenadores de tallo) a los 35-40 días.")

class Maiz(Cultivo):
    def __init__(self, cosecha):
        super().__init__(cosecha)
        
    def describir_cuidado(self):
        print(f"\n--- Cuidados para el cultivo de Maíz (Cosecha: {self.cosecha}) ---")
        print("- Necesita suelo fértil con buen drenaje y humedad controlada.")
        print("- Fertilización balanceada (N-P-K) y eliminación de malezas.")
        print("- Monitoreo constante de plagas como el gusano cogollero.")

cultivo_arroz = Arroz("4 a 5 toneladas por hectárea")
cultivo_maiz = Maiz("8 a 10 toneladas por hectárea")

cultivo_arroz.describir_cuidado()
cultivo_maiz.describir_cuidado()
