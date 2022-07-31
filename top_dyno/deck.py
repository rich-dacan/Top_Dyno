
import random
from utils import write_json, read_json

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
