data = input()


if data.find('pi') != -1:
    data = data.replace('pi', ' ')

if data.find('ka') != -1:
    data = data.replace('ka', ' ')

if data.find('chu') != -1:
    data = data.replace('chu', ' ')

if len(data.strip()) == 0:
    print('YES')
else:
    print('NO')



