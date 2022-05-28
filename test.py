def grammercheck(word):
    data = ['a', 'e', 'i', 'o', 'u']

    if word[0] in data:
        return 'an ' + word
    else:
        return 'a ' + word

word = input()

print(grammercheck(word))
