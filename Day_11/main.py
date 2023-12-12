
def get_points(space_increment: int):
    """Gets point coordinates from file
        :param space_increment: how much the horizontal space increases
    """
    points = set()
    i = 0
    for line in open("input.txt"):
        j = 0
        added = False
        for char in line:
            if char == "#":
                added = True
                points |= {(j, i)}
            j += 1
        if added is False:
            i += space_increment
        added = False
        i += 1
    return points


def account_for_space(p: set[tuple[int]], space_increment: int):
    """Accounts for horizonzal space (vertical space is accounted for in get_points function)
        :param p: set of coordinates
        :param space_increment: how much the vertical space increases
    """

    points_new = list(p.copy())
    max_vrt = max(p, key=lambda e: e[0])[0]

    for i in range(max_vrt + 1):
        if any(x == i for x, y in p):
            continue

        for index, (x, y) in enumerate(p):
            if x > i:
                a, b = points_new[index]
                points_new[index] = (a + 1 * space_increment, b)

    return points_new


def get_point_pairs(p: set[tuple[int]]) -> dict[set[tuple[int]]: int]:
    pairs = dict()
    for p1 in p:
        for p2 in p:
            if p2 == p1:
                continue
            if (p2, p1) in pairs:
                continue
            pairs[(p1, p2)] = 0
    return pairs


def calc_diff_sum(point_pairs: dict[set[tuple[int]]: int]):
    total = 0
    for galaxy1, galaxy2 in point_pairs:
        total += abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])
    print(total)


#  Part 1

points = get_points(1)
points = account_for_space(points, 1)
point_pairs = get_point_pairs(points)
calc_diff_sum(point_pairs)


#  Part 2

points = get_points(999999)
points = account_for_space(points, 999999)
point_pairs = get_point_pairs(points)
calc_diff_sum(point_pairs)
