def strip_edges_removal(s):
    if len(s) > 4:
        s = s.removeprefix(s[:2])
        s = s.removesuffix(s[-2:])
        return s
    return ''