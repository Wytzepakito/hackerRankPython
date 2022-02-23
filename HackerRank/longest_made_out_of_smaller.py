

def is_made_of_sub_words(word, hashset):

    if word in hashset:
        return True

    for i in range(word):
        sub_word = word[:i]
        rest_word = word[i:]
        if sub_word in hashset and is_made_of_sub_words(rest_word, hashset):
            return True
            





def get_longest(arr):

    hashset = set()

    for word in arr:
        hashset.add(word)


    arr.sort(key = len)

    arr = arr[::-1]
    longest = 0
    longest_word = ""
    for word in arr:
        if is_made_of_sub_words(word, hashset):
            if len(word) > longest:
                longest = len(word)
                longest_word = word

    return longest_word




















print(get_longest(["water", "polo", "tournament", "beer", "brandy", "whisky", "whiskybottle", "waterpolotournament", "barrel"]))