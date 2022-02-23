def marsExploration(s):
    # Write your code here

    sos_message = "SOS" * int((len(s)/3))
    diff_count =0
    print

    for real, original in zip(s, sos_message):
        if real != original:
            diff_count += 1

    return diff_count




print(marsExploration("SOSSPSSQSSOR"))