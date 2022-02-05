

def can_segment_string(string, dict):

    made_length = 0
    for i in range(len(string) + 1):
        if string[made_length:i] in dict:
            made_length += len(string[made_length:i])

    print(made_length)
    print(len(string))















print(can_segment_string("applepie", { "apple": 0, "apple": 0, "pear": 0, "pie": 0 }))


print(can_segment_string("applepeer", { "apple": 0, "apple": 0, "pear":0, "pie": 0}))
