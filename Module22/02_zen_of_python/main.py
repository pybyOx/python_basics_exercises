zen_file = open('zen.txt', 'r')

for string in [line for line in zen_file][::-1]:
    print(string.replace('\n', ''))

zen_file.close()
