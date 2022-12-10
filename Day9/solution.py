f = open("Day9/input", "r")
moves = [line.rstrip() for line in f]
f.close()


def create_grid(size, start_position):
    grid = [["." for _ in range(0, size)] for _ in range(0, size)]
    grid[start_position[0]][start_position[1]] = "S"
    return grid


def print_grid(positions, visited=False):
    title = "Visited" if visited else "Positions"
    print(f"{ title } grid:")
    x_list = [x[0] for x in positions]
    y_list = [y[1] for y in positions]
    max_x = max(x_list)
    min_x = min(x_list)
    max_y = max(y_list)
    min_y = min(y_list)

    modifier_x = abs(min_x) if min_x < 0 else 0
    modifier_y = abs(min_y) if min_y < 0 else 0
    start_position = [modifier_x, modifier_y]
    grid = create_grid(
        max([abs(max_x) + modifier_x, abs(max_y) + modifier_y]) + 1, start_position
    )

    for i, position in enumerate(positions):
        x = position[0] + modifier_x
        y = position[1] + modifier_y
        grid[x][y] = grid[x][y].replace(".", "")
        if visited:
            grid[x][y] = grid[x][y] + "#"
        elif i == 0:
            grid[x][y] = grid[x][y] + "H"
        else:
            grid[x][y] = grid[x][y] + str(i)

    pivot_grid = []
    for x in range(0, len(grid)):
        pivot_grid.append([])
        for y in range(0, len(grid)):
            pivot_grid[x].append(grid[y][x])

    pivot_grid.reverse()
    for x in range(0, len(grid)):
        print(pivot_grid[x])


def move_tail(current_head, current_tail):
    tail_x, tail_y = current_tail
    head_x, head_y = current_head

    dist_x = head_x - tail_x
    dist_y = head_y - tail_y
    if abs(dist_x) > 1 or abs(dist_y) > 1:
        if head_x != tail_x and head_y != tail_y:
            tail_x = tail_x + 1 if dist_x > 0 else tail_x - 1
            tail_y = tail_y + 1 if dist_y > 0 else tail_y - 1
        elif head_x != tail_x:
            tail_x = tail_x + 1 if dist_x > 0 else tail_x - 1
        else:
            tail_y = tail_y + 1 if dist_y > 0 else tail_y - 1

        current_tail[0] = tail_x
        current_tail[1] = tail_y

    return current_tail


def move_head(direction, current_head):
    current_x, current_y = current_head

    if direction == "U":
        current_y = current_y + 1
    elif direction == "D":
        current_y = current_y - 1
    elif direction == "R":
        current_x = current_x + 1
    elif direction == "L":
        current_x = current_x - 1

    current_head[0] = current_x
    current_head[1] = current_y

    return current_head


def process_moves(with_grid=False):
    current_head = [0, 0]
    current_tail = [0, 0]
    tail_visited = {f"{current_tail[0]} {current_tail[1]}"}

    for move in moves:
        direction, steps = move.split()
        for _ in range(0, int(steps)):
            current_head = move_head(direction, current_head)
            current_tail = move_tail(current_head, current_tail)
            tail_visited.add(f"{current_tail[0]} {current_tail[1]}")

    # print(f"Current head and tail: {[current_head, current_tail]}")
    if with_grid:
        print_grid([current_head, current_tail])
        print_grid(
            [[int(p[0]), int(p[1])] for p in [v.split() for v in list(tail_visited)]],
            visited=True,
        )

    return tail_visited


def p1(with_grid=False):
    tail_visited = process_moves(with_grid)
    print(f"Tail visited {len(tail_visited)} positions.")


def p2():
    pass


def day9():
    p1()
    p2()
