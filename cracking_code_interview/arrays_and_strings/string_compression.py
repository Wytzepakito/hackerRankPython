def compress(string):
    if string == "":
        return ""

    last_char = None
    count = 0
    new_string = ""

    for char in string:
        if char != last_char:
            if last_char != None:
                new_string += last_char + str(count)
                
            count = 1
            last_char = char
        elif char == last_char:
            count+= 1

    new_string += string[len(string) -1] + str(count)

    print(new_string)







print(compress("aaaaabbbbbcccccddd"))