with open('zen.txt', 'r')as zen_file:
    for string in [line for line in zen_file][::-1]:
        print(string.replace('\n', ''))
