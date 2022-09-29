def get_height():
    """Input user for height, repeat if not within bounds"""
    while True:
        h = input("Height: ").rstrip()
        try:
            h = int(h)
            if h < 9 and h > 0:
                return h
        except ValueError:
            print("Please enter a height value between 1 and 8 inclusive")


def draw_pyramids(current_height, total_height):
    """Draw pyramids recursively"""
    # If still more than 1 to finish, recurse
    if current_height > 1:
        draw_pyramids(current_height-1, total_height)

    # Make spaces
    spaces = total_height - current_height
    for i in range(spaces):
        print(" ", end="")

    for i in range(current_height):
        print("#", end="")

    print("  ", end="")

    for i in range(current_height):
        print("#", end="")

    # Finish level
    print("\n", end="")


def main():
    height = get_height()
    draw_pyramids(height, height)


if __name__ == '__main__':
    main()