"""Implementation of Towers of Hanoi game in the CLI."""

NUMBER_OF_HANOI_DISKS = 5
SOLVED_TOWER = [i for i in range(NUMBER_OF_HANOI_DISKS, 0, -1)]


def main():
    """Tower of Hanoi game that displays in the Terminal."""

    towers = {"A": SOLVED_TOWER[:], "B": [], "C": []}

    while True:
        display_towers(towers)
        from_move, to_move = get_player_moves()
        if not towers[from_move]:
            print("Cannot move from a tower with no disks.")
            continue
        if not towers[to_move] or towers[from_move][-1] < towers[to_move][-1]:
            towers[to_move].append(towers[from_move].pop())
        else:
            print("That move is invalid. Cannot place a disk of higher value on top of another one.")
        if towers["B"] == SOLVED_TOWER or towers["C"] == SOLVED_TOWER:
            display_towers(towers)
            print("Congratulations! You won.")
            break


def get_player_moves():
    """Gets player moves as a pair (from,to)."""
    possible_moves = ["AB", "AC", "BA", "BC", "CA", "CB"]

    while True:
        player_move = input('Enter the letters of "from" and "to" i.e. AB.: ')
        if player_move not in possible_moves:
            print("Please enter a valid move. Possible moves are: ", possible_moves)
        else:
            from_move, to_move = player_move[0], player_move[1]
            return from_move, to_move


def display_towers(towers):
    """Display the three towers with their disks."""

    pass


if __name__ == '__main__':
    main()
