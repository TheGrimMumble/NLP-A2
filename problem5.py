word_pairs = ['in the', 'in the', 'the jury', 'the jury', 'jury said', 'agriculture teacher']
target_words = ['past', 'time', 'said', 'recommended', 'that', ',']

size_of_vocab = []

with open('brown_vocab_100.txt') as data:
    for w in data:
        if not '<s>' in w and not '</s>' in w:
            size_of_vocab.append(w)

def find_probabilities(preceeding_words, target_word, smoothing=False):
    with open('brown_100.txt') as corpus:
        preceeding_words_count = 0
        target_words_count = 0
        for s in corpus:
            if preceeding_words in s.lower():
                preceeding_words_count += 1
            if f'{preceeding_words} {target_word}' in s.lower():
                target_words_count += 1
    if smoothing:
        return (target_words_count + 1) / (preceeding_words_count + len(size_of_vocab))
    else:
        return target_words_count / preceeding_words_count

for index, pairs in enumerate(word_pairs):
    probability = find_probabilities(pairs, target_words[index])
    print(f'P({target_words[index]} | {pairs}) = {probability}')

for index, pairs in enumerate(word_pairs):
    probability = find_probabilities(pairs, target_words[index], smoothing=True)
    print(f'P({target_words[index]} | {pairs}) = {probability}')
