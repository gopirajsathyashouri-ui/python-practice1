def word_frequency(sentence):
    counts = {}
    for word in sentence.lower().split():
        if word in counts:
            counts[word] += 1
        else :
            counts[word] = 1
    return counts
sentence = "Python python PYTHON is fun"
print(word_frequency(sentence))