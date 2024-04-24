word_pairs = ['in the', 'in the', 'the jury', 'the jury', 'jury said', 'agriculture teacher']
target_words = ['past', 'time', 'said', 'recommended', 'that', ',']

size_of_vocab = []

with open('brown_vocab_100.txt') as data:
    for w in data:
        #if not '<s>' in w and not '</s>' in w:
        size_of_vocab.append(w)

def find_probabilities(preceeding_words, target_word, smoothing=False, alpha=1):
    with open('brown_100.txt') as corpus:
        preceeding_words_count = 0
        target_words_count = 0
        for s in corpus:
            preceeding_words_count += s.count(preceeding_words)
            target_words_count += s.count(target_word)
            """
            if preceeding_words in s.lower():
                preceeding_words_count += 1
            if f'{preceeding_words} {target_word}' in s.lower():
                target_words_count += 1
            """
    if smoothing:
        return (target_words_count + alpha) / (preceeding_words_count + alpha * len(size_of_vocab))
    else:
        return target_words_count / preceeding_words_count


turn_smoothing_off_on = [False, True]

for off_on in turn_smoothing_off_on:
    print()
    for index, pairs in enumerate(word_pairs):
        probability = find_probabilities(pairs, target_words[index], smoothing=off_on, alpha=0.1)
        print(f'P({target_words[index]} | {pairs}) = {probability}')


"""
There must be something wrong. I thought the way to calculate the probability was: P(w3 w2 w1) / P(w2 w1), not P(w3) / P(w2 w1)

Are '<s>' and '</s>' counted as part of the vocabulary?
"""
