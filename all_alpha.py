alpha_set = set('abcdefghijklmnopqrstuvwxyz')
sentence_set = {'x', 'a', 'c', 'b'}


def includes_alphabet():
    return alpha_set.issubset(sentence_set)

print(includes_alphabet())

sentence_set = set('a quick red fox jumps over the lazy brown dog')
print(includes_alphabet())

sentence_set = set('the big wild zoo just recently having quieted down '
                   'for the known season hush keeping extra busy customers away')
print(includes_alphabet())

sentence_set = set("let's not go yet")
print(includes_alphabet())
