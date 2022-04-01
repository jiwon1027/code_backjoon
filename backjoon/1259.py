while True:
    data = input()
    if data == '0':
        break

    if data == data[::-1]:
        print('yes')
    else:
        print('no')
