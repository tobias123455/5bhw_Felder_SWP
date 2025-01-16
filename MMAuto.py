#Auto mit Magic Methods
class Auto:
    def __init__(self, ps):
        # PS
        self.ps = ps

    def __len__(self):
        #MM len(), gibt PS zurueck
        return self.ps

    def __add__(self, other):
        # Ueberladen + Operator
        if isinstance(other, Auto):
            return self.ps + other.ps
        else:
            raise TypeError("Man kann nur Autos addieren!")

    def __sub__(self, other):
        # Ueberladen  - Operator
        if isinstance(other, Auto):
            return self.ps - other.ps
        else:
            raise TypeError("Man kann nur Autos subtrahieren!")

    def __mul__(self, other):
        # Ueberladen  * Operator
        if isinstance(other, Auto):
            return self.ps * other.ps
        else:
            raise TypeError("Man kann nur Autos multiplizieren!")

    def __eq__(self, other):
        # Ueberladen == Operator
        if isinstance(other, Auto):
            return self.ps == other.ps
        else:
            return False

    def __lt__(self, other):
        # Ueberladen  < Operator
        if isinstance(other, Auto):
            return self.ps < other.ps
        else:
            return False

    def __gt__(self, other):
        # Ueberladen > Operator
        if isinstance(other, Auto):
            return self.ps > other.ps
        else:
            return False

# Test:
# erstellen
auto1 = Auto(50)  #50PS
auto2 = Auto(60)  #60PS

# Test len()
print(len(auto1))  

# Test Addition
print(auto1 + auto2) 

# Test Subtraktion
print(auto2 - auto1) 

# Test Multiplikation
print(auto1 * auto2)  

# Test Vergleichsoperatoren
print(auto1 == auto2)  # False
print(auto1 < auto2)   # True
print(auto1 > auto2)   # False

# Test falscher Typen
try:
    print(auto1 + 10)  # Sollt Fehler werfen
except TypeError as e:
    print(e)

try:
    print(auto1 - "50")  # Sollt Fehler werfen
except TypeError as e:
    print(e)
