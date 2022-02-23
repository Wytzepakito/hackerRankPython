






def reverse_words(sentence):


    list_sentence = [char for char in sentence]
    for i in range(len(list_sentence)// 2):
        temp = list_sentence[i]
        list_sentence[i] = list_sentence[len(sentence) - 1 - i]
        list_sentence[len(list_sentence) - 1 - i] = temp

    last_word = 0
    print("".join(list_sentence))
    for i in range(len(list_sentence)):
        if list_sentence[i]==" ":
            print("".join(list_sentence[last_word:i]))
            print(i)
            print(last_word)
            for j in range(0,(i - last_word) //2):
                print(j)
                temp = list_sentence[j + last_word]
                list_sentence[j + last_word] = list_sentence[i - 1 - j ] 
                list_sentence[i - 1 - j ] = temp
            print("".join(list_sentence[last_word:i]))
            last_word = i + 1


    print("".join(list_sentence))



reverse_words("Hello World murica muchacos friend")

