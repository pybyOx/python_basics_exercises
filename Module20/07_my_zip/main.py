def generator(string, tpl):
    my_generator = ((symbol, tpl[index]) for index, symbol in enumerate(string))
    print(my_generator)
    for pair in my_generator:
        print(pair)


user_string = 'abcd'
user_tpl = (10, 20, 30, 40)

generator(user_string, user_tpl)
