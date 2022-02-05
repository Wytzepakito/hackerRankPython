

def reverse_words(sentence):
    first_half = []
    second_half = []


    forward = 0
    backward = len(sentence) - 1

    while( forward <= backward):
        print(forward, backward)

        if sentence[forward] == " " and sentence[backward] == " ":
            forward_last_word = 0
            backward_last_word = len(sentence) 
            if len(first_half)>0:
                 forward_last_word = len(first_half[len(first_half) -1]) + 1
                 backward_last_word = len(sentence)  - len(second_half[0])
            first_half.append(sentence[backward:backward_last_word])
            second_half.insert(0, sentence[forward_last_word:forward])
            forward += 1
            backward -= 1

        elif sentence[forward] == " " and sentence[backward] != " ":
            backward -= 1
        elif sentence[forward] != " " and sentence[backward] == " ":
            forward += 1
        else:
            backward -= 1
            forward += 1
    print(first_half, second_half)






reverse_words("Hello World murica muchacos friend")