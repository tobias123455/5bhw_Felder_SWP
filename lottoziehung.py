import random

def lottoziehung():
    # Wir haben 45 Zahlen (von 1 bis 45) und ziehen 6 davon ohne Wiederholung.
    zahlen = list(range(1, 46))  # Erstelle Liste von 1 bis 45
    gezogene_zahlen = []  #  speichern der gezogenen Zahlen

    # Wir ziehen 6 mal eine Zahl
    for i in range(6):
        # zufälliger Index aus der noch vorhandenen Liste wird gewähkt
        index = random.randint(0, len(zahlen) - 1)
        zahl = zahlen.pop(index)  # Mit pop nehmen wir die Zahl raus, damit sie nicht nochmal gezogen wird
        gezogene_zahlen.append(zahl)  # Füge die gezogene Zahl zur Ergebnisliste hinzu

    return gezogene_zahlen

def lotto_statistik(anzahl_ziehungen=1000):
    # Erstelle ein Dictionary, wo jede Zahl (1-45) als Key und  Häufigkeit als Value gespeichert wird
    statistik = {zahl: 0 for zahl in range(1, 46)}

    # 1000 Ziehungen 
    for _ in range(anzahl_ziehungen):
        ziehung = lottoziehung()  #eine Ziehung
        # Für jede gezogene Zahl wird der Zähler erhöht
        for zahl in ziehung:
            statistik[zahl] += 1

    return statistik

# Hauptprogramm
if __name__ == "__main__":
    # einzelne Lottoziehung und Ausgabe der gezogenen Zahlen
    ergebnis = lottoziehung()
    print("Gezogene Zahlen:", ergebnis)

    # Lotto-Statistik: 1000 Ziehungen und Ausgabe, wie oft jede Zahl gezogen wurde
    stat = lotto_statistik(1000)
    print("\nLotto Statistik nach 1000 Ziehungen:")
    for zahl, anzahl in sorted(stat.items()):
        print(f"Zahl {zahl}: {anzahl} mal gezogen")
