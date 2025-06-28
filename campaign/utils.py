

def get_offset(params, def_count=10):
    count = int(params.get('count', def_count))
    offset = int(params.get('offset', 0))

    if offset > 0:
        total = offset + count
    else:
        total = count
    return offset, total