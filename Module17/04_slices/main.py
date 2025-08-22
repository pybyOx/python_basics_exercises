alphabet = 'abcdefg'

alphabet = [alphabet[:],
            alphabet[::-1],
            alphabet[::2],
            alphabet[1::2],
            alphabet[:1],
            alphabet[-1],
            alphabet[3:4],
            alphabet[-3:len(alphabet)],
            alphabet[3:5],
            alphabet[4:2:-1]]

for index in range(10):
    print(index + 1, ':', alphabet[index])
