

num = int(input())
string = ""
priors = []

for i in range(num):
    in_list = input().split(" ")
    op = int(in_list[0])


    if op == 1:
        priors.append(string)
        string += in_list[1]
    elif op == 2:
        k = int(in_list[1])
        priors.append(string)      
        string = string[:len(string) - k] 
    elif op == 3:
        k = int(in_list[1])
        print(string[k - 1])
    elif op == 4:
        string = priors.pop()

