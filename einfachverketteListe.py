import random

class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None

class EinfachVerketteteListe:
    def __init__(self):
        self.head = None

    def hinzufuegen(self, value: int):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def __len__(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def ausgabe(self):
        elements = []
        current = self.head
        while current is not None:
            elements.append(current.value)
            current = current.next
        print("Liste:", elements)

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        value = self.current.value
        self.current = self.current.next
        return value

def main():
    liste = EinfachVerketteteListe()
    
    for _ in range(10):
        zufallszahl = random.randint(1, 100)
        liste.hinzufuegen(zufallszahl)
    
    print("Länge der Liste:", len(liste))
    liste.ausgabe()

    print("Iteriere über die Liste:")
    for wert in liste:
        print(wert)

    # Benutzer-Eingabe: Zahl wird am Ende der Liste hinzugefügt
    try:
        benutzer_eingabe = int(input("Bitte geben Sie eine Ganzzahl ein, die am Ende der Liste hinzugefügt werden soll: "))
        liste.hinzufuegen(benutzer_eingabe)
        print("Nach der Hinzufügung:")
        liste.ausgabe()
        print("Länge der Liste:", len(liste))
    except ValueError:
        print("Ungültige Eingabe! Bitte geben Sie eine gültige Ganzzahl ein.")

if __name__ == '__main__':
    main()
