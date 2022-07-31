import top_dyno

FILE_PATH = 'top_dyno.json'


def main():
    # print(top_dyno.generate_random_dynos_data())

    top_dyno.create_random_dyno_deck(FILE_PATH)


if __name__ == "__main__":
    main()
