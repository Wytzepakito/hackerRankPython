

def minimumBribes(q):
    # Write your code here
    q_index = 0
    passed = 0

    while (q_index < len(q)):
        print(q_index)
        if q[q_index] == q_index + 1:
            q_index += 1
        elif q[q_index] == q_index + 2:
            q_index += 2
            passed += 1
        elif q[q_index] == q_index + 3:
            q_index += 1
            passed += 2
        elif q[q_index] == q_index:
            q_index += 1
        elif q[q_index] > q_index + 4:
            print("Too chaotic")
            return
    print(passed)
        
        
minimumBribes([2, 1, 5, 3, 4])

minimumBribes([2, 5, 1, 3, 4])