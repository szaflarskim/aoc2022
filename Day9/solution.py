GRID_SIZE = 500

f = open("Day9/input", "r")
moves = [line.rstrip() for line in f]
f.close()


def create_grid(size, start_position):
    grid = [["." for _ in range(0, size)] for _ in range(0, size)]
    grid[start_position[0]][start_position[1]] = "THS"
    return grid


def move_tail(grid, current_head, current_tail):
    tail_x, tail_y = current_tail
    head_x, head_y = current_head

    dist_x = head_x - tail_x
    dist_y = head_y - tail_y
    if abs(dist_x) > 1 or abs(dist_y) > 1:
        # update grid
        if "💩" in grid[tail_x][tail_y]:
            grid[tail_x][tail_y] = grid[tail_x][tail_y].replace("💩", "")
        grid[tail_x][tail_y] = grid[tail_x][tail_y].replace("T", "💩")

        if head_x != tail_x and head_y != tail_y:
            tail_x = tail_x + 1 if dist_x > 0 else tail_x - 1
            tail_y = tail_y + 1 if dist_y > 0 else tail_y - 1
        elif head_x != tail_x:
            tail_x = tail_x + 1 if dist_x > 0 else tail_x - 1
        else:
            tail_y = tail_y + 1 if dist_y > 0 else tail_y - 1

        grid[tail_x][tail_y] = grid[tail_x][tail_y] + "T"
        current_tail[0] = tail_x
        current_tail[1] = tail_y

    return current_tail


def move_head(grid, direction, current_head):
    current_x, current_y = current_head
    grid[current_x][current_y] = grid[current_x][current_y].replace("H", "")

    if direction == "U":
        current_y = current_y + 1
    elif direction == "D":
        current_y = current_y - 1
    elif direction == "R":
        current_x = current_x + 1
    elif direction == "L":
        current_x = current_x - 1

    try:
        if current_x < 0 or current_y < 0:
            raise (IndexError("Negative index - Grid too small!"))
        grid[current_x][current_y] = grid[current_x][current_y] + "H"
        current_head[0] = current_x
        current_head[1] = current_y
    except IndexError as e:
        print(f"Grid to small! Increase size and try again, {str(e)}")
        exit(1)
    return current_head


def process_moves(grid, start_position=[int(GRID_SIZE / 2), int(GRID_SIZE / 2)]):
    current_head = [start_position[0], start_position[1]]
    current_tail = [start_position[0], start_position[1]]
    tail_visited = {f"{current_tail[0]}{current_tail[1]}"}

    for move in moves:
        direction, steps = move.split()
        for _ in range(0, int(steps)):
            current_head = move_head(grid, direction, current_head)
            current_tail = move_tail(grid, current_head, current_tail)
            tail_visited.add(f"{current_tail[0]}{current_tail[1]}")
    return tail_visited


def p1(grid_size=GRID_SIZE, start_position=[int(GRID_SIZE / 2), int(GRID_SIZE / 2)]):
    grid = create_grid(grid_size, start_position)
    tail_visited = process_moves(grid, start_position)
    # for x in range(0, len(grid)):
    #     print("".join(grid[x]))
    print(f"Tail visited {len(tail_visited)} positions.")


def p2():
    pass


def day9():
    p1()
    p2()


