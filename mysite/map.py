def getLenght(iterable):
    return len(iterable)

def show_result(map_object):
    for item in map_object:
        print(item, end=' ')
    print('')

def print_Iter(iter_in):
    if isinstance(iter_in, str):
        print("The input iterable, '{}' is a String. Its length is {}.".format(iter_in, len(iter_in)))
    if isinstance(iter_in, (list, tuple, set)):
        print("The input iterable, {} is a {}. It has {} elements.".format(iter_in, type(iter_in).__name__, len(iter_in)))
        for item in iter_in:
            print("The {} contains '{}' and its length is {}.".format(type(iter_in).__name__, item, len(item)))
    if isinstance(iter_in, dict):
        print("The input iterable, {} is a {}. It has {} elements.".format(iter_in, type(iter_in).__name__, len(iter_in)))
        for key, value in iter_in.items():
            print("Dict key is '{}' and value is {}.".format(key, value))


iter_String = "Python"
print_Iter(iter_String)

map_result = map(getLenght, iter_String)
print("Type of map_result is {}".format(type(map_result)))

print("Lenghts are: ")
show_result(map_result)