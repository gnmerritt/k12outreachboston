def split_dicts(row, dicts):
    """Extract sub dicts A & B given a dictionary full of A.bar, C.foo keys"""
    return [extract_dict(d, row) for d in dicts]


def extract_dict(prefix, row):
    if not prefix.endswith('.'):
        prefix = prefix + '.'

    return {k.replace(prefix, ''): v
            for k, v in row.items()
            if k.find(prefix) == 0}
