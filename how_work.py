def spin_words(sentence):
    for i in sentence:
        n = ''
        if len(i) >=5:
            n = i[::-1]
            sentence.insert(sentence.index(i),n)

    return sentence


print(spin_words('This is a testt'.split()))
