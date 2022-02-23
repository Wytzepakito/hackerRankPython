def pangrams(s):
    char_set = set()

    for char in s:
        low_char = char.lower()
        if ord(low_char) > 96 and ord(low_char) < 123:
            char_set.add(low_char)
    if len(char_set) == 26:
        return "pangram"
    return "not pangram"



pangrams("We promptly judged antique ivory buckles for the next prize")



pangrams("We promptly judged antique ivory buckles for the prize")