def filter_query(param, data):
    return list(filter(lambda x: param in x, data))


def sort_query(param, data):
    reverse = False if param == 'asc' else True
    return sorted(data, reverse=reverse)


def map_query(param, data):
    # отбирает колонку
    col_number = int(param)
    return list(map(lambda x: x.split(' ')[col_number], data))


def unique_query(data, *args, **kwargs):
    return list(set(data))


def limit_query(param, data):
    limit = int(param)
    return list(data)[:limit]
