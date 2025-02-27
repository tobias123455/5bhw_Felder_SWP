import random
import time
import unittest

# Zeitmesser Decorator, damit man sieht, wie lang eine Funktion braucht
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        # f-String (für )float-formatierung auf 2 Stellen)
        print(f"Zeit für {func.__name__}: {end_time - start_time:.2f} sec")
        return result
    return wrapper

# Funktion, die Deck generiert 
def generate_deck(suits, ranks):
    # Erstellt Deck als Liste
    return [(rank, suit) for suit in suits for rank in ranks]

# Funktion, die eine Hand zieht (ohne wiederholen)
def draw_hand(deck, hand_size):
    # random.sample um hand_size Karten ohne Duplikate zu ziehen
    return random.sample(deck, hand_size)

# Hf: Zählt, wie oft welcher Rang in der Hand vorkommt
def count_ranks(hand):
    counts = {}
    for card in hand:
        rank = card[0]
        counts[rank] = counts.get(rank, 0) + 1
    return counts

# Prüft, Flash vorhanden
def is_flush(hand):
    suits = [card[1] for card in hand]
    return len(set(suits)) == 1

# Prüft, ob Srasse vorhanden
def is_straight(hand, rank_order):
    # Holt die Position jedes Kartenrangs in der Reihenfolge
    indices = [rank_order.index(card[0]) for card in hand]
    indices.sort()
    # Checkt, ob aufeinanderfolgende Zahlen exakt 1 auseinander liegen
    for i in range(1, len(indices)):
        if indices[i] != indices[i - 1] + 1:
            return False
    return True

# Prüft, ob Poker vorhanden
def is_four_of_a_kind(hand):
    counts = count_ranks(hand)
    for count in counts.values():
        if count == 4:
            return True
    return False

# Prüft, ob Drillinge vorhanden
def is_three_of_a_kind(hand):
    counts = count_ranks(hand)
    for count in counts.values():
        if count == 3:
            return True
    return False

# Prüft, ob Paar vorhanden
def is_pair(hand):
    counts = count_ranks(hand)
    for count in counts.values():
        if count == 2:
            return True
    return False

# Bewertet Hand und gibt beste Kombination zurück
def evaluate_hand(hand, rank_order):
    # Wenn Hand Flash und Strasse hat, dann is es Straight Flush
    if is_flush(hand) and is_straight(hand, rank_order):
        return "Straight Flush"
    elif is_four_of_a_kind(hand):
        return "Poker"
    elif is_flush(hand):
        return "Flash"
    elif is_straight(hand, rank_order):
        return "Strasse"
    elif is_three_of_a_kind(hand):
        return "Drillinge"
    elif is_pair(hand):
        return "Paar"
    else:
        return "Hohe Karte"

# Simuliert Pokerspiel und sammelt für die Statistik
@timer
def simulate_poker(simulations, deck, hand_size, rank_order):
    # Macht eine Statistik als Dictionary, wo Kombinationen die Keys sind
    possible_combinations = ["Straight Flush", "Poker", "Flash", "Strasse", "Drillinge", "Paar", "Hohe Karte"]
    stats = {comb: 0 for comb in possible_combinations}

    for _ in range(simulations):
        hand = draw_hand(deck, hand_size)
        comb = evaluate_hand(hand, rank_order)
        stats[comb] += 1

    return stats

# Hauptfunktion: Liest Input, führt Simulation durch und gibt Ergebnisse aus
def run_simulation():
    try:
        simulation_input = input("Gib Anzahl der Simulationen ein (Standard 100000): ")
        if simulation_input.strip() == "":
            simulations = 100000
        else:
            simulations = int(simulation_input)
    except Exception as e:
        print("Fehler bei der Eingabe, Standardwert 100000 wird benutzt.")
        simulations = 100000

    # Kartenparameter
    suits = ['Herz', 'Karo', 'Pik', 'Kreuz']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    hand_size = 5

    deck = generate_deck(suits, ranks)

    stats = simulate_poker(simulations, deck, hand_size, ranks)

    print("\nErgebnisse Simulation:")
    for comb, count in stats.items():
        percentage = (count / simulations) * 100
        print(f"{comb}: {count} mal gezogen, Wahrscheinlichkeit von: {percentage:.4f}%")

    total_hands = 2598960  # Gesamtzahl der 5-Karten-Kombinationen in einem 52-Karten-Deck

    real_probabilities = {
        "Straight Flush": (40 / total_hands) * 100,
        "Poker": (624 / total_hands) * 100,
        "Flash": (5068 / total_hands) * 100,
        "Strasse": (10200 / total_hands) * 100,
        "Drillinge": (58656 / total_hands) * 100,
        "Paar": (1221792 / total_hands) * 100,
        "Hohe Karte": (1302540 / total_hands) * 100,
    }

    print("\nReale Wahrscheinlichkeiten der Kombinationen (laut Wikipedia):")
    for comb, prob in real_probabilities.items():
        print(f"{comb}: {prob:.4f}%")

    # Zeigt Beispielhand 
    sample_hand = draw_hand(deck, hand_size)
    print("\nBeispielhand:")
    print(sample_hand)

# Unittests für die Funktionen
class TestPokerSimulator(unittest.TestCase):
    def setUp(self):
        self.suits = ['Herz', 'Karo', 'Pik', 'Kreuz']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def test_is_flush_true(self):
        hand = [('2', 'Herz'), ('5', 'Herz'), ('10', 'Herz'), ('K', 'Herz'), ('A', 'Herz')]
        self.assertTrue(is_flush(hand))

    def test_is_flush_false(self):
        hand = [('2', 'Herz'), ('5', 'Karo'), ('10', 'Herz'), ('K', 'Herz'), ('A', 'Herz')]
        self.assertFalse(is_flush(hand))

    def test_is_straight_true(self):
        hand = [('7', 'Herz'), ('8', 'Karo'), ('9', 'Pik'), ('10', 'Kreuz'), ('J', 'Herz')]
        self.assertTrue(is_straight(hand, self.ranks))

    def test_is_straight_false(self):
        hand = [('7', 'Herz'), ('8', 'Karo'), ('9', 'Pik'), ('10', 'Kreuz'), ('Q', 'Herz')]
        self.assertFalse(is_straight(hand, self.ranks))

    def test_is_four_of_a_kind_true(self):
        hand = [('9', 'Herz'), ('9', 'Karo'), ('9', 'Pik'), ('9', 'Kreuz'), ('A', 'Herz')]
        self.assertTrue(is_four_of_a_kind(hand))

    def test_is_four_of_a_kind_false(self):
        hand = [('9', 'Herz'), ('9', 'Karo'), ('9', 'Pik'), ('A', 'Kreuz'), ('A', 'Herz')]
        self.assertFalse(is_four_of_a_kind(hand))

    def test_is_three_of_a_kind_true(self):
        hand = [('K', 'Herz'), ('K', 'Karo'), ('K', 'Pik'), ('3', 'Kreuz'), ('A', 'Herz')]
        self.assertTrue(is_three_of_a_kind(hand))

    def test_is_three_of_a_kind_false(self):
        hand = [('K', 'Herz'), ('K', 'Karo'), ('3', 'Pik'), ('3', 'Kreuz'), ('A', 'Herz')]
        self.assertFalse(is_three_of_a_kind(hand))

    def test_is_pair_true(self):
        hand = [('2', 'Herz'), ('2', 'Karo'), ('5', 'Pik'), ('9', 'Kreuz'), ('A', 'Herz')]
        self.assertTrue(is_pair(hand))

    def test_is_pair_false(self):
        hand = [('2', 'Herz'), ('3', 'Karo'), ('5', 'Pik'), ('9', 'Kreuz'), ('A', 'Herz')]
        self.assertFalse(is_pair(hand))

    def test_evaluate_hand(self):
        # Teste verschiedene Kombinationen mit evaluate_hand
        hand_flush = [('2', 'Herz'), ('5', 'Herz'), ('7', 'Herz'), ('9', 'Herz'), ('K', 'Herz')]
        self.assertEqual(evaluate_hand(hand_flush, self.ranks), "Flash")

        hand_straight = [('7', 'Herz'), ('8', 'Karo'), ('9', 'Pik'), ('10', 'Kreuz'), ('J', 'Herz')]
        self.assertEqual(evaluate_hand(hand_straight, self.ranks), "Strasse")

        hand_four = [('9', 'Herz'), ('9', 'Karo'), ('9', 'Pik'), ('9', 'Kreuz'), ('A', 'Herz')]
        self.assertEqual(evaluate_hand(hand_four, self.ranks), "Poker")

        hand_three = [('K', 'Herz'), ('K', 'Karo'), ('K', 'Pik'), ('3', 'Kreuz'), ('A', 'Herz')]
        self.assertEqual(evaluate_hand(hand_three, self.ranks), "Drillinge")

        hand_pair = [('2', 'Herz'), ('2', 'Karo'), ('5', 'Pik'), ('9', 'Kreuz'), ('A', 'Herz')]
        self.assertEqual(evaluate_hand(hand_pair, self.ranks), "Paar")

        hand_high = [('2', 'Herz'), ('4', 'Karo'), ('6', 'Pik'), ('8', 'Kreuz'), ('10', 'Herz')]
        self.assertEqual(evaluate_hand(hand_high, self.ranks), "Hohe Karte")

if __name__ == "__main__":
    # Abfrage, ob Unittests oder Simulation gestartet werden sollen
    mode = input("Zum Testen 't' eingeben oder Simulation 's': ").strip().lower()
    if mode == 't':
        print("Starte Unittests...")
        unittest.main(argv=['first-arg-is-ignored'], exit=False)
    else:
        run_simulation()
