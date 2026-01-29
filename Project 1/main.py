from Solitaire import Solitaire


def main():
    wins = 0

    for games in range(1, 10001):
        game = Solitaire()
        if game.playGame():
            wins += 1

        if games % 1000 == 0:
            percent = (wins / games) * 100
            print(f"{wins}/{games} games won = {percent:.2f}%")


if __name__ == "__main__":
    main()
