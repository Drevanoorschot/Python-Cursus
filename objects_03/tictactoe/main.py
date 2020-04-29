from objects_03.tictactoe.models import Game, Player, Cell

if __name__ == '__main__':
    playing = True
    while playing:
        p_n1 = input("Name player 1: ")
        p_n2 = input("Name player 2: ")
        p1 = Player(p_n1, Cell.o)
        p2 = Player(p_n2, Cell.x)
        g = Game(p1, p2)
        winner = g.play()
        if winner is not None:
            inp = input("{player} won! play again? [Y/n] ".format(player=winner))
        else:
            inp = input("draw! play again? [Y/n]")
        while inp not in {"", "Y", "n"}:
            inp = input("play again? ")
        if inp == "n":
            break
    print("exiting game...")
