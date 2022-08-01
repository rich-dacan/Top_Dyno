import top_dyno

FILE_PATH = 'top_dyno.json'


def main():
    # print(top_dyno.generate_random_dynos_data())

    # top_dyno.create_random_dyno_deck(FILE_PATH)

    p1_deck, p2_deck = top_dyno.generate_players_decks(FILE_PATH)

    # print(f'{p1_deck} \n')
    # print(p2_deck)

    print(top_dyno.get_random_attr(p1_deck[0]))


if __name__ == "__main__":
    main()

    # 36:34
