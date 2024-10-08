from romeo_and_juliet import PLAY


def get_words(text):
    """Splits a text into a list of words sets the word into lowercase and removes all none alphabetic letters"""
    list_of_all_words = text.split(' ')
    list_of_all_words_lowercase_and_without_non_alphabetic_characters = []
    for word in list_of_all_words:
        alphabetic_word = ''
        for char in word:
            if char.isalnum():
                alphabetic_word += char
        list_of_all_words_lowercase_and_without_non_alphabetic_characters.append(alphabetic_word.lower())
    return list_of_all_words_lowercase_and_without_non_alphabetic_characters


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
        freq.pop(
            most_used_word)  #Deletes the most used word out of 'freq' to search for the next most used word under it at next iteration


def main():
    """Program sequence"""
    print('Top 50 most frequent words:')
    top_n_words(words_frequency(get_words(PLAY)), 50)  #Calls all 3 functions.


if __name__ == "__main__":
    main()
