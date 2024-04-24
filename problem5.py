bigrams = [('in', 'the'), ('in', 'the'), ('the', 'jury'), ('the', 'jury'), ('jury', 'said'), ('agriculture', 'teacher')]
trigrams = [('in', 'the', 'past'), ('in', 'the', 'time'), ('the', 'jury', 'said'), ('the', 'jury', 'recommended'), ('jury', 'said', 'that'), ('agriculture', 'teacher', ',')]

vocabulary = []

with open('brown_vocab_100.txt') as vocab:
    for word in vocab:
        #if not '<s>' in word and not '</s>' in word:
        vocabulary.append(word)


def find_probabilities(bigram, trigram, smoothing=False, alpha=1):
    with open('brown_100.txt') as corpus:
        bigram_count = 0
        trigram_count = 0
        for sentence in corpus:
            words = sentence.lower().split()
            for i in range(len(words) - 2):
                if words[i] == bigram[0] and words[i + 1] == bigram[1]:
                    bigram_count += 1
                if words[i] == trigram[0] and words[i + 1] == trigram[1] and words[i + 2] == trigram[2]:
                    trigram_count += 1
    if smoothing:
        return (trigram_count + alpha) / (bigram_count + alpha * len(vocabulary))
    else:
        return trigram_count / bigram_count


turn_smoothing_off_on = [False, True]

for off_on in turn_smoothing_off_on:
    print(f'\nSmoothing: {off_on}')
    for index, bigram in enumerate(bigrams):
        probability = find_probabilities(bigram, trigrams[index], smoothing=off_on, alpha=0.1)
        print(f'P({trigrams[index][-1]} | {bigram[0]} {bigram[1]}) = {probability}')


"""
Are '<s>' and '</s>' counted as part of the vocabulary?
"""
