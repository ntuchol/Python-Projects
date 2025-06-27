from sortedcontainers import SortedDict

    ordered_map = SortedDict()
    ordered_map[3] = "c"
    ordered_map[1] = "a"
    ordered_map[2] = "b"

    for key, value in ordered_map.items():
        print(key, value)  # Output: (1, 'a'), (2, 'b'), (3, 'c')