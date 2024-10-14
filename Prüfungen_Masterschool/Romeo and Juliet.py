from romeo_and_juliet import PLAY
import re

def get_words(text):
    """Sets the text into lower case and puts single words into a list"""
    text = text.lower()
    return re.findall('[a-z]+', text)


def words_frequency(words):
    """Returns a dictionary that shows each word one time and the amount it was in the text"""
    number_of_repetition_each_word = {}
    for word in words:
        if word not in number_of_repetition_each_word:
            number_of_repetition_each_word[word] = 0
            number_of_repetition_each_word[word] += 1
        else:
            number_of_repetition_each_word[word] += 1
    return number_of_repetition_each_word


def top_n_words(freq, n):
    """Prints the most used words. With freq change the text and with how long the list of the most used numbers should be"""
    for _ in range(n):  #Repeats how often to search for the most used word.
        most_used_word = ''
        count_most_used_word = 0
        for current_word, current_count in freq.items():
            if current_count > count_most_used_word:  # Check if current_word is more used than most_used_word, if its bigger replace with bigger counter and word
                count_most_used_word = current_count
                most_used_word = current_word
        print(f'{most_used_word}: {count_most_used_word}')
        freq.pop( most_used_word)  #Deletes the most used word out of 'freq' to search for the next most used word under it at next iteration


def main():
    """Program sequence"""
    print('Top 50 most frequent words:')
    top_n_words(words_frequency(get_words(PLAY)), 50)  #Calls all 3 functions.


if __name__ == "__main__":
    main()


#Old solution reworked but still not precice enough
"""def get_words(text):
    text = text.lower()
    list_of_all_words = text.split()
    list_of_all_words_lowercase_and_without_non_alphabetic_characters = []
    for word in list_of_all_words:
        alphabetic_word = ''
        for char in word:
            if char.isalpha():
                alphabetic_word += char
        if alphabetic_word != '':
            list_of_all_words_lowercase_and_without_non_alphabetic_characters.append(alphabetic_word)
    return list_of_all_words_lowercase_and_without_non_alphabetic_characters"""