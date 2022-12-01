import functions

CMD_TO_FUNCTION = {
    'filter': functions.filter_query,
    'sort': functions.sort_query,
    'map': functions.map_query,
    'unique': functions.unique_query,
    'limit': functions.limit_query
}

FILE_NAME = 'data/apache_logs.txt'

# CMD_TO_FUNCTION[cmd]()  # получается вызов функции по имени



def build_query(cmd1, value1, cmd2, value2):

    with open(FILE_NAME) as file:
        prepared_data = list(map(lambda x: x.strip(), file))


    result_after_cmd1 = CMD_TO_FUNCTION[cmd1](param=value1, data=prepared_data)

    result = CMD_TO_FUNCTION[cmd2](param=value2, data=result_after_cmd1)

    return result
