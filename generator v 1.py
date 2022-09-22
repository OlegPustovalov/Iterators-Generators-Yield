def flat_generator(list_):
    start = -1
    end = len(list_) - 1
    current_result = [] 
    while start < end :
        start += 1
        current_result = list_[start] 
        for item2 in current_result:
            yield(item2)

if __name__ == '__main__':
    nested_list = [ ['a', 'b', 'c'], ['d', 'e', 'f', 'h', False], [1, 2, None]]
# печать последовательности
    for item in flat_generator(nested_list):
        print(item)
# используем комперхеншн для формирования плоского списка из последовательности
    flat_list =[item for item in flat_generator(nested_list)]
    print(flat_list)