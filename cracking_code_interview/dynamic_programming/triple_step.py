


def triple_step(step_sizes, steps):

    possibles = [0] * (steps + 1)
    possibles[0] = 1


    for step_size in step_sizes:

        for i in range(step_size, steps + 1):
            possibles[i] = possibles[i] + possibles[i - step_size]

    print(possibles)











triple_step([1, 2, 3], 10)