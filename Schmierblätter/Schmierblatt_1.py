from romeo_and_juliet import PLAY

# Splits a Text into a list of Words.
def get_words(text):
    list_of_all_words = text.split(' ')
    return list_of_all_words

def words_frequency(words):
    number_of_repetition_each_word = {}
    for word in words:
        if word not in number_of_repetition_each_word:
            number_of_repetition_each_word[word] = 0
            number_of_repetition_each_word[word] += 1
        else:
            number_of_repetition_each_word[word] += 1
    return number_of_repetition_each_word


def top_n_words(freq, n):
    top_50_words = {}
    for i in range(n):
        most_used_word = ''
        amount_most_used_word = 0
        for word, amount in freq.items():
            if amount > amount_most_used_word:
                amount_most_used_word = amount
                most_used_word = word
        top_50_words[most_used_word] = amount_most_used_word
    print(top_50_words)