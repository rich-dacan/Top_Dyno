import random

from . import create_random_dyno_deck, generate_players_decks


def get_random_attr(card: dict) -> str:

    card_keys = [key for key in card.keys() if key != 'name']

    # -1 necessário pois toda lista se inicia um 0
    # rand_int = random.randint(0, len(card_keys) - 1)

    # return card_keys[rand_int]

    return random.choice(card_keys)


def play(filepath: str) -> None:

    create_random_dyno_deck(filepath)

    p1_deck, p2_deck = generate_players_decks(filepath)
