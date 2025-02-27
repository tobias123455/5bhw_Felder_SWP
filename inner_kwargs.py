# Diese Funktion nimmt beliebig viele Positionsargumente (*args) und
# beliebig viele Keyword-Argumente (**kwargs) entgegen.
def demo_args_kwargs(*args, **kwargs):
    # *args ist ein Tuple mit allen Positionsargumenten.
    print("Die übergebenen args sind:")
    print(args) 
    
    # **kwargs ist ein Dictionary mit allen Keyword-Argumenten.
    print("Die übergebenen kwargs sind:")
    print(kwargs) 

    # innere Funktion, die alle Zahlen verdoppelt.
    def verdopple(zahl):
        return zahl * 2

    # Nutze die innere Funktion auf alle args, falls es Zahlen sind.
    print("\nErgebnis nach Verdopplung der args:")
    for arg in args:
        try:
            print(f"{arg} verdoppelt ist: {verdopple(arg)}")
        except Exception as e:
            # Falls arg keine Zahl ist, gib eine Meldung aus.
            print(f"{arg} kann nicht verdoppelt werden, weil es keine Zahl ist.")
    
    # Falls es im kwargs einen Schlüssel 'zahl' gibt, wende die innere Funktion darauf an
    if 'zahl' in kwargs:
        try:
            print(f"\nDas Keyword 'zahl' hat den Wert {kwargs['zahl']}, verdoppelt ist {verdopple(kwargs['zahl'])}")
        except Exception as e:
            print("Das Keyword 'zahl' konnte nicht verdoppelt werden.")

#  weitere Funktion, um verschiedene Aufrufe zu demonstrieren.
def main():
    print("Beispiel 1: Nur Positionsargumente")
    demo_args_kwargs(5, 10, 15)
    
    print("\nBeispiel 2: Nur Keyword-Argumente")
    demo_args_kwargs(name="Anna", alter=16, zahl=7)
    
    print("\nBeispiel 3: Mischung aus beiden")
    demo_args_kwargs(3, 6, 9, spruch="Hallo Welt", zahl=4, extra="Test")

if __name__ == "__main__":
    main()
