import collections
with open('input.txt') as file:
    passphrases = file.readlines()

n_ok = 0
for passphrase in passphrases:
    if len(set(passphrase.strip().split(' '))) == len(passphrase.strip().split(' ')):
        n_ok += 1

print n_ok, len(passphrases)

## Part two
n_ok = 0
for passphrase in passphrases:
    ok = 1
    words = passphrase.strip().split(' ')
    characters_words = [list(word) for word in words]
    for m, set_character in enumerate(characters_words):
        for k in range(m+1, len(characters_words)):
            if collections.Counter(set_character) == collections.Counter(characters_words[k]):
                ok = 0

    n_ok += ok

print n_ok, len(passphrases)




