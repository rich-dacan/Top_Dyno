import random

from utils import read_json, write_json

DYNO_NAMES = ('Parasaurolophus', 'Stegosaurus',
              'Giganotosaurus', 'Triceratops', 'Velociraptor', 'Tyrannosaurus-Rex')


def generate_random_dynos_data() -> list[dict]:

    return [
        {
            'name': dyno_name,
            'strength': random.randint(1, 10),
            'agility': round(random.uniform(0, 10), 1),
            'height': round(random.uniform(0, 10), 2)
        }
        for dyno_name in DYNO_NAMES
    ]


def create_random_dyno_deck(filepath: str) -> None:

    generate_dynos = generate_random_dynos_data()

    write_json(filepath, generate_dynos)


def generate_players_decks(filepath: str):

    dyno_deck = read_json(filepath)

    split_deck = len(dyno_deck) // 2

    random.shuffle(dyno_deck)

    # retornar uma tupla com 2 decks
    # um deck começa do inicio e vai até a metade (split_deck) e o segundo faz o inverso.

    return (dyno_deck[:split_deck], dyno_deck[split_deck:])
