

def solve_coin_change(denomination, amount):

    solution = [0] * (amount + 1)
    solution[0] = 1

    for den in denomination:
        
        for i in range(den, amount + 1):
            print(solution[i - den])
            solution[i] += solution[i - den]
        print(list(range(9)))
        print(solution)
        print("="*20)




solve_coin_change([1, 2, 5], 8)















