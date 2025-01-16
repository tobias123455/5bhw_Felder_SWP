# Basisklasse Person
class Person:
    def __init__(self, name, geschlecht):
        if not isinstance(name, str) or not isinstance(geschlecht, str):
            # Fehlerprüfung: Neuer Fehler, nicht behebbar
            raise ValueError("Name und Geschlecht müssen Strings sein.")
        self.name = name  
        self.geschlecht = geschlecht 

#erbt von Klasse Person
class Mitarbeiter(Person):
    def __init__(self, name, geschlecht, abteilung):
        super().__init__(name, geschlecht) 
        if abteilung is None:
            # Fehlerprüfung: Neuer Fehler, behebbar
            print("Warnung: Abteilung ist None, Mitarbeiter ohne Abteilung erstellt.")
        self.abteilung = abteilung  

# erbt von  Klasse Mitarbeiter
class Abteilungsleiter(Mitarbeiter):
    def __init__(self, name, geschlecht, abteilung):
        try:
            super().__init__(name, geschlecht, abteilung) 
        except ValueError as e:
            # Fehlerprüfung: Hochgeblubberter Fehler, nicht behebbar
            raise ValueError(f"Fehler beim Erstellen des Abteilungsleiters: {e}")

#speichert Mitarbeiter und Abteilungsleiter
class Abteilung:
    def __init__(self, name):
        if not isinstance(name, str):
            # Fehlerprüfung: Neuer Fehler, nicht behebbar
            raise ValueError("Der Name der Abteilung muss ein String sein.")
        self.name = name  
        self.mitarbeiter = []  
        self.abteilungsleiter = None 

    def set_abteilungsleiter(self, abteilungsleiter):
        if not isinstance(abteilungsleiter, Abteilungsleiter):
            # Fehlerprüfung: Neuer Fehler, behebbar
            print("Warnung: Abteilungsleiter muss ein Objekt der Klasse Abteilungsleiter sein.")
        self.abteilungsleiter = abteilungsleiter  # Setzt den Abteilungsleiter

    def add_mitarbeiter(self, mitarbeiter):
        if not isinstance(mitarbeiter, Mitarbeiter):
            # Fehlerprüfung: Neuer Fehler, behebbar
            print("Warnung: Mitarbeiter muss ein Objekt der Klasse Mitarbeiter sein.")
            return
        self.mitarbeiter.append(mitarbeiter)  

#  Firma speichert alle Abteilungen.
class Firma:
    def __init__(self):
        self.abteilungen = [] 

    def add_abteilung(self, abteilung):
        if not isinstance(abteilung, Abteilung):
            # Fehlerprüfung: Neuer Fehler, behebbar
            print("Warnung: Hinzugefügtes Objekt ist keine Abteilung.")
            return
        self.abteilungen.append(abteilung)  
    def anzahl_mitarbeiter(self):
        try:
            return sum(len(abteilung.mitarbeiter) for abteilung in self.abteilungen)  
        except Exception as e:
            # Fehlerprüfung: Hochgeblubberter Fehler, behebbar
            print(f"Fehler beim Zählen der Mitarbeiter: {e}")
            return 0

    def anzahl_abteilungsleiter(self):
        try:
            return sum(1 for abteilung in self.abteilungen if abteilung.abteilungsleiter is not None) 
        except Exception as e:
            # Fehlerprüfung: Hochgeblubberter Fehler, behebbar
            print(f"Fehler beim Zählen der Abteilungsleiter: {e}")
            return 0

    def anzahl_abteilungen(self):
        try:
            return len(self.abteilungen)  
        except Exception as e:
            # Fehlerprüfung: Hochgeblubberter Fehler, behebbar
            print(f"Fehler beim Zählen der Abteilungen: {e}")
            return 0

    def groesste_abteilung(self):
        try:
            return max(self.abteilungen, key=lambda abteilung: len(abteilung.mitarbeiter), default=None)
        except ValueError as e:
            # Fehlerprüfung: Hochgeblubberter Fehler, behebbar
            print(f"Fehler beim Bestimmen der größten Abteilung: {e}")
            return None

    def geschlechterverhaeltnis(self):
        try:
            maenner = sum(
                1 for abteilung in self.abteilungen
                for mitarbeiter in abteilung.mitarbeiter + ([abteilung.abteilungsleiter] if abteilung.abteilungsleiter else [])
                if mitarbeiter.geschlecht == "m"
            )
            frauen = sum(
                1 for abteilung in self.abteilungen
                for mitarbeiter in abteilung.mitarbeiter + ([abteilung.abteilungsleiter] if abteilung.abteilungsleiter else [])
                if mitarbeiter.geschlecht == "w"
            )
            total = maenner + frauen
            if total == 0:
                # Fehlerprüfung: Neuer Fehler, nicht behebbar
                raise ZeroDivisionError("Keine Personen in der Firma vorhanden.")
            return (frauen / total * 100, maenner / total * 100)
        except ZeroDivisionError as e:
            # Fehlerprüfung: Hochgeblubberter Fehler, nicht behebbar
            print(f"Fehler beim Berechnen des Geschlechterverhältnisses: {e}")
            return (0, 0)

# Testcode
def test_programm():
    # Firma erstellen
    firma = Firma()

    # Abteilungen erstellen
    try:
        entwicklung = Abteilung(5)
        vertrieb = Abteilung("Vertrieb")
     ##   firma.add_abteilung(entwicklung)
        firma.add_abteilung(vertrieb)
    except ValueError as e:
        print(f"Fehler beim Erstellen einer Abteilung: {e}")

    # Mitarbeiter hinzufügen
    '''try:
        entwicklung.add_mitarbeiter(Mitarbeiter("Alice", "w", entwicklung))
        entwicklung.add_mitarbeiter(Mitarbeiter("Bob", "m", entwicklung))
        vertrieb.add_mitarbeiter(Mitarbeiter("Clara", "w", vertrieb))
    except ValueError as e:
        print(f"Fehler beim Hinzufügen eines Mitarbeiters: {e}")

    # Abteilungsleiter setzen
    try:
        entwicklung.set_abteilungsleiter(Abteilungsleiter("David", "m", entwicklung))
        vertrieb.set_abteilungsleiter(Abteilungsleiter("Eva", "w", vertrieb))
    except ValueError as e:
        print(f"Fehler beim Setzen eines Abteilungsleiters: {e}")
'''
    # Statistiken anzeigen
    print("Anzahl der Mitarbeiter in der Firma:", firma.anzahl_mitarbeiter())
    print("Anzahl der Abteilungsleiter in der Firma:", firma.anzahl_abteilungsleiter())
    print("Anzahl der Abteilungen in der Firma:", firma.anzahl_abteilungen())

    groesste_abt = firma.groesste_abteilung()
    if groesste_abt:
        print("Abteilung mit den meisten Mitarbeitern:", groesste_abt.name)

    frauen_prozent, maenner_prozent = firma.geschlechterverhaeltnis()
    print(f"Frauenanteil: {frauen_prozent:.2f}%")
    print(f"Männeranteil: {maenner_prozent:.2f}%")

# ausführen
test_programm()
