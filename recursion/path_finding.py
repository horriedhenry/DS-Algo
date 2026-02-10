def walk(
    maze: list, r_cord: int, c_cord: int, visited: list, cur_dir: str, path: list
) -> bool:
    # off the grid
    if r_cord < 0 or r_cord >= len(maze) or c_cord < 0 or c_cord >= len(maze[0]):
        return False

    # wall
    if maze[r_cord][c_cord] == 0:
        return False

    # visited
    if visited[r_cord][c_cord] == True:
        return False

    # End
    if maze[r_cord][c_cord] == -1:
        path.append(cur_dir)
        visited[r_cord][c_cord] = True
        return True

    # mark the valid position visited
    path.append(cur_dir)
    visited[r_cord][c_cord] = True

    # walk four directions from the current valid position
    # up
    if walk(maze, r_cord - 1, c_cord, visited, "U", path):
        return True

    # down
    elif walk(maze, r_cord + 1, c_cord, visited, "D", path):
        return True

    # right
    elif walk(maze, r_cord, c_cord + 1, visited, "R", path):
        return True

    # left
    elif walk(maze, r_cord + 1, c_cord, visited, "L", path):
        return True

    # if current walk failed for all other directions remove the direction
    # because it's invalid..
    """
        [
          [1, 0, 0, 0],
          [1, 1, 1, 0],
          [1, 0, 1, 1],
          [0, 1, 1, -1],
        ]
    """
    # without pop
    """
        T F F F
        T T T F
        T F T F
        F F T T

        S D D R R D D R
    """
    # with
    """
        T F F F
        T T T F
        T F T F
        F F T T

        S D R R D D R
    """
    path.pop()
    return False


def solve(
    maze: list, r_cord: int, c_cord: int, visited: list, cur_dir: str, path: list
):
    if walk(maze, r_cord, c_cord, visited, cur_dir, path):
        print("Fount the end...")
        for row in visited:
            for col in row:
                if col:
                    print("T", end=" ")
                else:
                    print("F", end=" ")
            print()
        print(" ".join(path))
    else:
        print("Cannot find a path to end")
        for row in visited:
            for col in row:
                if col:
                    print("T", end=" ")
                else:
                    print("F", end=" ")
            print()
        if len(path):
            print(" ".join(path))


maze = [
    [1, 0, 0, 0],
    [1, 1, 1, 0],
    [1, 0, 1, 1],
    [0, 1, 1, -1],
]

visited = [[False] * len(maze[0]) for _ in range(len(maze))]

path = []
initial_dir = "S"

solve(maze, 0, 0, visited, initial_dir, path)
