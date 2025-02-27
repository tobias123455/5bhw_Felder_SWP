# Basis-Klasse für alle Teammitglieder (Spieler, Trainer etc.)
class TeamMember:
    def __init__(self, name, age):
        self._name = name  #Name
        self._age = age    #Alter

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    def info(self):
        # Gibt grundlegende Infos über das Teammitglied zurück
        return f"{self._name}, {self._age} Jahre alt"


# Spieler erben von TeamMember und haben zusätzliche Eigenschaften
class Player(TeamMember):
    def __init__(self, name, age, position, number):
        super().__init__(name, age)
        self._position = position  # z.B. Stürmer, Verteidiger, etc.
        self._number = number      # Trikotnummer
        self._goals = 0            # Anzahl der geschossenen Tore

    @property
    def position(self):
        return self._position

    @property
    def number(self):
        return self._number

    def score_goal(self):
        # Erhöht die Tore um 1
        self._goals += 1

    def get_goals(self):
        return self._goals

    def info(self):
        # Überschreibt die info-Methode von TeamMember, um auch Position, Nummer und Tore anzuzeigen
        base_info = super().info()
        return f"{base_info} | Position: {self._position} | Nummer: {self._number} | Tore: {self._goals}"


# Trainer erben ebenfalls von TeamMember und haben eigene Eigenschaften
class Coach(TeamMember):
    def __init__(self, name, age, experience_years):
        super().__init__(name, age)
        self._experience_years = experience_years  # Anzahl der Jahre an Trainer-Erfahrung

    @property
    def experience_years(self):
        return self._experience_years

    def strategy(self):
        # Gibt simple Strategie aus
        return "Kick and Rush!"

    def info(self):
        # Überschreibt die info-Methode, um auch die Erfahrung anzuzeigen
        base_info = super().info()
        return f"{base_info} | Trainer mit {self._experience_years} Jahren Erfahrung"


# Die FootballTeam-Klasse kapselt alle Logiken rund um die Mannschaft
class FootballTeam:
    def __init__(self, team_name):
        self._team_name = team_name
        self._players = []  # Liste für Spieler
        self._coach = None  # Trainer

    def add_player(self, player):
        #Validierung
        if isinstance(player, Player):
            self._players.append(player)
        else:
            print("Ey, das ist kein Spieler!")

    def set_coach(self, coach):
        #Validierung
        if isinstance(coach, Coach):
            self._coach = coach
        else:
            print("Ey, das ist kein Trainer!")

    def team_info(self):
        # Gibt alle Infos zur Mannschaft aus (Trainer und Spieler)
        print(f"Team: {self._team_name}")
        if self._coach:
            print("Trainer:")
            print(self._coach.info())
        else:
            print("Kein Trainer gesetzt!")
        print("Spieler:")
        for player in self._players:
            print(player.info())

    def simulate_match(self):
        # Simuliert ein Match, in dem zufällig ein paar Spieler Tore schießen
        print("Match Simulation startet!")
        if not self._players:
            print("Keine Spieler im Team! shit")
            return
        import random
        # Jeder Spieler hat ca. 30% Chance, ein Tor zu schießen
        for player in self._players:
            if random.random() < 0.3:
                player.score_goal()
                print(f"{player.name} hat ein Tor geschossen!")
        print("Match Simulation beendet!")


# Hauptprogramm
if __name__ == "__main__":

    team = FootballTeam("Dortmund")

    team.add_player(Player("Max", 22, "Stürmer", 9))
    team.add_player(Player("Lukas", 24, "Verteidiger", 5))
    team.add_player(Player("Jonas", 21, "Mittelfeld", 8))
    team.add_player(Player("Tim", 23, "Torwart", 1))

    # Setzt Trainer
    team.set_coach(Coach("Herr Schmidt", 45, 20))

    # Zeigt Infos zur Mannschaft an
    team.team_info()

    # Simulieret ein Match
    team.simulate_match()

    # Zeigt nach dem Match nochmal die aktualisierten Infos an
    print("\nNach dem Match, Stats:")
    team.team_info()
