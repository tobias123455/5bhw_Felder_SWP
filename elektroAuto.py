class Auto:
    def __init__(self, marke, modell):
        self.marke = marke   # Marke 
        self.modell = modell # Modell 

    def start(self):
        # Standardstart-Methode für ein normales Auto
        print("Das Auto startet.")


class ElektroAuto(Auto):
    def __init__(self, marke, modell, batteriekapazitaet):
        # Ruf Konstruktor der Basisklasse Auto auf
        super().__init__(marke, modell)
        # Fügt das zusätzliche Attribut für die Batteriekapazität hinzu
        self.batteriekapazitaet = batteriekapazitaet 

    def start(self):
        # Überschreibt die start-Methode, damit sie lautlos startet
        print("Das Elektroauto startet lautlos!")


# Hauptprogramm 
if __name__ == "__main__":

    normales_auto = Auto("VW", "Golf")
    elektro_auto = ElektroAuto("Tesla", "Model 3", 75)  

    normales_auto.start()     
    elektro_auto.start()      