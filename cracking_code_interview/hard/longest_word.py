



def sub_word_in_word(sub_word, word):
    pass





def longest_word(arr):

    arr.sort( key = len)
    print(arr)

    word_set = set()
    for word in arr:
        word_set.add(word)

    longest_word_len = 0
    longest_word = ""
    for word in arr:
        for i in range(len(word)):
            sub_word1 = word[:i]
            sub_word2 = word[i:]

            if sub_word1 in word_set and sub_word2 in word_set:
                if len(word) > longest_word_len:
                    longest_word = word
                    longest_word_len = len(word)

    return longest_word







print(longest_word(["cat", "banana", "dog", "nana", "walk", "walker", "dogwalker", "catbananawalker"]))