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

    # Display the three towers:
    for level in range(NUMBER_OF_HANOI_DISKS, -1, -1):
        for tower in (towers["A"], towers["B"], towers["C"]):
            if level >= len(tower):
                display_disk(0)  # Display the bare pole with no disk.
            else:
                display_disk(tower[level])  # Display the disk.
        print("")

    # Display the tower labels A, B, and C:
    empty_space = " " * (NUMBER_OF_HANOI_DISKS)
    print("{0} A{0}{0} B{0}{0} C\n".format(empty_space))


def display_disk(width):
    """Display a disk of the given width. A width of 0 means no disk."""
    empty_space = " " * (NUMBER_OF_HANOI_DISKS - width)

    if width == 0:
        # Display a pole segment without a disk:
        print(f"{empty_space}||{empty_space}", end="")
    else:
        # Display the disk:
        disk = "#" * width
        number_label = str(width).rjust(2, "_")
        print(f"{empty_space}{disk}{number_label}{disk}{empty_space}", end="")


if __name__ == '__main__':
    main()
