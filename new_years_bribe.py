import time

# def minimumBribes(q):
#     # Write your code here
#     q_index = 0
#     passed = 0

#     while (q_index < len(q)):
#         print(f"{q[q_index] =}, {q_index =}")
#         if q[q_index] == q_index + 1:
#             q_index += 1
#         elif q[q_index] == q_index + 2:
#             q_index += 1
#             passed += 1
#         elif q[q_index] == q_index + 3:
#             q_index += 1
#             passed += 2
#         elif q[q_index] == q_index:
#             q_index += 1
#         elif q[q_index] < q_index:
#             q_index += 1
#         elif q[q_index] >= q_index + 4:
#             print("Too chaotic")
#             return

#     print(passed)


def minimumBribes(q):
    increasing_stack = []
    pops = 0

    for i in range(len(q)):
        small_save = []
        if q[i] >= i + 4:
            print("Too chaotic")
            return
        while increasing_stack and increasing_stack[-1] > q[i]:
            small_save.append(increasing_stack.pop())
            pops +=1
        increasing_stack.append(q[i])
        increasing_stack.extend(small_save[::-1])
    print(pops)
    return
        


minimumBribes([1, 2, 5, 3, 7, 8, 6, 4,])
    
        
minimumBribes([2, 1, 5, 3, 4])

minimumBribes([2, 5, 1, 3, 4])


# minimumBribes([1, 2, 5, 3, 7, 8, 6, 4,])
